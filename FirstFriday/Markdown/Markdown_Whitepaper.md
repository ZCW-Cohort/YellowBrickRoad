# Markdown

[ [Home](../../README.md#first-friday) ]

**What It Is, and Why It Matters to a Beginner Programmer**
*Zip Code Wilmington*

---

## About This Document <!-- omit from toc -->

[ [Top](#markdown) | [Home](../../README.md#first-friday) ]

This is part of Zip Code Wilmington's series of short, language-agnostic "concept" whitepapers. It's also a bit of a special case: this document — like every other whitepaper in this collection — is itself written in the exact language it's about. Every heading, bold word, and bullet list you've seen so far in this series is Markdown source, quietly turned into the formatted page you're actually reading.

This paper is extra careful to show both halves of that transformation: for each of the seven most common Markdown features, you'll see the **raw Markdown source** exactly as it's typed, and the **HTML it actually produces** once a Markdown processor gets ahold of it.

---

## Table of Contents <!-- omit from toc -->

[ [Top](#markdown) | [Home](../../README.md#first-friday) ]

- [Markdown](#markdown)
  - [1. What Is Markdown?](#1-what-is-markdown)
  - [2. Why It Matters to a Beginner Programmer](#2-why-it-matters-to-a-beginner-programmer)
  - [3. How Markdown Becomes HTML](#3-how-markdown-becomes-html)
  - [4. The 7 Most Common Markdown Features](#4-the-7-most-common-markdown-features)
    - [1. Headings](#1-headings)
    - [2. Bold and Italic](#2-bold-and-italic)
    - [3. Lists](#3-lists)
    - [4. Links](#4-links)
    - [5. Images](#5-images)
    - [6. Code](#6-code)
    - [7. Blockquotes](#7-blockquotes)
  - [5. Common Beginner Mistakes](#5-common-beginner-mistakes)
  - [6. Key Takeaways](#6-key-takeaways)

---

## 1. What Is Markdown?

[ [Top](#markdown) | [Home](../../README.md#first-friday) ]

**Markdown** is a lightweight way of formatting plain text — headings, bold words, lists, links — using a small set of plain-keyboard symbols instead of the tags a web page actually needs. A **Markdown processor** (sometimes called a renderer or a compiler) reads that plain text and converts it into real **HTML**, the markup language browsers actually understand and display.

Markdown's defining design goal is that the *source* itself should already be readable, even before anything converts it. A line like `# Getting Started` still clearly reads as a heading even if nothing ever renders it — compare that to an HTML file full of `<div>` and `<span>` tags, which is far harder to read in its raw form.

---

## 2. Why It Matters to a Beginner Programmer

[ [Top](#markdown) | [Home](../../README.md#first-friday) ]

- **It's everywhere in software work.** A project's `README.md`, its documentation, its issue and pull-request descriptions, and code comments on most collaboration platforms are all written in Markdown.
- **This very whitepaper collection is written in it.** Every document in this series — this one included — is a plain `.md` file, formatted with exactly the seven features covered in Section 4.
- **It's fast, and it doesn't get in your way.** Because the source is plain text, you can write it in any editor, track its changes with ordinary version control, and never touch a mouse or a formatting toolbar to make a word bold.
- **Chat and forum tools borrow it constantly.** Slack, Discord, and GitHub's comment boxes all understand a close cousin of the same syntax — learn it once, and it works in more places than you'd expect.

---

## 3. How Markdown Becomes HTML

[ [Top](#markdown) | [Home](../../README.md#first-friday) ]

The pipeline is short: you write a plain text file with a few extra symbols in it; a Markdown processor reads that file and outputs HTML; a browser (or any HTML-aware viewer) reads that HTML and displays real formatting — a heading actually appears large and bold, a list actually gets bullet points.

Here's the whole pipeline for a single, tiny example:

**Source:**
```markdown
**hello**
```

**Renders to (HTML):**
```html
<strong>hello</strong>
```

Which a browser then displays as: **hello**

That three-step shape — Markdown source, then the HTML it produces, then what that HTML actually looks like — is exactly the pattern the rest of this document follows for each feature.

---

## 4. The 7 Most Common Markdown Features

[ [Top](#markdown) | [Home](../../README.md#first-friday) ]

### 1. Headings

[ [Top](#markdown) | [Back](#4-the-7-most-common-markdown-features) | [Home](../../README.md#first-friday) ]

**Source:**
```markdown
# Heading 1
## Heading 2
### Heading 3
```

**Renders to (HTML):**
```html
<h1>Heading 1</h1>
<h2>Heading 2</h2>
<h3>Heading 3</h3>
```

The number of `#` symbols sets the heading level (1 through 6) — a browser displays lower numbers larger and bolder. A space after the `#` is required; `#Heading` with no space isn't treated as a heading at all.

### 2. Bold and Italic

[ [Top](#markdown) | [Back](#4-the-7-most-common-markdown-features) | [Home](../../README.md#first-friday) ]

**Source:**
```markdown
**bold text**
*italic text*
```

**Renders to (HTML):**
```html
<strong>bold text</strong>
<em>italic text</em>
```

Double asterisks (or double underscores, `__like this__`) produce `<strong>` — displayed bold. Single asterisks (or single underscores) produce `<em>` — displayed italic.

### 3. Lists

[ [Top](#markdown) | [Back](#4-the-7-most-common-markdown-features) | [Home](../../README.md#first-friday) ]

**Source:**
```markdown
- First item
- Second item
- Third item

1. First step
2. Second step
3. Third step
```

**Renders to (HTML):**
```html
<ul>
  <li>First item</li>
  <li>Second item</li>
  <li>Third item</li>
</ul>

<ol>
  <li>First step</li>
  <li>Second step</li>
  <li>Third step</li>
</ol>
```

A leading `-`, `*`, or `+` produces an unordered list (`<ul>`), displayed with bullet points. A leading number and period produces an ordered list (`<ol>`), displayed with actual sequential numbers — worth knowing that the numbers you type don't even have to be correct; a Markdown processor renumbers the list itself, so `1.` repeated three times in the source still displays as 1, 2, 3.

### 4. Links

[ [Top](#markdown) | [Back](#4-the-7-most-common-markdown-features) | [Home](../../README.md#first-friday) ]

**Source:**
```markdown
[Zip Code Wilmington](https://zipcodewilmington.com)
```

**Renders to (HTML):**
```html
<a href="https://zipcodewilmington.com">Zip Code Wilmington</a>
```

The square brackets hold the clickable text; the parentheses right after hold the URL. A browser displays the bracketed text as an underlined, clickable link.

### 5. Images

[ [Top](#markdown) | [Back](#4-the-7-most-common-markdown-features) | [Home](../../README.md#first-friday) ]

**Source:**
```markdown
![Zip Code Wilmington logo](logo.png)
```

**Renders to (HTML):**
```html
<img src="logo.png" alt="Zip Code Wilmington logo">
```

The same shape as a link, with a `!` in front. The square brackets become the image's **alt text** — shown in place of the image if it fails to load, and read aloud by screen readers — and the parentheses hold the image's file path or URL. A browser displays the actual picture, not any text at all, when the image loads successfully.

### 6. Code

[ [Top](#markdown) | [Back](#4-the-7-most-common-markdown-features) | [Home](../../README.md#first-friday) ]

**Source:**
````markdown
Use the `print()` function to display output.

```python
print("Hello, Zip Code!")
```
````

**Renders to (HTML):**
```html
<p>Use the <code>print()</code> function to display output.</p>

<pre><code class="language-python">print("Hello, Zip Code!")
</code></pre>
```

Single backticks around a short piece of text produce inline `<code>` — displayed in a monospace font right in the middle of a sentence. A "fence" of three backticks on its own line starts a block of code, closed by another line of three backticks — displayed as a separate, monospace block, with the optional word right after the opening fence (`python`, here) telling the renderer which language to syntax-highlight it as.

### 7. Blockquotes

[ [Top](#markdown) | [Back](#4-the-7-most-common-markdown-features) | [Home](../../README.md#first-friday) ]

**Source:**
```markdown
> This is a quoted passage.
> It can span multiple lines.
```

**Renders to (HTML):**
```html
<blockquote>
  <p>This is a quoted passage.
  It can span multiple lines.</p>
</blockquote>
```

A `>` at the start of a line produces a `<blockquote>` — displayed indented, often with a visual bar down the left edge. This is exactly the syntax behind every **Common Mistake** callout in this whitepaper series, this document's own Section 5 included.

---

## 5. Common Beginner Mistakes

[ [Top](#markdown) | [Home](../../README.md#first-friday) ]

> **Forgetting a blank line before a list or heading.** Many Markdown processors need a genuinely empty line separating a paragraph from the list or heading that follows it — without one, the list can render as a single run-on paragraph instead of actual bullet points.

> **Leaving out the space after `#`.** `#Heading` (no space) is often left as plain text with a stray `#` in front of it, not converted into an actual heading — always write `# Heading`.

> **Nesting a fenced code block inside another fenced code block using the same three backticks.** The inner fence's closing backticks accidentally close the *outer* fence early. The fix — used in Section 4's own "Code" example — is to make the outer fence longer (four backticks instead of three) so it isn't confused with the shorter one nested inside it.

> **Assuming Markdown looks identical everywhere.** GitHub, Slack, and a given blogging platform each support slightly different *flavors* of Markdown — GitHub's, for instance, adds extras like tables and task lists on top of the common base covered here. Something that renders perfectly in one place isn't guaranteed to look identical in another.

---

## 6. Key Takeaways

[ [Top](#markdown) | [Home](../../README.md#first-friday) ]

- Markdown is plain text with a small set of symbols added; a Markdown processor converts that source into HTML, which a browser (or viewer) then actually displays.
- Markdown's source is designed to be readable even before it's rendered — that's the whole point of the format.
- The seven features covered here — headings (`#`), bold/italic (`**`/`*`), lists (`-`/`1.`), links (`[text](url)`), images (`![alt](path)`), code (`` ` `` and ` ``` `), and blockquotes (`>`) — cover the large majority of everyday Markdown writing.
- Every one of those seven maps to a specific, predictable HTML tag: `<h1>`–`<h6>`, `<strong>`/`<em>`, `<ul>`/`<ol>`/`<li>`, `<a>`, `<img>`, `<code>`/`<pre>`, and `<blockquote>`.
- This document — and every other whitepaper in this collection — is itself an example of all seven features in real use.

---

*Zip Code Wilmington — Markdown: What It Is and Why It Matters*

[ [Top](#markdown) | [Home](../../README.md#first-friday) ]
