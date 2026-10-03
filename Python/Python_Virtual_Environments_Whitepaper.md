# Python Virtual Environments and pip

[ [Home](../README.md#6-python) ]

**Practical Techniques for Beginners**
*Zip Code Wilmington*

---

## About This Document <!-- omit from toc -->

[ [Top](#python-virtual-environments-and-pip) | [Home](../README.md#6-python) ]

This is a focused deep-dive on one specific piece of working in Python: installing other people's code into your project, and keeping each project's installed code separate from every other project's. It assumes you can already write and run a small Python script (`python3 hello.py`) from the terminal, and it covers the handful of commands — `venv`, `pip`, and `requirements.txt` — that you'll type at the start of nearly every Python project you ever work on.

---

## Table of Contents <!-- omit from toc -->

[ [Top](#python-virtual-environments-and-pip) | [Home](../README.md#6-python) ]

- [Python Virtual Environments and pip](#python-virtual-environments-and-pip)
  - [1. What Is a Virtual Environment?](#1-what-is-a-virtual-environment)
  - [2. Why You Need One](#2-why-you-need-one)
  - [3. Creating and Activating a Virtual Environment](#3-creating-and-activating-a-virtual-environment)
  - [4. Installing Packages with pip](#4-installing-packages-with-pip)
  - [5. requirements.txt: Sharing What You Installed](#5-requirementstxt-sharing-what-you-installed)
  - [6. Virtual Environments, Git, and Your Editor](#6-virtual-environments-git-and-your-editor)
  - [7. Common Beginner Mistakes](#7-common-beginner-mistakes)
  - [8. Key Takeaways](#8-key-takeaways)

---

## 1. What Is a Virtual Environment?

[ [Top](#python-virtual-environments-and-pip) | [Home](../README.md#6-python) ]

Python ships with a large **standard library** — `json`, `csv`, `math`, `datetime`, and hundreds more — that you can `import` with nothing extra installed. But most real projects also need **third-party packages**: code someone else wrote and published, like `requests` (for making HTTP requests) or `pandas` (for working with tables of data). Those packages are downloaded from the **Python Package Index** (PyPI) using a tool called **`pip`**.

The question is *where* `pip` puts them. A **virtual environment** answers it: it's an ordinary folder, usually named `.venv`, sitting inside your project, that contains its own private copy of the `python` command, its own `pip`, and its own `site-packages` folder where installed packages land.

```tree
my-project/
├── .venv/                 ← the virtual environment
│   ├── bin/
│   │   ├── python         ← this project's python
│   │   ├── pip            ← this project's pip
│   │   └── activate       ← the script that switches you into it
│   └── lib/python3.14/site-packages/   ← packages installed for this project
├── main.py
└── requirements.txt
```

Think of it as a separate toolbox per project. Whatever you install while working on `my-project` goes into `my-project`'s toolbox, and nowhere else.

| Term | Meaning |
|---|---|
| **Package** | A bundle of Python code published for others to install (`requests`, `pandas`, `pytest`) |
| **PyPI** | The Python Package Index — the public website `pip` downloads packages from |
| **pip** | Python's package installer |
| **Virtual environment** (venv) | A folder holding a private `python`, `pip`, and set of installed packages for one project |
| **Activating** | Switching your current terminal session so `python` and `pip` mean *this project's* copies |
| **Dependency** | A package your project needs in order to run |
| **`requirements.txt`** | A plain text file listing a project's dependencies, so anyone can install the same set |

---

## 2. Why You Need One

[ [Top](#python-virtual-environments-and-pip) | [Home](../README.md#6-python) ]

- **Your Mac's Python won't let you install packages into it directly.** If you installed Python with Homebrew and try `pip3 install requests` outside a virtual environment, you'll get `error: externally-managed-environment`. That's deliberate: the system-wide Python is shared by other tools on your machine, and installing into it can break them. The error message is Python telling you to use a virtual environment.
- **Different projects need different versions.** One project might need `pandas` 2.1 and another 2.3. Without separate environments, installing one version silently replaces the other, and an old project that used to work stops working for no visible reason.
- **It makes your project reproducible.** A virtual environment plus a `requirements.txt` file (Section 5) means a teammate — or you, on a new laptop — can rebuild exactly the same setup with two commands.
- **It's disposable.** If an environment gets into a strange state, delete the `.venv` folder and make a new one. Nothing outside the project is affected.

---

## 3. Creating and Activating a Virtual Environment

[ [Top](#python-virtual-environments-and-pip) | [Home](../README.md#6-python) ]

From inside your project folder, create the environment once:

```bash
cd ~/Projects/my-project
python3 -m venv .venv
```

`python3 -m venv` runs Python's built-in `venv` module, and `.venv` is the name of the folder to create. (The leading dot makes it a hidden folder, so it stays out of the way in `ls`.)

Then **activate** it — and do this every time you open a new terminal to work on the project:

```bash
source .venv/bin/activate
```

Your prompt changes to show the environment's name, which is how you know it worked:

```text
(.venv) kris@mac my-project %
```

While it's active, plain `python` and `pip` now point at the project's own copies. You can check:

```bash
which python
# /Users/kris/Projects/my-project/.venv/bin/python
```

When you're done, switch back to normal:

```bash
deactivate
```

Activation only affects the one terminal window or tab you ran it in. Open a new tab, and you'll need to `source .venv/bin/activate` again.

---

## 4. Installing Packages with pip

[ [Top](#python-virtual-environments-and-pip) | [Home](../README.md#6-python) ]

With the environment active, install a package:

```bash
pip install requests
```

`pip` downloads `requests` from PyPI, along with any packages *it* depends on, and puts them all in `.venv`. Now a script can use it:

```python
# octocat.py
import requests

response = requests.get("https://api.github.com/users/octocat")
print(response.status_code)
print(response.json()["name"])
```

```bash
python octocat.py
# 200
# The Octocat
```

Run the same script *without* the environment active, and Python can't find the package at all:

```text
ModuleNotFoundError: No module named 'requests'
```

That error, nine times out of ten, means "you forgot to activate your virtual environment" — not "the package is broken."

A few more `pip` commands you'll use regularly:

| Command | What it does |
|---|---|
| `pip install requests` | Install the latest version of a package |
| `pip install "requests==2.34.2"` | Install one exact version |
| `pip install --upgrade requests` | Upgrade an installed package to the latest version |
| `pip uninstall requests` | Remove a package |
| `pip list` | Show every package installed in this environment |
| `pip show requests` | Show details about one installed package (version, location, what it depends on) |

You'll also see `python -m pip install ...` in documentation. It does the same thing, but guarantees that the `pip` you're running belongs to the `python` you're running — a useful habit when you're not sure which environment is active.

---

## 5. requirements.txt: Sharing What You Installed

[ [Top](#python-virtual-environments-and-pip) | [Home](../README.md#6-python) ]

Your `.venv` folder is not something you share (Section 6). What you share instead is a *list* of what's in it. `pip freeze` prints every installed package with its exact version, and you save that to a file:

```bash
pip freeze > requirements.txt
```

```yaml
# requirements.txt
certifi==2026.7.22
charset-normalizer==3.5.2
idna==3.20
requests==2.34.2
urllib3==2.8.0
```

You only asked for `requests`, but the other four are packages `requests` needs, so they're listed too. Pinning exact versions is the point: it means everyone gets the same code.

When you clone someone else's Python project, this is the routine, every single time:

```bash
git clone https://github.com/someone/their-project
cd their-project
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

`-r` means "read the list of packages from this file." Five commands, and you have exactly the setup the project's author had.

Re-run `pip freeze > requirements.txt` whenever you install or upgrade something, so the file stays in sync with what the project really uses.

---

## 6. Virtual Environments, Git, and Your Editor

[ [Top](#python-virtual-environments-and-pip) | [Home](../README.md#6-python) ]

**Never commit `.venv` to Git.** It can contain thousands of files, it's specific to your machine (it records absolute paths to your Python installation), and anyone can rebuild it from `requirements.txt`. Add it to your project's `.gitignore`:

```text
# .gitignore
.venv/
```

Commit `requirements.txt` instead.

**Point your editor at the environment.** VS Code usually notices a `.venv` folder in your project and offers to use it. If it doesn't — or if VS Code marks `import requests` with a squiggly "could not be resolved" warning even though the script runs fine in the terminal — open the Command Palette and run **Python: Select Interpreter**, then pick the one inside `.venv`. VS Code's integrated terminal will then activate the environment for you whenever you open a new one.

**A faster alternative you'll see: `uv`.** `uv` is a newer tool that does the same jobs as `venv` and `pip`, much faster (`uv venv` to create, `uv pip install requests` to install). Everything in this document still applies — same `.venv` folder, same `requirements.txt` — so if a project's README tells you to use `uv`, you already understand what it's doing.

---

## 7. Common Beginner Mistakes

[ [Top](#python-virtual-environments-and-pip) | [Home](../README.md#6-python) ]

> **Forgetting to activate.** You open a new terminal tab, run your script, and get `ModuleNotFoundError`. Check your prompt for `(.venv)` before anything else.

> **Installing before activating.** If `pip install` ran outside the environment, the package didn't go into your project. Activate, then install again.

> **Fighting the `externally-managed-environment` error.** You'll find advice online to add `--break-system-packages` to make the error go away. Don't. The error is pointing you toward a virtual environment; create one.

> **Committing `.venv` to Git.** Your repository balloons with thousands of files that won't even work on a teammate's machine. Add `.venv/` to `.gitignore` before your first commit.

> **Moving or renaming the project folder.** A virtual environment remembers the absolute path it was created at. After moving a project, the old `.venv` often stops working. Delete it and recreate it — that's what `requirements.txt` is for.

> **Forgetting to update `requirements.txt`.** The project runs on your machine but fails on everyone else's, because the package you installed last week never made it into the file. Re-run `pip freeze > requirements.txt` after every install.

> **Using `sudo pip install`.** Installing with administrator rights writes into system folders and can break tools your Mac relies on. You never need `sudo` inside a virtual environment.

---

## 8. Key Takeaways

[ [Top](#python-virtual-environments-and-pip) | [Home](../README.md#6-python) ]

- A **virtual environment** is a `.venv` folder inside your project holding its own `python`, `pip`, and installed packages.
- Create it once with `python3 -m venv .venv`; activate it every session with `source .venv/bin/activate`; look for `(.venv)` in your prompt.
- Install packages with `pip install <name>` *after* activating.
- Record dependencies with `pip freeze > requirements.txt`, and rebuild them anywhere with `pip install -r requirements.txt`.
- Commit `requirements.txt`; put `.venv/` in `.gitignore`.
- `ModuleNotFoundError` for a package you installed almost always means the environment isn't active.

Put simply: one project, one `.venv`, one `requirements.txt`, and activate before you do anything else.

---

*Zip Code Wilmington — Python Virtual Environments and pip: Practical Techniques for Beginners*

[ [Top](#python-virtual-environments-and-pip) | [Home](../README.md#6-python) ]
