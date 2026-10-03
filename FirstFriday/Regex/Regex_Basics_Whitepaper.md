# Regex Basics

[ [Home](../../README.md#first-friday) ]

**What They Are, and Why They Matter to a Beginner Programmer**
*Zip Code Wilmington*

---

## About This Document <!-- omit from toc -->

[ [Top](#regex-basics) | [Home](../../README.md#first-friday) ]

This is the sixth in Zip Code Wilmington's series of short, language-agnostic "concept" whitepapers. Unlike most of the earlier topics, a regular expression isn't a system or a protocol — it's a small, specialized language of its own, just for describing patterns in text. It shows up inside nearly every other language and tool you'll touch, including a couple already covered in this series.

---

## Table of Contents <!-- omit from toc -->

[ [Top](#regex-basics) | [Home](../../README.md#first-friday) ]

- [Regex Basics](#regex-basics)
  - [1. What Is a Regular Expression?](#1-what-is-a-regular-expression)
  - [2. Why It Matters to a Beginner Programmer](#2-why-it-matters-to-a-beginner-programmer)
  - [3. Core Vocabulary](#3-core-vocabulary)
  - [4. Building a Pattern, Piece by Piece](#4-building-a-pattern-piece-by-piece)
  - [5. Regex in Practice: grep and Beyond](#5-regex-in-practice-grep-and-beyond)
  - [6. Common Beginner Mistakes](#6-common-beginner-mistakes)
  - [7. Key Takeaways](#7-key-takeaways)

---

## 1. What Is a Regular Expression?

[ [Top](#regex-basics) | [Home](../../README.md#first-friday) ]

A **regular expression** (regex, for short) is a compact pattern language for describing *shapes* of text — not one specific string, but a whole family of strings that all share some structure. "Three digits, then a hyphen, then four more digits" is a shape; `555-1234` and `867-5309` both fit it, and a regex lets you write that shape down precisely enough for a computer to check any string against it.

You've actually already seen a distant, much simpler relative of this idea: in *Essential Shell Commands*, a wildcard like `*.txt` matches any filename ending in `.txt`. That's the same basic instinct — describing a pattern instead of one exact name — but shell wildcards can only express a handful of very simple ideas. Regex is a full, much more expressive pattern language, capable of describing things like "a valid-looking email address" or "a line that starts with a number" with real precision. (It's worth remembering that these are two genuinely different systems with some overlapping symbols — more on that in Section 6, because it's a very common source of confusion.)

---

## 2. Why It Matters to a Beginner Programmer

[ [Top](#regex-basics) | [Home](../../README.md#first-friday) ]

- **It's everywhere, not just in one tool.** Nearly every programming language has regex support built into its standard library, and it's baked directly into command-line tools like `grep` and `sed`, into the search-and-replace box of most code editors, and into countless configuration files and validation rules.
- **It replaces a mountain of manual string-checking code.** Without regex, checking "does this look like a phone number?" means writing out character-by-character loops and conditionals by hand. With it, that check often fits on one line.
- **It's the backbone of searching and validating text.** Validating a form field, searching a log file for a specific kind of error, extracting a piece of data buried in a larger string — all classic regex jobs.
- **You've already met one of its most famous homes.** The `grep` command from the *Terminal and Shell* whitepaper's piping example is, historically, named after a regex operation — its name is short for "**g**lobal **r**egular **e**xpression **p**rint." Learning regex is what turns `grep` from "the tool that searches for text I type in" into "the tool that searches for any *shape* of text I can describe."

---

## 3. Core Vocabulary

[ [Top](#regex-basics) | [Home](../../README.md#first-friday) ]

| Symbol | Meaning |
|---|---|
| Literal characters | Match themselves exactly — `cat` matches the text "cat" |
| `.` | Any single character (except, usually, a newline) |
| `[...]` | A character class — any *one* character from the set, e.g. `[aeiou]` |
| `[^...]` | A negated character class — any one character **not** in the set |
| `\d` | Any digit, `0`-`9` |
| `\w` | Any "word" character — letters, digits, or underscore |
| `\s` | Any whitespace character — space, tab, or newline |
| `^` | Anchors the match to the start of the string (or line) |
| `$` | Anchors the match to the end of the string (or line) |
| `*` | Zero or more of whatever came immediately before it |
| `+` | One or more of whatever came immediately before it |
| `?` | Zero or one of whatever came immediately before it (i.e., "optional") |
| `{n,m}` | Between `n` and `m` repetitions of whatever came before it |
| `(...)` | A group — captures a piece of the match, or groups things for `*`/`+`/`?`/`\|` to apply to |
| `\|` | Alternation — "this **or** that" |

---

## 4. Building a Pattern, Piece by Piece

[ [Top](#regex-basics) | [Home](../../README.md#first-friday) ]

The best way to read (or write) a regex is left to right, one piece at a time. Take a simple phone-number pattern:

```
\d{3}-\d{3}-\d{4}
```

- `\d{3}` — exactly three digits
- `-` — a literal hyphen
- `\d{3}` — three more digits
- `-` — another literal hyphen
- `\d{4}` — four digits

Put together, that pattern matches `555-123-4567` but not `555-12-34567` or `555.123.4567` — the shape has to match exactly, hyphens and all.

A slightly more ambitious example, roughly matching an email-shaped string:

```
^[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}$
```

Read piece by piece: `^` anchors to the very start, `[\w.+-]+` allows one or more letters/digits/dots/pluses/hyphens (a rough stand-in for the part before the `@`), `@` matches a literal `@`, `[\w-]+` allows the domain name, `\.` matches a literal dot, `[a-zA-Z]{2,}` requires at least two letters (`com`, `org`, `io`), and `$` anchors to the very end.

It's worth being honest about that example's limits: fully validating an email address with regex alone is a famously deeper problem than it looks — the real specification allows far stranger addresses than most patterns account for. In practice, most real systems use a pattern like this as a quick, rough sanity check, and rely on actually sending a confirmation email to verify the address is truly valid and reachable.

---

## 5. Regex in Practice: grep and Beyond

[ [Top](#regex-basics) | [Home](../../README.md#first-friday) ]

The *Terminal and Shell* whitepaper used `grep` for a plain literal search:

```bash
grep "TODO" notes.txt
```

That's technically already a (very simple) regex — `TODO` matches itself, literally. The real power shows up once the pattern gets more specific:

```bash
grep -E "^[0-9]{3}-[0-9]{4}$" contacts.txt
```

The `-E` flag turns on "extended" regex syntax, and this pattern only matches lines that are *entirely* a phone-number shape like `555-1234`, start to finish — nothing before or after it on the line.

You'll find essentially the same pattern language, with small syntax differences, built into nearly every language you'll use: Python's `re` module, JavaScript's built-in `/pattern/` literals, Go's `regexp` package, and so on. Across all of them, the two operations you'll reach for constantly are the same: **test** whether a string matches a pattern at all (true/false), and **search-and-replace**, swapping every piece of a string that matches a pattern with something else.

---

## 6. Common Beginner Mistakes

[ [Top](#regex-basics) | [Home](../../README.md#first-friday) ]

> **Confusing regex symbols with shell wildcard symbols.** This is the single most common point of confusion for beginners who've just learned both. In a shell wildcard, `*` means "any characters at all." In regex, `*` means something narrower and easy to miss: "zero or more of whatever symbol came immediately before me." Matching "any characters at all" in regex actually requires `.*` — the `.` (any character) followed by `*` (repeated zero or more times). Two different systems, sharing one symbol with two different meanings.

> **Forgetting to escape a special character you want to match literally.** A bare `.` in a regex matches *any* character, not specifically a period — so a pattern meant to match `example.com` written as `example.com` would also incorrectly match `exampleXcom`. The fix is to escape it: `example\.com`.

> **Being surprised by greedy matching.** Quantifiers like `*` and `+` grab as much text as they possibly can by default. A pattern like `<.*>` intended to match one HTML-ish tag can, on a line with two tags, greedily stretch from the very first `<` to the very last `>`, swallowing everything in between instead of stopping at the first `>`.

> **Trying to use regex to fully validate deeply nested structure** — matching balanced parentheses, or fully parsing HTML or JSON. This isn't a skill gap; it's a genuine, well-known limitation of what regex as a pattern language can express. Nested, recursive structure is a job for an actual parser, not a regex.

> **Writing one giant, unreadable pattern in a single attempt.** Build a regex incrementally, testing it against real examples (an online regex tester, or just print statements) as you go, rather than trying to get a complex pattern exactly right on the first try.

---

## 7. Key Takeaways

[ [Top](#regex-basics) | [Home](../../README.md#first-friday) ]

- A regular expression describes a *shape* of text — a whole family of matching strings — not one specific string, and it's a genuinely different, more expressive system than shell wildcards.
- The core vocabulary is small: literal characters, character classes (`[...]`, `\d`, `\w`, `\s`), anchors (`^`, `$`), quantifiers (`*`, `+`, `?`, `{n,m}`), groups (`(...)`), and alternation (`|`) cover the overwhelming majority of everyday patterns.
- Read (and build) a pattern left to right, one piece at a time, rather than trying to take it in all at once.
- Regex is built into nearly every language and into essential command-line tools like `grep` — the same core language, with small syntax differences everywhere you find it.
- Watch for the two classic gotchas: `*` means something different in a shell wildcard than it does in regex, and unescaped special characters (like `.`) match more than you intend.
- Regex is genuinely bad at nested or recursive structure — reach for a real parser when the problem is "is this balanced/well-formed," not "does this look like the right shape."

---

*Zip Code Wilmington — Regex Basics: What They Are and Why They Matter*

[ [Top](#regex-basics) | [Home](../../README.md#first-friday) ]
