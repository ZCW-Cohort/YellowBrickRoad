# Homebrew

[ [Home](../../README.md#first-friday) ]

**What It Is, and Why It Matters to a Beginner Programmer**
*Zip Code Wilmington*

---

## About This Document <!-- omit from toc -->

[ [Top](#homebrew) | [Home](../../README.md#first-friday) ]

This is part of Zip Code Wilmington's series of short, language-agnostic "concept" whitepapers. *Terminal and Shell* and *Essential Shell Commands* gave you the tools to move around your machine and manage files from the command line. This one covers the tool most Mac (and increasingly Linux) developers add almost immediately after that: **Homebrew**, the package manager that installs everything else. As a running example, this document installs and uses a real tool from start to finish — **HTTPie**, a friendlier command-line way to make HTTP requests.

---

## Table of Contents <!-- omit from toc -->

[ [Top](#homebrew) | [Home](../../README.md#first-friday) ]

- [Homebrew](#homebrew)
  - [1. What Is Homebrew?](#1-what-is-homebrew)
  - [2. Why It Matters to a Beginner Programmer](#2-why-it-matters-to-a-beginner-programmer)
  - [3. Core Vocabulary](#3-core-vocabulary)
  - [4. Installing Homebrew Itself](#4-installing-homebrew-itself)
  - [5. Installing a Real Tool: HTTPie](#5-installing-a-real-tool-httpie)
  - [6. Everyday Homebrew Commands](#6-everyday-homebrew-commands)
  - [7. Casks: Installing Full Applications](#7-casks-installing-full-applications)
  - [8. Common Beginner Mistakes](#8-common-beginner-mistakes)
  - [9. Key Takeaways](#9-key-takeaways)

---

## 1. What Is Homebrew?

[ [Top](#homebrew) | [Home](../../README.md#first-friday) ]

**Homebrew** is a **package manager**: a tool that installs, updates, and removes software from the command line, automatically handling anything else that software needs to actually work. Instead of finding an installer on a website, downloading it, opening it, and dragging an icon somewhere, you run one line in your terminal:

```bash
brew install wget
```

and a few seconds later, `wget` is installed, fully working, and immediately usable — no separate download page, no unzipping, no deciding where the files should live.

A **package** in this context means a named, versioned piece of software, bundled together with a clear recipe for building and installing it correctly. Homebrew's real job is managing all of that on your behalf: finding the right version, pulling in anything else it depends on, and putting every file exactly where it needs to go.

---

## 2. Why It Matters to a Beginner Programmer

[ [Top](#homebrew) | [Home](../../README.md#first-friday) ]

- **macOS doesn't ship with a package manager of its own.** Most Linux distributions come with one built in (`apt`, `dnf`, `pacman`); macOS doesn't, and Homebrew has become the de facto standard that fills that gap.
- **Nearly every setup guide assumes you already have it.** "Just run `brew install` ___" is the near-universal first step in developer tool documentation written for Mac users.
- **It resolves dependencies for you.** A tool that needs three other libraries to function gets all three installed automatically and correctly — you never have to hunt them down yourself.
- **It keeps your whole toolchain current with one command.** `brew upgrade` updates everything Homebrew manages at once, rather than you needing to remember how — or whether — you installed each individual thing.
- **It's not just a Mac thing anymore.** Homebrew also runs on Linux, with the exact same commands and the exact same experience — one set of habits that travels with you across machines.

---

## 3. Core Vocabulary

[ [Top](#homebrew) | [Home](../../README.md#first-friday) ]

| Term | Meaning |
|---|---|
| **Package manager** | A tool that installs, updates, and removes software, resolving dependencies automatically |
| **Formula** | Homebrew's term for the "recipe" describing how to install one particular package |
| **Cask** | A formula for installing a full graphical macOS application, rather than a command-line tool |
| **Tap** | An additional source of formulae, beyond Homebrew's own default collection |
| **Dependency** | Another package that a given package needs installed in order to actually work |
| **Bottle** | A precompiled, ready-to-install version of a formula, so most installs skip building from source entirely |

---

## 4. Installing Homebrew Itself

[ [Top](#homebrew) | [Home](../../README.md#first-friday) ]

Homebrew installs with a single, official bootstrap command, run once per machine:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

This downloads Homebrew's own install script and runs it, which sets up `brew` itself in a standard location — `/opt/homebrew` on an Apple Silicon Mac, `/usr/local` on an older Intel Mac, or `/home/linuxbrew/.linuxbrew` on Linux. At the end, it prints instructions to add that location to your `PATH`, the environment variable that tells your shell where to look for commands. Until that step is done, your shell has no way to find `brew` itself, let alone anything installed through it.

---

## 5. Installing a Real Tool: HTTPie

[ [Top](#homebrew) | [Home](../../README.md#first-friday) ]

With Homebrew set up, installing something real is exactly the one-liner from Section 1:

```bash
brew install httpie
```

Homebrew looks up the `httpie` formula, works out what it depends on, downloads a precompiled bottle for your system, and installs it — one command, no separate steps. **HTTPie** is a command-line tool for making HTTP requests, built specifically to be easier to read than raw `curl` output. Making the same kind of request covered elsewhere in this series:

```bash
http GET https://api.github.com/users/octocat
```

HTTPie prints the response with readable, colorized formatting by default — headers clearly separated from the body, JSON automatically indented — without needing any extra flags. It isn't a replacement for `curl -v`'s raw, unfiltered view of exactly what went over the wire; it's a friendlier everyday tool for the common case of just wanting to *read* a response comfortably.

---

## 6. Everyday Homebrew Commands

[ [Top](#homebrew) | [Home](../../README.md#first-friday) ]

| Command | What it does |
|---|---|
| `brew install <name>` | Installs a package |
| `brew uninstall <name>` | Removes a package |
| `brew upgrade` | Upgrades every installed package to its latest version |
| `brew upgrade <name>` | Upgrades just one specific package |
| `brew list` | Lists everything currently installed |
| `brew search <name>` | Searches for a package by name |
| `brew info <name>` | Shows details about a package before installing it |
| `brew doctor` | Checks your Homebrew setup for common problems |

`brew search` and `brew info` are worth using *before* an install, not just when something goes wrong — they're the fastest way to confirm a package actually exists, and what it will bring with it, before committing to installing it.

---

## 7. Casks: Installing Full Applications

[ [Top](#homebrew) | [Home](../../README.md#first-friday) ]

Everything so far has installed a command-line tool. Homebrew can also install full graphical applications, through a **cask** — the same idea as a formula, just for something with a windowed interface rather than a terminal command:

```bash
brew install --cask visual-studio-code
```

This downloads and installs the full VS Code application into your normal Applications folder, exactly as if you'd downloaded it from its website by hand — just started from the same terminal command you already know. The `--cask` flag is what tells Homebrew you're asking for an application, not a command-line formula; leaving it off when you mean a cask (or including it when you mean a formula) is a common early mix-up.

---

## 8. Common Beginner Mistakes

[ [Top](#homebrew) | [Home](../../README.md#first-friday) ]

> **Forgetting to add Homebrew to your `PATH` after installing it.** The install script tells you exactly what line to add and to which file — skip that step, and the `brew` command (and everything you install with it) simply won't be found afterward.

> **Running `brew` with `sudo`.** Homebrew is deliberately designed to install into locations your own user already owns, with no elevated privileges required. Forcing it with `sudo` doesn't fix a permissions problem — it usually causes new ones, by handing some of Homebrew's files to the wrong user.

> **Confusing a formula and a cask.** Trying to `brew install` a full graphical application without `--cask` will either fail outright or quietly grab the wrong thing — check `brew search` first if you're not sure which one something is.

> **Letting `brew upgrade` pile up unrun for months.** Nothing forces you to update — but the longer you wait, the more there is to update at once, and the more likely something has changed enough to need a little attention.

> **Ignoring what `brew doctor` actually says.** It's built to name specific, fixable problems with your setup — read its output literally rather than skipping past it when something Homebrew-related isn't working.

---

## 9. Key Takeaways

[ [Top](#homebrew) | [Home](../../README.md#first-friday) ]

- Homebrew is a package manager — it installs, updates, and removes command-line tools (and, via casks, full applications) with one command, resolving dependencies automatically.
- macOS has no package manager built in; Homebrew has become the standard one nearly every Mac-focused tutorial assumes you already have, and it runs on Linux too.
- A **formula** is a recipe for one command-line package; a **cask** is the same idea for a full graphical application.
- After installing Homebrew itself, its location has to be added to your `PATH` before `brew` (or anything it installs) can actually be found.
- `brew install`, `brew uninstall`, `brew upgrade`, `brew list`, `brew search`, and `brew info` cover the vast majority of everyday use.
- Never run Homebrew with `sudo` — it's built to work entirely within your own user account.

---

*Zip Code Wilmington — Homebrew: What It Is and Why It Matters*

[ [Top](#homebrew) | [Home](../../README.md#first-friday) ]
