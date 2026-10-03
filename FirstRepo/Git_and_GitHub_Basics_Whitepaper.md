# Git and GitHub Basics

[ [Home](../README.md#4-firstrepo) ]

**What They Are, and Why They Matter to a Beginner Programmer**
*Zip Code Wilmington*

---

## About This Document <!-- omit from toc -->

[ [Top](#git-and-github-basics) | [Home](../README.md#4-firstrepo) ]

This is part of Zip Code Wilmington's series of short, language-agnostic "concept" whitepapers, and it's paced for someone who has never used Git before. It covers exactly one workflow — the one you'll use on your very first day and on most solo projects after that: **fork** a project on GitHub, **clone** it to your laptop, **make a change**, then **add**, **commit**, and **push** that change back up.

There's a lot more to Git than this (branches, merging, working on a team). None of it is needed yet. Get these six steps comfortable first; everything else is built on top of them.

The running example is Zip Code Wilmington's `FirstRepo` lab, a tiny project with one Python file, `hello.py`.

---

## Table of Contents <!-- omit from toc -->

[ [Top](#git-and-github-basics) | [Home](../README.md#4-firstrepo) ]

- [Git and GitHub Basics](#git-and-github-basics)
  - [1. What Are Git and GitHub?](#1-what-are-git-and-github)
  - [2. Why It Matters to a Beginner Programmer](#2-why-it-matters-to-a-beginner-programmer)
  - [3. Core Vocabulary](#3-core-vocabulary)
    - [Add vs. commit: why two steps?](#add-vs-commit-why-two-steps)
  - [4. The Big Picture: Three Copies of One Project](#4-the-big-picture-three-copies-of-one-project)
  - [5. One-Time Setup](#5-one-time-setup)
  - [6. Step 1: Fork](#6-step-1-fork)
  - [7. Step 2: Clone](#7-step-2-clone)
  - [8. Step 3: Make a Change](#8-step-3-make-a-change)
  - [9. Step 4: Add](#9-step-4-add)
  - [10. Step 5: Commit](#10-step-5-commit)
    - [Writing a good commit message](#writing-a-good-commit-message)
  - [11. Step 6: Push](#11-step-6-push)
  - [12. The Everyday Loop](#12-the-everyday-loop)
  - [13. Common Beginner Mistakes](#13-common-beginner-mistakes)
  - [14. Key Takeaways](#14-key-takeaways)

---

## 1. What Are Git and GitHub?

[ [Top](#git-and-github-basics) | [Home](../README.md#4-firstrepo) ]

They're two different things with similar names, and keeping them apart makes everything else easier.

**Git** is a program on your laptop. It keeps a history of a project folder: every time you tell it to, it takes a snapshot of all the files, and it remembers every snapshot you've ever taken. You can look back at any of them later. You run Git by typing `git` commands in the terminal.

**GitHub** is a website (github.com). It stores copies of Git projects on the internet, so they're backed up, so other people can see them, and so you can get to them from any computer.

An analogy: Git is like the camera that takes the pictures. GitHub is like the online photo album where you upload them. You can use the camera without ever uploading anything — but in this course, you'll upload everything.

---

## 2. Why It Matters to a Beginner Programmer

[ [Top](#git-and-github-basics) | [Home](../README.md#4-firstrepo) ]

- **It's how you'll turn in your work.** Nearly every lab in this course starts with "fork and clone this repo" and ends with "push your changes." The steps in this document are the steps for handing in an assignment.
- **It's an undo button for your whole project.** Every commit is a saved point you can return to. Breaking something stops being scary when you know the last working version is one command away.
- **It's your backup.** Once your work is pushed to GitHub, a dead laptop doesn't lose it.
- **It's your portfolio.** Employers look at GitHub profiles. A steady trail of commits across real projects shows what you can do better than a résumé line can.
- **Every developer job uses it.** Git is the standard tool for tracking code across the entire industry. Learning it now isn't course busywork; it's day-one job skills.

---

## 3. Core Vocabulary

[ [Top](#git-and-github-basics) | [Home](../README.md#4-firstrepo) ]

| Term | Meaning |
|---|---|
| **Repository** (repo) | A project folder that Git is tracking, including its full history |
| **Fork** | Your own copy of someone else's repo, made *on GitHub*, under your account |
| **Clone** | A copy of a repo downloaded from GitHub onto *your laptop* |
| **Working directory** | The project folder on your laptop, where you actually edit files |
| **Staging** | Choosing which changes go into your next snapshot (done with `git add`) |
| **Commit** | A saved snapshot of your staged changes, with a short message describing them |
| **Commit message** | The one-line description you attach to a commit ("Add my name to hello.py") |
| **Remote** | A copy of the repo somewhere else — for you, the one on GitHub |
| **`origin`** | The name Git automatically gives the remote you cloned from |
| **Push** | Sending your new commits from your laptop up to GitHub |
| **`main`** | The name of the project's main line of history (its default *branch*) |

### Add vs. commit: why two steps?

[ [Top](#git-and-github-basics) | [Back](#3-core-vocabulary) | [Home](../README.md#4-firstrepo) ]

This trips up nearly everyone at first. Why not just "save to Git" in one step?

Think of packing a box to mail. `git add` is putting items *into* the box. `git commit` is taping it shut and writing a label on it. You might change five files but only want to put three of them in this box — the add step lets you choose. On a small solo project you'll usually add everything, but the two steps are still there, and Git will remind you if you forget one.

---

## 4. The Big Picture: Three Copies of One Project

[ [Top](#git-and-github-basics) | [Home](../README.md#4-firstrepo) ]

When you work on a lab, the same project exists in three places:

```text
   ZCW-Cohort/FirstRepo          ← the original (on GitHub, belongs to Zip Code)
           │
           │  1. fork  (on the GitHub website)
           ▼
   your-username/FirstRepo       ← your fork (on GitHub, belongs to you)
           │          ▲
  2. clone │          │ 6. push
           ▼          │
   ~/Projects/FirstRepo          ← your clone (on your laptop)
           │
           │  3. edit  →  4. add  →  5. commit
           └──────────────────────────────────
```

- You **fork** once, on the website, to get your own copy on GitHub.
- You **clone** once, in the terminal, to get that copy onto your laptop.
- Then, as many times as you like: **edit**, **add**, **commit**, **push**.

Notice that you never push to the original. You can't — it belongs to Zip Code. You push to *your fork*, and that's where your instructors look at your work.

---

## 5. One-Time Setup

[ [Top](#git-and-github-basics) | [Home](../README.md#4-firstrepo) ]

Do these once per laptop, not once per project.

**Tell Git who you are.** Every commit is labeled with a name and email. Use the same email as your GitHub account:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

**Let your laptop log in to GitHub.** GitHub doesn't accept your account password from the terminal. The simplest way to set this up is GitHub's own command-line tool:

```bash
brew install gh
gh auth login
```

Answer its questions (GitHub.com, HTTPS, log in with a web browser), and from then on `git push` just works.

**Have a place for your projects.** Keep all your code in one folder:

```bash
mkdir ~/Projects
```

---

## 6. Step 1: Fork

[ [Top](#git-and-github-basics) | [Home](../README.md#4-firstrepo) ]

*Where:* the GitHub website. *How often:* once per project.

1. Go to `https://github.com/ZCW-Cohort/FirstRepo`.
2. Click the **Fork** button near the top right.
3. Click **Create fork**.

GitHub takes you to `https://github.com/your-username/FirstRepo` — your copy. Check the top left of the page: it should show *your* username, with a small note underneath saying "forked from ZCW-Cohort/FirstRepo."

Nothing is on your laptop yet. A fork only lives on GitHub.

---

## 7. Step 2: Clone

[ [Top](#git-and-github-basics) | [Home](../README.md#4-firstrepo) ]

*Where:* the terminal. *How often:* once per project.

On **your fork's** page, click the green **Code** button and copy the HTTPS URL. It should have your username in it. Then:

```bash
cd ~/Projects
git clone https://github.com/your-username/FirstRepo
cd FirstRepo
```

`git clone` downloads the whole project, history and all, into a new `FirstRepo` folder. The `cd FirstRepo` matters: Git commands only work when you're *inside* the project folder.

Take a look around:

```bash
ls
# README.md  hello.py
```

---

## 8. Step 3: Make a Change

[ [Top](#git-and-github-basics) | [Home](../README.md#4-firstrepo) ]

*Where:* your editor. *How often:* as often as you like.

Open `hello.py`:

```python
# hello.py
# A very simple Python program that says hello to someone.
#
# YOUR FIRST CHANGE: replace "World" below with your own name
# (keep the quote marks!), save the file, and run the program again.

name = "World"

print("Hello, " + name + "!")
```

Change `"World"` to your own name, save the file, and run it to make sure it works:

```bash
python3 hello.py
# Hello, Kris!
```

Now ask Git what it thinks happened. **`git status` is the most important command in this document** — run it before every add, every commit, and every push, and read what it says:

```bash
git status
```

```text
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   hello.py

no changes added to commit (use "git add" and/or "git commit -a")
```

Git noticed that `hello.py` changed, and it's telling you that change isn't in a box yet ("not staged"). Notice that it even tells you the next command to run.

---

## 9. Step 4: Add

[ [Top](#git-and-github-basics) | [Home](../README.md#4-firstrepo) ]

*Where:* the terminal. *How often:* every time you're ready to save a snapshot.

Put the change in the box:

```bash
git add hello.py
```

Or, to add *every* changed file in the project at once:

```bash
git add .
```

(The `.` means "this folder and everything in it.") Check again:

```bash
git status
```

```text
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   hello.py
```

"Changes to be committed" means the change is staged — it's in the box, waiting to be sealed.

---

## 10. Step 5: Commit

[ [Top](#git-and-github-basics) | [Home](../README.md#4-firstrepo) ]

*Where:* the terminal. *How often:* every time you finish a small, meaningful piece of work.

Seal the box and label it:

```bash
git commit -m "Add my name to hello.py"
```

```
[main d3f302c] Add my name to hello.py
 1 file changed, 1 insertion(+), 1 deletion(-)
```

The `-m` is for *message*. `d3f302c` is the commit's short ID; yours will be different. Git has now saved a permanent snapshot — **on your laptop**. Check:

```bash
git status
```

```text
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
```

Read that carefully. "Working tree clean" means everything is committed. But "ahead of 'origin/main' by 1 commit" means GitHub doesn't have it yet. A commit is saved, but it isn't shared or backed up until you push.

### Writing a good commit message

[ [Top](#git-and-github-basics) | [Back](#10-step-5-commit) | [Home](../README.md#4-firstrepo) ]

A commit message should say *what this change does*, in a few words, as if finishing the sentence "This commit will…":

- Good: `Add my name to hello.py`, `Fix typo in README`, `Add test for empty input`
- Not helpful: `stuff`, `changes`, `asdf`, `final`, `final2`

---

## 11. Step 6: Push

[ [Top](#git-and-github-basics) | [Home](../README.md#4-firstrepo) ]

*Where:* the terminal. *How often:* whenever you want GitHub to have your latest commits — at least at the end of every work session.

```bash
git push
```

```text
To https://github.com/your-username/FirstRepo.git
   df230ef..d3f302c  main -> main
```

Your commit is now on GitHub. **Go check** — this is the step beginners skip:

1. Open `https://github.com/your-username/FirstRepo` in your browser.
2. Near the top, you should see your commit message, "Add my name to hello.py."
3. Click `hello.py` and confirm your name is there.

If you can see it on GitHub, your instructors can see it too. That's what "turned in" means.

---

## 12. The Everyday Loop

[ [Top](#git-and-github-basics) | [Home](../README.md#4-firstrepo) ]

Fork and clone happen once. After that, working on a project by yourself is the same four commands, over and over:

```bash
git status                      # what changed?
git add .                       # put the changes in the box
git commit -m "Describe it"     # seal and label the box
git push                        # send it to GitHub
```

Zip Code calls `add`, `commit`, and `push` **the 'holy' Triad**, with `status` as the habit wrapped around all three. Do it every time you get something working — not once at the end of the week. Small, frequent commits mean small, easy-to-understand saved points, and a lost laptop costs you an hour of work instead of a week.

| Step | Command | Where it happens | How often |
|---|---|---|---|
| Fork | *Fork* button | GitHub website | Once per project |
| Clone | `git clone <your fork's URL>` | Terminal | Once per project |
| Check | `git status` | Terminal | Constantly |
| Add | `git add .` | Terminal | Every snapshot |
| Commit | `git commit -m "..."` | Terminal | Every snapshot |
| Push | `git push` | Terminal | At least every work session |

---

## 13. Common Beginner Mistakes

[ [Top](#git-and-github-basics) | [Home](../README.md#4-firstrepo) ]

> **Cloning the original instead of your fork.** If the URL you cloned says `ZCW-Cohort` instead of your username, `git push` will fail with a permission error, because you're trying to push to a repo you don't own. Check the URL before you clone. (Already did it? `git remote -v` shows where you cloned from. The easy fix is to move the folder aside, clone your fork, and copy your changed files over.)

> **Running Git commands in the wrong folder.** `fatal: not a git repository` means you're not inside the project. `cd` into the project folder and try again. `pwd` tells you where you are.

> **Cloning a project inside another project.** Always `cd ~/Projects` before `git clone`, so each project gets its own folder side by side — not nested inside the last one.

> **Forgetting `git add`.** You commit, and Git says "no changes added to commit." The commit step only saves what's been added. Add first, then commit.

> **Thinking "committed" means "turned in."** A commit lives only on your laptop until you push. If `git status` says "ahead of 'origin/main'," GitHub doesn't have your work yet.

> **Never checking GitHub after pushing.** The push looked fine in the terminal, but did it land where you think? Thirty seconds in the browser answers that for sure.

> **Committing once, at the very end.** One giant commit called "done" is hard to understand and gives you no saved points to go back to. Commit each time a small piece works.

> **Getting stuck in a strange editor after `git commit`.** If you forget the `-m "message"`, Git opens a text editor and waits for you to type a message. If it's vim, press `Esc`, type `:q!`, and press `Enter` to get out, then run the commit again with `-m`.

---

## 14. Key Takeaways

[ [Top](#git-and-github-basics) | [Home](../README.md#4-firstrepo) ]

- **Git** is the program on your laptop that saves snapshots. **GitHub** is the website that stores them online.
- **Fork** (on GitHub) and **clone** (in the terminal) happen **once** per project. Always clone **your fork**, not the original.
- After that, the everyday loop is **status → add → commit → push**.
- `git add` chooses what goes in the snapshot; `git commit -m "..."` saves it on your laptop; `git push` sends it to GitHub.
- `git status` tells you exactly where you are and usually what to do next. Run it constantly.
- Your work isn't turned in until you can see it on GitHub in your browser.

Put simply: fork it, clone it, change it, then add, commit, push — and go look.

---

*Zip Code Wilmington — Git and GitHub Basics: What They Are and Why They Matter*

[ [Top](#git-and-github-basics) | [Home](../README.md#4-firstrepo) ]
