# Essential Shell Commands

[ [Home](../README.md#3-terminal--shell) ]

**What They Are, and Why They Matter to a Beginner Programmer**
*Zip Code Wilmington*

---

## About This Document <!-- omit from toc -->

[ [Top](#essential-shell-commands) | [Home](../README.md#3-terminal--shell) ]

This is the third in Zip Code Wilmington's series of short, language-agnostic "concept" whitepapers, and it builds directly on the first two: *Filesystems* explained the tree of files and folders your computer organizes everything into, and *Terminal and Shell* explained the window-and-interpreter pair you use to talk to it. This one is the payoff — the small set of commands you'll actually type into that shell, over and over, to move around that tree and get real work done in it.

There's no cleverness to memorize here, just a short list of verbs worth knowing cold.

---

## Table of Contents <!-- omit from toc -->

[ [Top](#essential-shell-commands) | [Home](../README.md#3-terminal--shell) ]

- [Essential Shell Commands](#essential-shell-commands)
  - [1. Why So Few Commands Get You So Far](#1-why-so-few-commands-get-you-so-far)
  - [2. Why It Matters to a Beginner Programmer](#2-why-it-matters-to-a-beginner-programmer)
  - [3. Finding and Moving: pwd, ls, and cd](#3-finding-and-moving-pwd-ls-and-cd)
    - [`pwd` — "print working directory"](#pwd--print-working-directory)
    - [`ls` — "list"](#ls--list)
    - [`cd` — "change directory"](#cd--change-directory)
    - [`find` - "find  **PRO TIP**"](#find---find--pro-tip)
      - [What's it doing?](#whats-it-doing)
      - [How to use it](#how-to-use-it)
      - [Too Noisy?](#too-noisy)
  - [4. Building and Inspecting: mkdir, touch, cat, and echo](#4-building-and-inspecting-mkdir-touch-cat-and-echo)
    - [`mkdir` — "make directory"](#mkdir--make-directory)
    - [`touch`](#touch)
    - [`cat` — "concatenate"](#cat--concatenate)
    - [`echo`](#echo)
  - [5. Copying, Moving, and Deleting: cp, mv, and rm](#5-copying-moving-and-deleting-cp-mv-and-rm)
    - [`cp` — "copy"](#cp--copy)
    - [`mv` — "move"](#mv--move)
    - [`rm` — "remove"](#rm--remove)
  - [6. The Recursive Flag: -r Means the Same Thing Everywhere](#6-the-recursive-flag--r-means-the-same-thing-everywhere)
  - [7. Common Beginner Mistakes](#7-common-beginner-mistakes)
  - [8. Key Takeaways](#8-key-takeaways)

---

## 1. Why So Few Commands Get You So Far

[ [Top](#essential-shell-commands) | [Home](../README.md#3-terminal--shell) ]

The shell has hundreds of available programs on any given machine, but almost all of your day-to-day movement through the filesystem comes down to fewer than ten of them. That's not a coincidence — these commands were designed to each do exactly one small thing (find out where you are, list what's here, go somewhere else, make a file, copy it, delete it) and nothing more. Because they're so narrow, they're also easy to combine, easy to remember, and easy to type without thinking — which is exactly the point. You want navigating the filesystem to require as little conscious effort as possible, so the effort you do have goes toward the actual problem you're solving.

## 2. Why It Matters to a Beginner Programmer

[ [Top](#essential-shell-commands) | [Home](../README.md#3-terminal--shell) ]

Every one of these commands is doing, by hand, the exact same thing your code, your editor, and your tools are constantly doing automatically underneath: checking where a file is, creating one, reading one, getting rid of one. Typing them yourself first is what makes all of that later machinery make sense instead of feeling like magic.

- **You will type these constantly.** Setting up a new project, checking whether a file actually saved where you think it did, cleaning up a mess — this handful of commands covers nearly all of it.
- **They're the foundation everything else assumes.** Git commands, build tools, and install scripts all operate relative to "wherever you currently are" in the filesystem — the same working directory `pwd` and `cd` control directly.
- **They turn into scripts.** A sequence of these commands, typed once to solve a problem, is also a sequence you can save and re-run automatically — the first real step toward automation.

## 3. Finding and Moving: pwd, ls, and cd

[ [Top](#essential-shell-commands) | [Home](../README.md#3-terminal--shell) ]

### `pwd` — "print working directory"

[ [Top](#essential-shell-commands) | [Back](#3-finding-and-moving-pwd-ls-and-cd) | [Home](../README.md#3-terminal--shell) ]

Prints the absolute path of wherever the shell currently considers "here":

```bash
$ pwd
/Users/kris/projects/zcw-notes
```

When you're not sure where you are, `pwd` is always the first thing to run.

### `ls` — "list"

[ [Top](#essential-shell-commands) | [Back](#3-finding-and-moving-pwd-ls-and-cd) | [Home](../README.md#3-terminal--shell) ]

Lists what's inside a directory — by default, the working directory:

```bash
$ ls
notes.txt  src  README.md
```

Two flags you'll use immediately: `-l` for a detailed, one-entry-per-line listing (permissions, size, last modified date), and `-a` to also show hidden files — anything starting with a `.`, which `ls` hides by default. Combined, `ls -la` is probably the single most-typed command in this whole document.

### `cd` — "change directory"

[ [Top](#essential-shell-commands) | [Back](#3-finding-and-moving-pwd-ls-and-cd) | [Home](../README.md#3-terminal--shell) ]

Moves the shell's working directory:

```bash
cd src      # relative — move into "src", inside the folder you're already in
cd /etc     # absolute — jump straight there, no matter where you started
```

Every directory contains two special entries: `.` refers to the directory itself, and `..` refers to its parent. `cd ..` moves up one level, and it chains: `cd ../..` moves up two.

`~` is shorthand the shell expands to your **home directory** — your own personal folder (`/Users/kris` on macOS, `/home/kris` on Linux). `cd ~`, or just `cd` with no argument at all, takes you home from anywhere; `~/Documents` always means "the Documents folder inside my home directory," regardless of where you currently are.

One more worth knowing on purpose: `cd -` jumps back to whichever directory you were in immediately before your last `cd` — and running it again toggles you right back. It's a small thing, but genuinely useful once you're bouncing between two folders repeatedly.

As covered in *Filesystems*: `pwd` always prints an absolute path, but the argument you hand `cd` can be either kind — absolute or relative — and a relative one is resolved against wherever you currently are.

### `find` - "find  **PRO TIP**"

[ [Top](#essential-shell-commands) | [Back](#3-finding-and-moving-pwd-ls-and-cd) | [Home](../README.md#3-terminal--shell) ]

This specific invocation is Paul's favorite shell command. It's useful for quickly traversing a folder structure, like a repo, to look for files that contain a specific bit of text.

```bash
find . -type f -name "*.py" -exec grep -iEn "^some_string.*$" {} /dev/null \;
```

#### What's it doing?

[ [Top](#essential-shell-commands) | [Back](#find---find--pro-tip) | [Home](../README.md#3-terminal--shell) ]

- `find` - This is the Unix `find` command. It can locate files, directories or devices based on a large number of specifications.
  - `.` - This says "start in the current directory". If you replace this with a specific or relative directory path, it will start there instead.
  - `-type f` - Let's only look at regular files, excludes directories, devices, etc. We could still get unreadable binary files so we need more.
  - `-name "*.py"` - This is more! It refines our search to just Python files. Change this to look at any specific file based on its name.
  - `-exec ...` - This runs whatever command follows it on EVERY item that `find` locates.
    - `grep` - This is the Unix `grep` command. It can locate all occurrences of a string in a file.
      - `-iEn` - These are options for `grep`: `-i` ignore case, `-E` allow regular expressions in search string, `-n` print line numbers of matches
      - `"^some_string.*"` - A regular expression search string that looks for `some_string` at the start of a line, followed by 0 or more characters.
      - `{}` - This is where the file name from `find` gets inserted into the `grep` command.
      - `/dev/null` – This is the `bit bucket`. We include this so that `grep` thinks there are multiple files and will print the file names
      - `\;` - This is needed to terminate the end of the command for `-exec`.

#### How to use it

[ [Top](#essential-shell-commands) | [Back](#find---find--pro-tip) | [Home](../README.md#3-terminal--shell) ]

Change the `*.py` to look for any sort of files you want, either by base name or extension. Want Jupyter notebook files? "*.ipynb". Change the quoted string in the `grep` command to look for different strings. For example, `"^class \b[A-Z][a-zA-Z0-9]*\b"` will find all the classes in your python files.

#### Too Noisy?

If you get back alot of "Permission Denied" or similar errors, those can drown out the useful output. To reduce the noise, try piping the command through another `grep`, but this one uses `-v` to ignore the errors. Note the `2>&1` on the `find` command. This redirects the errors to `stdout`, allowing `grep` to see them as well as the output we want to keep.

```bash
find . -type f -name "*.py" -exec grep -iEn "^some_string.*$" {} /dev/null \; 2>&1 | grep -v "Permission denied"
```

## 4. Building and Inspecting: mkdir, touch, cat, and echo

[ [Top](#essential-shell-commands) | [Home](../README.md#3-terminal--shell) ]

### `mkdir` — "make directory"

[ [Top](#essential-shell-commands) | [Back](#4-building-and-inspecting-mkdir-touch-cat-and-echo) | [Home](../README.md#3-terminal--shell) ]

Creates a new, empty folder:

```bash
mkdir notes
```

Plain `mkdir` fails if any of the parent folders in the path don't exist yet. `mkdir -p` creates every missing folder along the way in one shot, and — usefully — doesn't complain if the target already exists:

```bash
mkdir -p projects/2026/january
```

### `touch`

[ [Top](#essential-shell-commands) | [Back](#4-building-and-inspecting-mkdir-touch-cat-and-echo) | [Home](../README.md#3-terminal--shell) ]

Creates an empty file if it doesn't exist yet — or, if it already does, just updates its "last modified" timestamp without touching the contents at all:

```bash
touch notes.txt
```

Worth stating plainly: `touch` does not put anything *inside* the file. It gives you an empty file, full stop — nothing more.

### `cat` — "concatenate"

[ [Top](#essential-shell-commands) | [Back](#4-building-and-inspecting-mkdir-touch-cat-and-echo) | [Home](../README.md#3-terminal--shell) ]

Prints a file's contents straight to the terminal — the fastest way to peek inside a file without opening an editor:

```bash
cat notes.txt
```

Its name comes from its other job: stringing several files together into one stream of output — `cat part1.txt part2.txt` prints both, back to back, as if they were a single file.

### `echo`

[ [Top](#essential-shell-commands) | [Back](#4-building-and-inspecting-mkdir-touch-cat-and-echo) | [Home](../README.md#3-terminal--shell) ]

Prints back whatever text you give it. On its own that looks trivial, but paired with the redirection covered in *Terminal and Shell*, it becomes the fastest way to create a file with real content — no editor required:

```bash
echo "Hello, Zip Code!" > greeting.txt
cat greeting.txt
# Hello, Zip Code!
```

## 5. Copying, Moving, and Deleting: cp, mv, and rm

[ [Top](#essential-shell-commands) | [Home](../README.md#3-terminal--shell) ]

### `cp` — "copy"

[ [Top](#essential-shell-commands) | [Back](#5-copying-moving-and-deleting-cp-mv-and-rm) | [Home](../README.md#3-terminal--shell) ]

Duplicates a file, leaving the original in place:

```bash
cp notes.txt notes-backup.txt
```

### `mv` — "move"

[ [Top](#essential-shell-commands) | [Back](#5-copying-moving-and-deleting-cp-mv-and-rm) | [Home](../README.md#3-terminal--shell) ]

Relocates a file — or renames it. Worth saying explicitly, because it's a genuinely useful insight: in a filesystem, *renaming* and *moving* are the same operation. Renaming a file is just moving it to a new name inside the same folder:

```bash
mv draft.txt final.txt      # renaming — same folder, new name
mv final.txt archive/       # moving — same name, new folder
```

### `rm` — "remove"

[ [Top](#essential-shell-commands) | [Back](#5-copying-moving-and-deleting-cp-mv-and-rm) | [Home](../README.md#3-terminal--shell) ]

Deletes a file. Unlike dragging a file to the Trash or Recycle Bin, there is no confirmation dialog, no holding area, and no undo:

```bash
rm old-notes.txt
```

> This is the single most important habit in this entire document: **`rm` is forever.** Before running it — especially with a wildcard, and doubly especially with `-r`, next — it's worth a second look at exactly what you're about to type.

## 6. The Recursive Flag: -r Means the Same Thing Everywhere

[ [Top](#essential-shell-commands) | [Home](../README.md#3-terminal--shell) ]

`cp` and `rm` (among plenty of other commands) only act on one file at a time by default — pointing either one at a folder, with nothing extra, just gives you an error. The `-r` flag stands for **recursive**, and it means the exact same thing no matter which command it's attached to: *"don't stop at this one thing — go all the way down the tree, into everything inside it, and everything inside that."*

```bash
cp -r src backup-of-src   # copy an entire folder, and everything inside it
rm -r old-project          # delete an entire folder, and everything inside it
```

`rm -rf` adds `-f` ("force") on top of that, which skips confirmation prompts and pushes through errors that would otherwise stop it. That combination — *delete*, *go all the way down the tree*, *don't ask first* — packed into four characters, is the single most dangerous ordinary thing you'll type as a beginner. It has real, legitimate uses. It also deserves a genuine second look, every single time, before you press Enter.

## 7. Common Beginner Mistakes

[ [Top](#essential-shell-commands) | [Home](../README.md#3-terminal--shell) ]

> **Assuming `rm` has an undo.** It doesn't. There's no Trash to fish a file back out of — see Section 5.

> **Running `mkdir` on a path whose parent folders don't exist yet**, and getting stuck on a "No such file or directory" error. The fix is `mkdir -p`.

> **Expecting `touch` to create a file that already has something in it.** It only creates an empty file, or bumps a timestamp on an existing one — never content.

> **Forgetting that a single `>` overwrites a whole file**, while `>>` appends to the end of it. Using the wrong one with `echo` (or any other redirected command) can silently erase something you meant to keep.

> **Running `cp`, `mv`, or `rm` with a relative path without checking `pwd` first**, and acting on the wrong file entirely because the working directory wasn't what you assumed.

> **Letting a wildcard expand into more than you meant**, especially in front of `rm -r`. It's worth running `ls` on the same pattern first, to see exactly what will match, before you let `rm` anywhere near it.

## 8. Key Takeaways

[ [Top](#essential-shell-commands) | [Home](../README.md#3-terminal--shell) ]

- `pwd` tells you where you are; `ls` tells you what's there; `cd` moves you — and together, they're most of what "navigating the filesystem" actually means.
- `~` means your home directory, `..` means the parent of wherever you are, and `cd -` jumps back to your previous location — three small shortcuts you'll use constantly.
- `mkdir -p` builds nested folders in one step; `touch` creates an empty file (or just updates its timestamp); `cat` and `echo` let you inspect and create simple files with no editor at all.
- `cp` copies, `mv` moves *or* renames (the same operation either way), and `rm` deletes — permanently.
- `-r` always means "go all the way down the tree," on any command that supports it — it's one idea, not a separate thing to memorize per command.

Put simply: `pwd`, `ls`, and `cd` are how you find your place in the tree and move around it, using either an absolute path from the root or a relative path from wherever you're currently standing. `mkdir`, `mkdir -p`, `cp`, `mv`, `rm`, `touch`, and `cat` let you build, copy, rename, delete, and inspect files with no editor at all. `-r` means the exact same thing — "go all the way down the tree" — wherever it shows up. And `rm` deletes for good, no undo: the one habit worth keeping more than any other from today. A small number of commands, each one you'll type many times.

---

*Zip Code Wilmington — Essential Shell Commands: What They Are and Why They Matter*

[ [Top](#essential-shell-commands) | [Home](../README.md#3-terminal--shell) ]
