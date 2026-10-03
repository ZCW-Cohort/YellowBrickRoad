# Environment Variables

[ [Home](../README.md#3-terminal--shell) ]

**What They Are, and Why They Matter to a Beginner Programmer**
*Zip Code Wilmington*

---

## About This Document <!-- omit from toc -->

[ [Top](#environment-variables) | [Home](../README.md#3-terminal--shell) ]

This is the eighth in Zip Code Wilmington's series of short, language-agnostic "concept" whitepapers. *Terminal and Shell* introduced `PATH` — the one environment variable that solves the mystery of "command not found." This document generalizes that idea: `PATH` isn't special, it's just one example of a much broader, extremely common pattern for configuring programs without touching their code.

---

## Table of Contents <!-- omit from toc -->

[ [Top](#environment-variables) | [Home](../README.md#3-terminal--shell) ]

- [Environment Variables](#environment-variables)
  - [1. What Is an Environment Variable?](#1-what-is-an-environment-variable)
  - [2. Why It Matters to a Beginner Programmer](#2-why-it-matters-to-a-beginner-programmer)
  - [3. Core Vocabulary](#3-core-vocabulary)
  - [4. Shell Variables vs. Environment Variables](#4-shell-variables-vs-environment-variables)
  - [5. Reading and Setting Environment Variables](#5-reading-and-setting-environment-variables)
  - [6. Common Beginner Mistakes](#6-common-beginner-mistakes)
  - [7. Key Takeaways](#7-key-takeaways)

---

## 1. What Is an Environment Variable?

[ [Top](#environment-variables) | [Home](../README.md#3-terminal--shell) ]

An **environment variable** is a named value that lives outside any one program's own code, made available to that program — and to any program it goes on to launch — by whatever started it. Think of it like a note posted on a shared bulletin board rather than something written on one specific desk: any process that walks by can read it, instead of it belonging privately to a single piece of code.

Every running program (a **process**) is handed a full set of these name/value pairs the moment it starts, inherited from whatever launched it. Your shell has its own environment; when you run a command, that new process is handed a copy of the shell's environment to start with. This is exactly how `PATH`, from *Terminal and Shell*, actually reaches the shell in the first place — it isn't hardcoded into `bash` or `zsh`, it's an environment variable the shell reads like any other, and it's why every program you run can rely on the same `PATH` the shell itself is using.

---

## 2. Why It Matters to a Beginner Programmer

[ [Top](#environment-variables) | [Home](../README.md#3-terminal--shell) ]

- **It's the standard way to configure a program without touching its code.** Whether a server listens on port `8080` or `3000`, whether an app talks to a production database or a test one — this is almost always controlled by an environment variable, not a line you'd have to edit and re-save inside the program itself.
- **Every language reads them the same basic way.** Python's `os.environ`, Go's `os.Getenv`, C's `getenv`, and equivalents in every other mainstream language all do the same job: read a value out of the process's environment. It's one of the few genuinely universal mechanisms across languages.
- **It's how secrets are supposed to be handled.** API keys, database passwords, and similar sensitive values belong in environment variables, read at runtime — never typed directly into your source code, where (as covered in *Git and Version Control*) they risk being committed and pushed somewhere permanent and public.
- **It's what lets the same code run in different places.** The same program can behave differently on your laptop, a teammate's laptop, and a production server, purely because each of those environments sets different values for the same variable names — with zero changes to the code itself.

---

## 3. Core Vocabulary

[ [Top](#environment-variables) | [Home](../README.md#3-terminal--shell) ]

| Term | Meaning |
|---|---|
| **Environment variable** | A named value available to a running process and to any processes it starts |
| **Process** | A single running instance of a program |
| **Shell variable** | A variable that exists only inside your current shell session — not automatically handed to programs it runs |
| **Exporting** | Marking a shell variable so that programs launched from the shell inherit it as an environment variable |
| **Inheriting** | The way a newly launched program automatically receives a copy of its parent's environment |
| **`PATH`** | The environment variable listing directories the shell searches to find a command (see *Terminal and Shell*) |
| **`.env` file** | A common convention: a plain text file of `key=value` pairs, loaded into a project's environment automatically by many tools |

---

## 4. Shell Variables vs. Environment Variables

[ [Top](#environment-variables) | [Home](../README.md#3-terminal--shell) ]

This is the single most important — and most commonly missed — distinction in this whole topic. Setting a plain variable in your shell does **not** automatically make it an environment variable:

```bash
NAME="Ada"
echo $NAME          # "Ada" — visible right here, in this shell
```

`NAME` exists, and this shell can see it, but it exists only in this shell's own private memory. Any *separate* program launched from here — even a brand-new shell — won't see it at all:

```bash
bash -c 'echo $NAME'   # prints nothing — the new process never received NAME
```

To make a variable part of the environment that gets handed down to every program you launch, you have to **export** it:

```bash
export NAME="Ada"
bash -c 'echo $NAME'   # now prints "Ada" — the child process inherited it
```

That one word, `export`, is the entire difference between "a value only I can see" and "a value every program I run from here can see." A Python, Go, or C program reading its environment for `NAME` will only find it if it was exported first — a plain shell variable is invisible to it, no matter how confidently you set it.

---

## 5. Reading and Setting Environment Variables

[ [Top](#environment-variables) | [Home](../README.md#3-terminal--shell) ]

```bash
echo $PATH           # print the value of one specific variable
printenv             # list every environment variable currently set
export API_KEY="abc123"   # set (and export) a new one for this session
```

- The `$` in front of a variable's name means "give me the *value* of this" — `echo PATH` would just print the literal word `PATH`, while `echo $PATH` prints its actual contents.
- `printenv` (or plain `env`) is the fastest way to see everything currently available, which is especially useful when debugging "why can't my program find this value?"
- A variable exported at the prompt only lasts for that one terminal session — close the window, and it's gone. To make one available every time you open a new shell, add its `export` line to your shell's startup file (`~/.bashrc` or `~/.zshrc`, from *Terminal and Shell*), so it's set automatically before you ever type a command.
- For project-specific values, the common modern convention is a **`.env` file** — a plain text file of `key=value` lines sitting in a project's folder, which many frameworks and libraries know how to load automatically, so you don't have to `export` a long list of variables by hand every time you start working.

---

## 6. Common Beginner Mistakes

[ [Top](#environment-variables) | [Home](../README.md#3-terminal--shell) ]

> **Setting a variable and forgetting to `export` it.** This is the single most common source of "my program can't see the value I *know* I set" confusion — see Section 4.

> **Hardcoding a secret directly into source code instead of an environment variable.** Beyond being bad practice on its own, this is exactly how API keys and passwords end up accidentally committed to a public repository — see *Git and Version Control*'s note on `.gitignore` and sensitive files.

> **Committing a `.env` file to version control.** Since `.env` files frequently hold real secrets, they almost always belong in `.gitignore`, not in the repository itself.

> **Assuming a variable set in one terminal window is available in another.** Each terminal window or tab is typically its own separate shell process with its own separate environment — a variable exported in one won't magically appear in another unless it's set in a startup file every new shell reads.

> **Forgetting that variable names are case-sensitive.** `PATH` and `path` are two entirely different variables on a Unix-like system — the same case-sensitivity rule covered for filenames in *Filesystems* applies here too.

> **Not quoting a variable that might contain spaces.** `cp $FILE backup/` can break in surprising ways if `$FILE` contains a space, because the shell splits unquoted values on whitespace. Wrapping it as `"$FILE"` avoids the problem.

---

## 7. Key Takeaways

[ [Top](#environment-variables) | [Home](../README.md#3-terminal--shell) ]

- An environment variable is a named value handed to a process (and everything it launches) by whatever started it — `PATH` is the most familiar example, but the pattern is completely general.
- A shell variable stays private to your current shell until you `export` it; only exported variables are inherited by programs you run from that shell.
- Every mainstream language reads environment variables the same basic way, which is exactly what makes them the standard tool for configuring a program's behavior without editing its code.
- Secrets — API keys, passwords, tokens — belong in environment variables (or a `.env` file kept out of version control), never typed directly into source code.
- `export` inside a session is temporary; put the `export` line in your shell's startup file to make it permanent across new terminal sessions.
- Variable names are case-sensitive, and an unquoted variable containing spaces can be split apart unexpectedly by the shell — two small habits worth building early.

---

*Zip Code Wilmington — Environment Variables: What They Are and Why They Matter*

[ [Top](#environment-variables) | [Home](../README.md#3-terminal--shell) ]
