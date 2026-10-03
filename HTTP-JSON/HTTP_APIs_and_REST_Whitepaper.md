# HTTP APIs and REST Basics

[ [Home](../README.md#8-http--json) ]

**What They Are, and Why They Matter to a Beginner Programmer**
*Zip Code Wilmington*

---

## About This Document <!-- omit from toc -->

[ [Top](#http-apis-and-rest-basics) | [Home](../README.md#8-http--json) ]

This is the ninth in Zip Code Wilmington's series of short, language-agnostic "concept" whitepapers, and it picks up right where *HTTP and JSON* left off. That paper covered the *mechanics* of a single request and response — methods, status codes, headers, `curl`. This one covers the *design pattern* built on top of all of that: how a well-organized collection of endpoints hangs together into something recognizable as an **API**, and specifically a **REST API** — far and away the style you'll encounter most often, especially early in your career.

If any of "method," "status code," or "`curl`" feels unfamiliar, *HTTP and JSON* is worth a look first — this document builds directly on top of it rather than re-explaining it.

---

## Table of Contents <!-- omit from toc -->

[ [Top](#http-apis-and-rest-basics) | [Home](../README.md#8-http--json) ]

- [HTTP APIs and REST Basics](#http-apis-and-rest-basics)
  - [1. What Is an API?](#1-what-is-an-api)
  - [2. What Is REST, Specifically?](#2-what-is-rest-specifically)
  - [3. Why It Matters to a Beginner Programmer](#3-why-it-matters-to-a-beginner-programmer)
  - [4. Resources and URLs as Nouns](#4-resources-and-urls-as-nouns)
  - [5. Statelessness](#5-statelessness)
  - [6. Query Parameters, Pagination, and Authentication](#6-query-parameters-pagination-and-authentication)
  - [7. Common Beginner Mistakes](#7-common-beginner-mistakes)
  - [8. Key Takeaways](#8-key-takeaways)

---

## 1. What Is an API?

[ [Top](#http-apis-and-rest-basics) | [Home](../README.md#8-http--json) ]

An **API** — an **A**pplication **P**rogramming **I**nterface — is a defined set of operations one piece of software offers to another, without either side needing to know how the other is actually built inside. Think of a restaurant menu: you don't need to know anything about the kitchen's layout or the chef's technique to order a meal — you just need to know what's on the menu, and what you'll get back when you order it. An API is that same idea applied to software: a fixed, documented list of things you're allowed to ask for, and the shape of the answer you'll get.

A **web API** is simply an API you interact with over HTTP — the same request/response protocol from *HTTP and JSON* — which is why nearly everything in that earlier paper (methods, status codes, JSON bodies) shows up again here, just organized around a specific design philosophy.

---

## 2. What Is REST, Specifically?

[ [Top](#http-apis-and-rest-basics) | [Home](../README.md#8-http--json) ]

**REST** (**RE**presentational **S**tate **T**ransfer) is the most common architectural style for designing a web API — a set of conventions for organizing endpoints, not a strict protocol enforced by any official body. It was described by Roy Fielding in his year-2000 doctoral dissertation, and its central idea is simple to state, even though following it well takes some practice: **everything the API deals with is a resource**, each resource gets its own URL, and you act on that resource using the same handful of HTTP methods you already know.

A "resource" is just a noun — a user, an order, a photo, a book — and REST's whole design philosophy flows from treating URLs as *addresses for things*, and letting the HTTP method carry the *action*, rather than baking the action into the URL itself. Sections 4 and 5 unpack exactly what that means in practice.

---

## 3. Why It Matters to a Beginner Programmer

[ [Top](#http-apis-and-rest-basics) | [Home](../README.md#8-http--json) ]

- **You'll use REST APIs long before you build one.** Any web or mobile app that talks to a server — which is most of them — is making REST (or REST-like) API calls constantly, usually many times per screen.
- **You'll very likely be asked to build one.** A "build a small API" exercise is one of the most common early assignments and interview tasks in web development, and it's almost always expected to follow REST conventions.
- **It turns "learn this one company's weird custom API" into "recognize a pattern I already know."** Once you understand the resource/URL/method pattern, a brand-new, unfamiliar API stops being a mystery and becomes a matter of reading a few endpoint names and matching them to a shape you already recognize.
- **It's a launching point for everything else you'll hear about.** Newer styles like GraphQL and gRPC solve some of the same problems differently — but REST is overwhelmingly the one you'll meet first, and understanding it well makes those alternatives easier to place in context later.

---

## 4. Resources and URLs as Nouns

[ [Top](#http-apis-and-rest-basics) | [Home](../README.md#8-http--json) ]

The clearest way to see the REST pattern is to watch the same URL prefix get reused across every operation on one resource, with only the HTTP method changing:

| Action | Method | URL |
|---|---|---|
| List every book | `GET` | `/books` |
| Get one specific book | `GET` | `/books/42` |
| Create a new book | `POST` | `/books` |
| Replace a book entirely | `PUT` | `/books/42` |
| Partially update a book | `PATCH` | `/books/42` |
| Delete a book | `DELETE` | `/books/42` |

Notice the URL never changes shape to describe the action — it's always some form of `/books` or `/books/{id}`. The **method** (from *HTTP and JSON*) is what supplies the verb. This is exactly what it means to design URLs around nouns instead of verbs.

Contrast that with a non-RESTful design that bakes the verb directly into the URL instead: `/getBookById?id=42`, `/deleteBook?id=42`, `/createNewBook`. Nothing about that is technically broken — HTTP doesn't require REST conventions — but it's a strong signal that an API isn't following them, and it forces you to invent a new URL for every single action instead of reusing one consistent shape per resource.

`PUT` and `PATCH` are worth telling apart carefully: `PUT` conventionally means "replace this resource entirely with what I'm sending," while `PATCH` means "apply just these specific changes, and leave the rest alone." Sending a `PUT` with only one field filled in can, in a strict implementation, wipe out every other field on that resource — a genuinely common beginner mix-up.

---

## 5. Statelessness

[ [Top](#http-apis-and-rest-basics) | [Home](../README.md#8-http--json) ]

REST's least obvious, most important rule: each request must carry **everything** the server needs to understand and fulfill it, entirely on its own. The server isn't expected to remember anything about you from your last request — no memory of who you are, what you were just looking at, or what step you're on, unless you tell it again, every single time.

In practice, this means information like "who is making this request" (Section 6) has to be attached to *every* request — typically as a header — rather than established once and then silently remembered by the server afterward. It feels redundant at first, but it's what makes REST APIs so easy to scale: since no server involved is keeping any request-specific memory, literally any available server can handle any incoming request, with no need to route you back to "the one that remembers you."

---

## 6. Query Parameters, Pagination, and Authentication

[ [Top](#http-apis-and-rest-basics) | [Home](../README.md#8-http--json) ]

A resource's own URL (`/books/42`) identifies *which* thing you're asking about. **Query parameters** — appended after a `?`, separated by `&` — refine or filter that request instead:

```rest
GET /books?author=Tolkien&sort=title
```

This asks for books by a specific author, sorted by title — narrowing down a collection, rather than identifying one exact resource. Real-world collections are also rarely small enough to return all at once, so most APIs support **pagination** through query parameters too, commonly something like:

```rest
GET /books?page=2&limit=20
```

— fetching results twenty at a time, one page at a time, instead of every book in existence in a single enormous response.

Because of statelessness (Section 5), nearly every real API also requires **authentication** on every single request — proof of who's asking. The most common beginner-friendly form is an API key or token, most often sent as a header:

```rest
Authorization: Bearer abc123def456...
```

This is exactly where the lessons from *Git and Version Control* and *Environment Variables* converge: an API key is a secret, and it belongs in an environment variable read at runtime — never typed directly into source code, where it risks being committed and pushed somewhere public for anyone to find and use.

---

## 7. Common Beginner Mistakes

[ [Top](#http-apis-and-rest-basics) | [Home](../README.md#8-http--json) ]

> **Treating REST as a strict, enforced specification.** It's a set of conventions, not a rulebook with an authority checking compliance — plenty of real, working APIs bend or break these conventions in places. Recognizing the pattern doesn't mean every API you touch will follow it perfectly.

> **Baking a verb into the URL** (`/getBooks`, `/deleteBook`) instead of letting the HTTP method carry the action — a strong sign of drifting away from REST's core idea, even if the API still technically works.

> **Forgetting that the server doesn't remember you.** Sending authentication on your *first* request and assuming it carries over to the next one is a direct violation of statelessness — expect to include it every time, unless the specific API explicitly tells you otherwise (for instance, by handing you a short-lived session mechanism).

> **Hardcoding an API key directly into source code.** The single most common security mistake beginners make the first time they work with a third-party API — see *Environment Variables* for the fix.

> **Guessing at a request's expected shape instead of reading the documentation.** Required headers, expected field names, and exact data types vary from API to API — a few minutes with the actual docs saves much longer spent guessing why a request keeps failing.

> **Confusing `PUT` and `PATCH`.** Sending a `PUT` when you meant a partial update can silently erase fields you never intended to touch.

---

## 8. Key Takeaways

[ [Top](#http-apis-and-rest-basics) | [Home](../README.md#8-http--json) ]

- An API is a defined, documented set of operations one piece of software offers another — a web API is simply one you interact with over HTTP.
- REST is an architectural *style*, not an enforced protocol: everything is a resource, each resource has its own URL, and the HTTP method — not the URL — carries the action.
- Well-designed REST URLs are nouns (`/books`, `/books/42`); a verb baked into the URL is a sign an API has drifted from REST conventions.
- REST APIs are stateless — every request must carry everything the server needs on its own, including authentication, every single time.
- Query parameters filter and page through collections (`?author=Tolkien&page=2`), while the URL path itself identifies which specific resource you're addressing.
- API keys and tokens are secrets — they belong in environment variables, never hardcoded into source code or committed to version control.

---

*Zip Code Wilmington — HTTP APIs and REST Basics: What They Are and Why They Matter*

[ [Top](#http-apis-and-rest-basics) | [Home](../README.md#8-http--json) ]
