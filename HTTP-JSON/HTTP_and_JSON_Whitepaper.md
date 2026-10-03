# HTTP and JSON

[ [Home](../README.md#8-http--json) ]

**What They Are, and Why They Matter to a Beginner Programmer**
*Zip Code Wilmington*

---

## About This Document <!-- omit from toc -->

[ [Top](#http-and-json) | [Home](../README.md#8-http--json) ]

This is part of Zip Code Wilmington's series of short, language-agnostic "concept" whitepapers. Nearly every server this program's students build, in every language track, speaks the same two things this document introduces: **HTTP**, the protocol shaping every request and response, and **JSON**, the format nearly every one of those messages carries as its body. Neither depends on the shell or Git covered elsewhere in this series — this is genuinely new vocabulary, worth learning precisely, since later material assumes it's already comfortable rather than re-explaining it.

---

## Table of Contents <!-- omit from toc -->

[ [Top](#http-and-json) | [Home](../README.md#8-http--json) ]

- [HTTP and JSON](#http-and-json)
  - [1. What Is HTTP?](#1-what-is-http)
  - [2. Why It Matters to a Beginner Programmer](#2-why-it-matters-to-a-beginner-programmer)
  - [3. Core Vocabulary](#3-core-vocabulary)
  - [4. A Request and a Response, Matched](#4-a-request-and-a-response-matched)
  - [5. Reading Real Traffic with curl](#5-reading-real-traffic-with-curl)
  - [6. POST, and Why a Write Is Treated Differently](#6-post-and-why-a-write-is-treated-differently)
  - [7. JSON: Five Types, and Nesting](#7-json-five-types-and-nesting)
  - [8. When JSON Breaks](#8-when-json-breaks)
  - [9. Common Beginner Mistakes](#9-common-beginner-mistakes)
  - [10. Key Takeaways](#10-key-takeaways)

---

## 1. What Is HTTP?

[ [Top](#http-and-json) | [Home](../README.md#8-http--json) ]

**HTTP**'s entire shape is one exchange, two messages: a client sends a **request**, and a server sends back exactly one **response**.

```
GET /businesses/1 HTTP/1.1
Host: miniyelp.local

HTTP/1.1 200 OK
Content-Type: application/json

{"id": 1, "name": "Joe's Pizza", "city": "Wilmington"}
```

A request's first line names a **verb** (`GET`), a **path** (`/businesses/1` — which specific resource is being asked for), and a protocol version. `Host:` says which server the request is meant for. A response mirrors that same structure: a **status line** (`200 OK`), **headers** (`Content-Type:` describing the body's format), and the **body** itself — the actual data.

---

## 2. Why It Matters to a Beginner Programmer

[ [Top](#http-and-json) | [Home](../README.md#8-http--json) ]

- **Almost every server you'll ever build speaks it.** Regardless of language, HTTP and JSON are the shared vocabulary underneath — learned once, assumed everywhere after.
- **A verb states intent, separately from the path.** `GET` means "give me this, without changing anything"; later verbs (`POST`, `PUT`, `DELETE`) mean create, replace, and remove respectively.
- **A status code is worth reading before the body, every time.** It's the response's own one-line summary of what actually happened.
- **`404` and `500` are worth keeping distinct.** A `404` is the server working *correctly* and reporting an honest "not here"; a `500` means something actually broke on the server's own side, and no amount of adjusting the request will fix it.

---

## 3. Core Vocabulary

[ [Top](#http-and-json) | [Home](../README.md#8-http--json) ]

| Term | Meaning |
|---|---|
| **Verb** (method) | States intent — `GET`, `POST`, `PUT`, `DELETE` |
| **Path** | Which specific resource is being addressed |
| **Status line** | The response's first line — protocol version, status code, reason |
| **Status code** | A one-line summary of what happened, worth reading before the body |
| **Header** | Metadata about the request or response, e.g. `Content-Type:` |
| **Body** | The actual data being sent or returned |

---

## 4. A Request and a Response, Matched

[ [Top](#http-and-json) | [Home](../README.md#8-http--json) ]

`200` broadly means success; `404` means the specific thing requested doesn't exist at that path; `500` means the server itself hit a problem handling the request.

That distinction between `404` and `500` matters beyond just recognizing the numbers: a `404` tells you the server is working fine and the thing you asked for genuinely isn't there — the fix, if any, is in what you're asking for. A `500` tells you the server itself failed while trying to handle an otherwise valid request — no amount of changing your request will help, since the problem is on the other side entirely.

---

## 5. Reading Real Traffic with curl

[ [Top](#http-and-json) | [Home](../README.md#8-http--json) ]

`curl -v` against a real API shows the entire exchange, not a clean diagram:

```bash
curl -v https://api.github.com/users/octocat
```

```
> GET /users/octocat HTTP/1.1
> Host: api.github.com
>
< HTTP/1.1 200 OK
< content-type: application/json; charset=utf-8
{"login": "octocat", "id": 1, ...}
```

Lines starting with `>` are what curl sent; `<` lines are what came back. A blank line after the request's `>` headers marks the boundary between headers and (absent, for a `GET`) body. Requesting something that truly doesn't exist returns a real `404`, body included — a `404` doesn't mean silence, it means a response explaining, correctly, that the requested thing isn't there.

---

## 6. POST, and Why a Write Is Treated Differently

[ [Top](#http-and-json) | [Home](../README.md#8-http--json) ]

A `GET` has no body — there's nothing to send, only something to request. A `POST` carries one: actual data describing what to create.

```
POST /businesses/1/reviews HTTP/1.1
Content-Type: application/json

{"author": "Kris", "rating": 5}

HTTP/1.1 201 Created
{"id": 42, "business_id": 1, "author": "Kris", "rating": 5}
```

`201 Created` is more specific than a generic `200`: it confirms not just success, but that something new now exists as a direct result, evidenced by the newly assigned `id`. This specificity is worth taking seriously — status codes carry real, precise information worth reading exactly, not just as a pass/fail signal.

The deeper reason a read and a write get handled differently: running the same `GET` ten times leaves the server in exactly the same state as running it once, since a read changes nothing. Running the same review-creating `POST` ten times creates ten separate reviews — a write's effects *accumulate* with repetition. This is why a browser warns before resubmitting a form, why network retries are considered safe for a `GET` but risky for a `POST`, and why real server code ends up treating read routes and write routes with genuinely different care.

---

## 7. JSON: Five Types, and Nesting

[ [Top](#http-and-json) | [Home](../README.md#8-http--json) ]

Every response body shown so far has actually been **JSON**. JSON has exactly five value types — string, number, boolean, `null`, and structure (object `{}` or array `[]`) — and nothing else; no functions, no loops, nothing beyond representing data, which is exactly what makes it simple enough for nearly any language to read and write identically.

```json
{
  "id": 1,
  "name": "Joe's Pizza",
  "reviews": [
    {"author": "Kris", "rating": 5},
    {"author": "Dana", "rating": 4}
  ]
}
```

A value in JSON can itself be another object or array — this is **nesting**, and it can go as deep as the data actually needs. Reading this by eye: "the second review" means index `1` of the `reviews` array (arrays are zero-indexed, so the first item is index `0`); "Dana's rating" means going into that second review object and reading its `rating` key. This by-eye reading — answering a specific "find this value" question without writing a single line of parsing code — is a genuinely practiceable skill, and exactly the one needed to sanity-check a real API's response before ever writing code against it.

---

## 8. When JSON Breaks

[ [Top](#http-and-json) | [Home](../README.md#8-http--json) ]

JSON has exactly one valid grammar at each point — a missing character in the wrong place makes the whole structure unreadable, not merely unattractive.

```json
{
  "name": "Joe's Pizza"
  "city": "Wilmington"
}
```

This is invalid: no comma follows `"Joe's Pizza"`, so nothing tells a reader (human or program) that a second key is starting. A mismatched brace or bracket — an array opened with `[` that never gets its matching `]`, closed too early by the wrong outer `}` — is a second common shape of the same underlying problem, best caught by counting and matching each opening symbol to its closing partner, the same discipline as matching parentheses in an equation.

A validator's error message is worth reading literally: "Expecting ',' delimiter" at a specific line and column names exactly what's missing and exactly where, rather than a vague "this is broken." That habit matters beyond fixing text by hand — real code that parses JSON automatically will, sooner or later, encounter malformed input, and this same skill (reading a parser's error message precisely, locating the exact spot) is what actually debugs it.

---

## 9. Common Beginner Mistakes

[ [Top](#http-and-json) | [Home](../README.md#8-http--json) ]

> **Treating every non-`200` response as "it's broken."** A `404` is the server working correctly and reporting an honest "not here" — only a `500` means something actually failed on the server's own side. Conflating the two wastes time chasing a fix in the wrong place.

> **Assuming a `GET` and a `POST` are equally safe to retry.** Repeating an identical `GET` leaves the server in exactly the same state; repeating an identical `POST` can create duplicate records, since a write's effects accumulate with every repetition.

> **Reading a JSON validator's error message as a vague "something's wrong"** instead of literally. "Expecting ',' delimiter" at a specific line and column names the exact fix and the exact place — skimming past that detail means re-reading the whole structure by hand instead of going straight to the one missing character.

> **Missing a comma between two JSON keys, or leaving a bracket or brace unmatched.** Both break the *entire* structure, not just the one line they appear on — count opening and closing symbols the same way you'd check that parentheses balance in an equation.

> **Forgetting that curl's blank line marks a real boundary.** Everything before the blank line in `curl -v`'s `>` output is headers; a `GET` has no body at all, so there's nothing after it to send.

---

## 10. Key Takeaways

[ [Top](#http-and-json) | [Home](../README.md#8-http--json) ]

- A request has a verb, a path, and headers; a response has a status code, headers, and a body — read the status code first, every time.
- `curl -v` reveals real traffic: `>` for what was sent, `<` for what came back, with a blank line marking the header/body boundary.
- `404` is an honest "not found"; `500` is the server's own failure — keeping the two distinct tells you where to actually look for a fix.
- A `POST` carries a body and, on success, often returns the more specific `201 Created` rather than a plain `200`.
- Reads are safe to repeat; writes accumulate effects — this is the real reason `GET` and `POST` get handled with different care, both by browsers and by the code you'll eventually write yourself.
- JSON has exactly five value types and supports nesting — a value can itself be a structure — and reading it by eye, correctly, needs no code at all.
- When JSON breaks, a validator's precise error message, read literally, points to the exact fix — the same skill that debugs real parsing code later.

---

*Zip Code Wilmington — HTTP and JSON: What They Are and Why They Matter*

[ [Top](#http-and-json) | [Home](../README.md#8-http--json) ]
