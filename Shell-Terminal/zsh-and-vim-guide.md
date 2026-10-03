# Your Shell and Your Editor: A Beginner's Guide to `.zshrc`, Oh My Zsh, and Vim

[ [Home](../README.md#3-terminal--shell) ]

This guide covers four things every developer runs into in the first week:

1. What `.zshrc` is and how it works
2. Environment variables and aliases
3. Sourcing `.zshrc` (and why your changes "don't work")
4. Oh My Zsh and the plugins worth installing
5. A quick tour of vi/vim, so you're never trapped in it again

Zsh is the default shell on macOS (since Catalina) and is easy to install on Linux (`sudo apt install zsh`, then `chsh -s $(which zsh)`). Check which shell you're running with:

```zsh
echo $SHELL     # your login shell, e.g. /bin/zsh
echo $0         # the shell running right now
```

---

## 1. What is `.zshrc`?

[ [Top](#your-shell-and-your-editor-a-beginners-guide-to-zshrc-oh-my-zsh-and-vim) | [Home](../README.md#3-terminal--shell) ]

`.zshrc` is a plain-text script that zsh runs **every time you open a new interactive terminal**. Anything you put in it (settings, variables, aliases, functions) is applied to that terminal session automatically.

- It lives in your home directory: `~/.zshrc`
- The leading dot makes it a *hidden* file. Use `ls -a ~` to see it.
- If it doesn't exist yet, create it: `touch ~/.zshrc`

Open it with any editor:

```zsh
code ~/.zshrc    # VS Code (if the `code` command is installed)
vim ~/.zshrc     # Vim (see section 5)
nano ~/.zshrc    # Nano, the simplest option
```

### Zsh's other startup files (for reference)

[ [Top](#your-shell-and-your-editor-a-beginners-guide-to-zshrc-oh-my-zsh-and-vim) | [Back](#1-what-is-zshrc) | [Home](../README.md#3-terminal--shell) ]

Zsh reads several files at startup. As a beginner, you'll mostly use `.zshrc`, but it helps to know the others exist:

| File | When it runs | Typical use |
|---|---|---|
| `~/.zshenv` | Every zsh, even scripts | Rarely needed; keep minimal |
| `~/.zprofile` | Login shells | Homebrew setup (`eval "$(/opt/homebrew/bin/brew shellenv)"`) |
| `~/.zshrc` | Interactive shells | **Aliases, prompt, plugins, most PATH changes** |
| `~/.zlogin` | Login shells, after `.zshrc` | Rarely used |

> On macOS, each new Terminal window is a login shell, so both `.zprofile` and `.zshrc` run.

### A well-organized `.zshrc`

[ [Top](#your-shell-and-your-editor-a-beginners-guide-to-zshrc-oh-my-zsh-and-vim) | [Back](#1-what-is-zshrc) | [Home](../README.md#3-terminal--shell) ]

Comments start with `#`. Grouping your file into sections keeps it readable as it grows:

```zsh
# ~/.zshrc

# ---------- Oh My Zsh (if installed) ----------
export ZSH="$HOME/.oh-my-zsh"
ZSH_THEME="robbyrussell"
plugins=(git z)
source $ZSH/oh-my-zsh.sh

# ---------- Environment variables ----------
export EDITOR="vim"
export PATH="$HOME/bin:$PATH"

# ---------- Aliases ----------
alias ll="ls -lah"
alias gs="git status"

# ---------- Functions ----------
mkcd() { mkdir -p "$1" && cd "$1"; }
```

---

## 2. Environment Variables

[ [Top](#your-shell-and-your-editor-a-beginners-guide-to-zshrc-oh-my-zsh-and-vim) | [Home](../README.md#3-terminal--shell) ]

An **environment variable** is a named value that your shell and every program you launch from it can read. Programs use them for configuration: where to find tools, which editor to open, which Java to use, and so on.

### Viewing variables

[ [Top](#your-shell-and-your-editor-a-beginners-guide-to-zshrc-oh-my-zsh-and-vim) | [Back](#2-environment-variables) | [Home](../README.md#3-terminal--shell) ]

```zsh
echo $HOME        # /Users/yourname
echo $USER        # yourname
echo $PATH        # colon-separated list of directories
printenv          # list every environment variable
printenv PATH     # print just one
```

### Setting variables

[ [Top](#your-shell-and-your-editor-a-beginners-guide-to-zshrc-oh-my-zsh-and-vim) | [Back](#2-environment-variables) | [Home](../README.md#3-terminal--shell) ]

```zsh
MY_VAR="hello"           # shell variable: only this shell sees it
export MY_VAR="hello"    # environment variable: child programs see it too
```

Rules that trip beginners up:

- **No spaces around `=`.** `export NAME = "x"` is an error; `export NAME="x"` is correct.
- **Quote values** that contain spaces: `export GREETING="hello world"`.
- Setting a variable in the terminal lasts **only for that session**. Put it in `.zshrc` to make it permanent.

### `PATH`: the most important variable

[ [Top](#your-shell-and-your-editor-a-beginners-guide-to-zshrc-oh-my-zsh-and-vim) | [Back](#2-environment-variables) | [Home](../README.md#3-terminal--shell) ]

When you type a command like `python3` or `mvn`, the shell searches each directory in `$PATH`, left to right, and runs the first match.

```zsh
echo $PATH | tr ':' '\n'   # show PATH one directory per line
which python3              # show which file a command resolves to
```

To add a directory, **prepend or append; never overwrite**:

```zsh
export PATH="$HOME/bin:$PATH"        # prepend: your version wins
export PATH="$PATH:$HOME/tools"      # append: system version wins
```

> ⚠️ `export PATH="$HOME/bin"` (without `:$PATH`) replaces the whole list, and suddenly `ls`, `git`, and everything else "stop existing." If this happens, open a new terminal after fixing `.zshrc`, or run `export PATH="/usr/bin:/bin:/usr/sbin:/sbin"` to recover temporarily.

### Common variables you'll set as a developer

[ [Top](#your-shell-and-your-editor-a-beginners-guide-to-zshrc-oh-my-zsh-and-vim) | [Back](#2-environment-variables) | [Home](../README.md#3-terminal--shell) ]

```zsh
export EDITOR="vim"                                   # used by git, crontab, etc.
export JAVA_HOME=$(/usr/libexec/java_home)            # macOS: current JDK
export JAVA_HOME=$(/usr/libexec/java_home -v 21)      # macOS: a specific version
export PATH="$JAVA_HOME/bin:$PATH"
```

### Secrets: a word of caution

[ [Top](#your-shell-and-your-editor-a-beginners-guide-to-zshrc-oh-my-zsh-and-vim) | [Back](#2-environment-variables) | [Home](../README.md#3-terminal--shell) ]

It's common to see API keys in `.zshrc` (`export OPENAI_API_KEY=...`). That works, but **never commit your `.zshrc` to a public repo with secrets in it.** A safer pattern is a separate, untracked file:

```zsh
# in ~/.zshrc
[ -f ~/.secrets ] && source ~/.secrets
```

For project-specific values, prefer a `.env` file inside the project (and add `.env` to `.gitignore`).

---

## 3. Aliases

[ [Top](#your-shell-and-your-editor-a-beginners-guide-to-zshrc-oh-my-zsh-and-vim) | [Home](../README.md#3-terminal--shell) ]

An **alias** is a shortcut: a short name that expands to a longer command.

```zsh
alias name="command to run"
```

Same rule as variables: **no spaces around `=`**, and quote the command.

### Useful starter aliases

[ [Top](#your-shell-and-your-editor-a-beginners-guide-to-zshrc-oh-my-zsh-and-vim) | [Back](#3-aliases) | [Home](../README.md#3-terminal--shell) ]

```zsh
# Navigation
alias ..="cd .."
alias ...="cd ../.."
alias ll="ls -lah"            # long listing, hidden files, human-readable sizes

# Safety nets: ask before overwriting or deleting
alias rm="rm -i"
alias cp="cp -i"
alias mv="mv -i"

# Git
alias gs="git status"
alias ga="git add"
alias gc="git commit -m"
alias gco="git checkout"
alias gp="git push"
alias gl="git log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(auto)%d%C(reset)' --all"
alias gitlog=gl
git config --global alias.all '!f() { ls -R -d */.git | xargs -I{} bash -c "echo {} && git -C {}/../ $1"; }; f'

# Docker
alias dps="docker ps"
alias dc="docker -compose"
alias dcu="docker -compose up -d"
alias dcd="docker -compose down"

# Tailscale
alias tailscale='/Applications/Tailscale.app/Contents/MacOS/Tailscale'

# Editing your config
alias zshconfig="code ~/.zshrc"
alias reload="source ~/.zshrc"

# Project shortcuts
alias dev="cd ~/dev"
alias pro="cd ~/Projects"
```

### Managing aliases

[ [Top](#your-shell-and-your-editor-a-beginners-guide-to-zshrc-oh-my-zsh-and-vim) | [Back](#3-aliases) | [Home](../README.md#3-terminal--shell) ]

```zsh
alias            # list all aliases
alias gs         # show what one alias expands to
type gs          # also shows whether something is an alias, function, or program
unalias gs       # remove an alias for this session
\rm file.txt     # a leading backslash bypasses the alias and runs the real command
```

### When to use a function instead

[ [Top](#your-shell-and-your-editor-a-beginners-guide-to-zshrc-oh-my-zsh-and-vim) | [Back](#3-aliases) | [Home](../README.md#3-terminal--shell) ]

Aliases can't take arguments in the middle of a command. If you need `$1`, write a function:

```zsh
# Make a directory and cd into it
mkcd() {
  mkdir -p "$1" && cd "$1"
}

# Create a new Java/Maven-style project folder structure
newproj() {
  mkdir -p "$1"/src/{main,test}/java && cd "$1" && git init
}
```

Usage: `mkcd my-new-folder`

---

## 4. Sourcing `.zshrc`

[ [Top](#your-shell-and-your-editor-a-beginners-guide-to-zshrc-oh-my-zsh-and-vim) | [Home](../README.md#3-terminal--shell) ]

Here's the #1 beginner confusion: **you edit `.zshrc`, save it, and nothing changes.** That's because `.zshrc` only runs when a shell *starts*. Your already-open terminal read the old version.

You have two options:

```zsh
source ~/.zshrc    # re-run .zshrc in the current shell
. ~/.zshrc         # same thing; `.` is shorthand for `source`
```

Or simply open a new terminal tab/window.

### What `source` actually does

[ [Top](#your-shell-and-your-editor-a-beginners-guide-to-zshrc-oh-my-zsh-and-vim) | [Back](#4-sourcing-zshrc) | [Home](../README.md#3-terminal--shell) ]

`source file` runs the file's commands **inside your current shell**, so any variables, aliases, or `cd`s it makes stick around. By contrast, running a script normally (`./script.sh` or `zsh script.sh`) starts a *new* child shell; its changes vanish when it exits.

```zsh
# demo.sh contains:  export DEMO="hi"
zsh demo.sh;    echo $DEMO     # prints nothing
source demo.sh; echo $DEMO     # prints: hi
```

### Gotchas

[ [Top](#your-shell-and-your-editor-a-beginners-guide-to-zshrc-oh-my-zsh-and-vim) | [Back](#4-sourcing-zshrc) | [Home](../README.md#3-terminal--shell) ]

- **Sourcing doesn't remove things.** If you delete an alias from `.zshrc` and re-source, the old alias still exists in that session. Open a new terminal (or run `exec zsh` to restart the shell in place) for a clean slate.
- **Repeated sourcing can duplicate PATH entries.** `export PATH="$HOME/bin:$PATH"` adds `~/bin` again each time. Harmless, but if it bothers you, add `typeset -U path` near the top of `.zshrc`; zsh will then keep `PATH` entries unique.
- **Syntax errors** print a message with a line number, e.g. `/Users/you/.zshrc:42: parse error`. Open the file at that line and fix it.

---

## 5. Oh My Zsh

[ [Top](#your-shell-and-your-editor-a-beginners-guide-to-zshrc-oh-my-zsh-and-vim) | [Home](../README.md#3-terminal--shell) ]

[Oh My Zsh](https://ohmyz.sh) is a free, community-run framework that manages your zsh configuration. Out of the box it gives you a nicer prompt (with your git branch), hundreds of plugins, and themes, all toggled from `.zshrc`.

### Prerequisites

[ [Top](#your-shell-and-your-editor-a-beginners-guide-to-zshrc-oh-my-zsh-and-vim) | [Back](#5-oh-my-zsh) | [Home](../README.md#3-terminal--shell) ]

You need `zsh`, `git`, and `curl` installed. On macOS, run `xcode-select --install` first if `git` is missing.

### Installing

[ [Top](#your-shell-and-your-editor-a-beginners-guide-to-zshrc-oh-my-zsh-and-vim) | [Back](#5-oh-my-zsh) | [Home](../README.md#3-terminal--shell) ]

```zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

> The installer **replaces your `.zshrc`** with its template and saves the old one as `~/.zshrc.pre-oh-my-zsh`. Copy any custom aliases or variables from the backup into the new file.

After installing, your `.zshrc` will contain a few key lines:

```zsh
export ZSH="$HOME/.oh-my-zsh"   # where Oh My Zsh lives
ZSH_THEME="robbyrussell"        # the prompt theme
plugins=(git)                   # enabled plugins
source $ZSH/oh-my-zsh.sh        # load it all; must come AFTER the lines above
```

Put your own aliases and exports **below** the `source $ZSH/oh-my-zsh.sh` line so they override Oh My Zsh's defaults when names collide.

### Themes

[ [Top](#your-shell-and-your-editor-a-beginners-guide-to-zshrc-oh-my-zsh-and-vim) | [Back](#5-oh-my-zsh) | [Home](../README.md#3-terminal--shell) ]

Change `ZSH_THEME` and re-source. A few good ones bundled with Oh My Zsh:

- `robbyrussell`: the default; minimal and fast
- `agnoster`: powerline-style segments (needs a [Powerline/Nerd Font](https://www.nerdfonts.com))
- `af-magic`, `bira`, `ys`: informative two-line prompts
- `random`: picks a new theme every session; fun for browsing

For a highly customizable prompt later on, look at [Powerlevel10k](https://github.com/romkatv/powerlevel10k) or [Starship](https://starship.rs).

### Plugins: the essentials for beginners

[ [Top](#your-shell-and-your-editor-a-beginners-guide-to-zshrc-oh-my-zsh-and-vim) | [Back](#5-oh-my-zsh) | [Home](../README.md#3-terminal--shell) ]

Plugins are enabled by listing them, **separated by spaces (not commas)**, inside `plugins=( )`:

```zsh
plugins=(git z sudo colored-man-pages copypath zsh-autosuggestions zsh-syntax-highlighting)
```

#### Bundled plugins (already installed; just enable them)

[ [Top](#your-shell-and-your-editor-a-beginners-guide-to-zshrc-oh-my-zsh-and-vim) | [Back](#plugins-the-essentials-for-beginners) | [Home](../README.md#3-terminal--shell) ]

| Plugin | What it does | Try it |
|---|---|---|
| **git** | ~200 git aliases. Learn the real commands first, then let these save keystrokes. | `gst` (status), `gaa` (add all), `gcmsg "msg"` (commit), `gp` (push), `gl` (pull), `gco` (checkout), `glog` |
| **z** | Jump to frequently used directories by typing part of the name. | After visiting `~/dev/projects/capstone` once, type `z cap` from anywhere |
| **sudo** | Press `Esc` twice to prefix the current (or previous) command with `sudo`. | Forgot `sudo`? Hit `Esc Esc`, then Enter |
| **colored-man-pages** | Adds color to `man` pages so they're easier to read. | `man ls` |
| **copypath** | Copies the current directory's path to the clipboard. | `copypath` |
| **copyfile** | Copies a file's contents to the clipboard. | `copyfile ~/.ssh/id_ed25519.pub` |
| **dirhistory** | `Alt+←` / `Alt+→` to move back/forward through directories you've visited. | |
| **history** | Shortcuts for searching history. | `h` (show history), `hs docker` (search) |
| **web-search** | Search the web from the terminal. | `google zsh aliases`, `stackoverflow null pointer` |
| **macos** | macOS helpers (macOS only). | `ofd` (open current dir in Finder), `cdf` (cd to the Finder window's dir) |

Language/tool plugins add tab-completion for those tools; enable the ones you use: `docker`, `npm`, `node`, `python`, `pip`, `mvn`, `gradle`, `brew`.

> 💡 Run `alias | grep git` to see every git alias the plugin added, or browse the full list at `~/.oh-my-zsh/plugins/git/README.md`.

#### Must-have external plugins (install first, then enable)

[ [Top](#your-shell-and-your-editor-a-beginners-guide-to-zshrc-oh-my-zsh-and-vim) | [Back](#plugins-the-essentials-for-beginners) | [Home](../README.md#3-terminal--shell) ]

These three aren't bundled, but almost everyone installs them.

**zsh-autosuggestions** suggests commands as you type, based on your history, shown in faded gray. Press `→` (right arrow) to accept.

```zsh
git clone https://github.com/zsh-users/zsh-autosuggestions \
  ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
```

**zsh-history-substring-search** ala Fish, type in any part of any command from history and then press chosen keys, like UP and DOWN arrows, to cycle through matches.

```zsh
git clone https://github.com/zsh-users/zsh-history-substring-search \
  ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-history-substring-search
```

**zsh-syntax-highlighting** colors commands as you type: green if the command exists, red if it doesn't. You catch typos *before* pressing Enter.

```zsh
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git \
  ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

Then add your plugins to the list. **`zsh-syntax-highlighting` should be last**:

```zsh
plugins=(
  git
  z
  colored-man-pages
  sudo
  macos
  python
  uv
  virtualenv
  zsh-autosuggestions
  zsh-history-substring-search
  zsh-syntax-highlighting)
```

Finally: `source ~/.zshrc`.

### Maintaining Oh My Zsh

[ [Top](#your-shell-and-your-editor-a-beginners-guide-to-zshrc-oh-my-zsh-and-vim) | [Back](#5-oh-my-zsh) | [Home](../README.md#3-terminal--shell) ]

```zsh
omz update            # update Oh My Zsh
omz plugin list       # list available plugins
omz theme list        # list available themes
omz reload            # reload the configuration
```

A word of caution: every plugin adds a little startup time. If new terminals start feeling slow, trim plugins you don't use. You can measure with `time zsh -i -c exit`.

To uninstall: `uninstall_oh_my_zsh` (your previous `.zshrc` is restored).

---

## 6. A Quick Tour of vi/vim

[ [Top](#your-shell-and-your-editor-a-beginners-guide-to-zshrc-oh-my-zsh-and-vim) | [Home](../README.md#3-terminal--shell) ]

`vi` is a text editor that exists on virtually every Unix, Linux, and macOS system; `vim` ("Vi IMproved") is the modern version you'll usually get when you type `vi`. Even if you use VS Code or IntelliJ every day, you'll land in vim eventually: when `git commit` opens without `-m`, when you SSH into a server, or when you edit a config file like `.zshrc`.

### The one big idea: modes

[ [Top](#your-shell-and-your-editor-a-beginners-guide-to-zshrc-oh-my-zsh-and-vim) | [Back](#6-a-quick-tour-of-vivim) | [Home](../README.md#3-terminal--shell) ]

Vim is a **modal** editor. Keys do different things depending on the mode you're in:

| Mode | Purpose | How to enter it |
|---|---|---|
| **Normal** | Move around, delete, copy, paste. *The default mode.* | `Esc` |
| **Insert** | Type text like a normal editor | `i` (and others below) |
| **Visual** | Select text | `v` (characters), `V` (lines) |
| **Command-line** | Save, quit, search/replace | `:` from Normal mode |

**When in doubt, press `Esc`.** It always gets you back to Normal mode.

### Surviving: open, edit, save, quit

[ [Top](#your-shell-and-your-editor-a-beginners-guide-to-zshrc-oh-my-zsh-and-vim) | [Back](#6-a-quick-tour-of-vivim) | [Home](../README.md#3-terminal--shell) ]

```text
vim notes.txt     open (or create) a file
i                 enter Insert mode, then type your text
Esc               back to Normal mode
:w                write (save)
:q                quit
:wq   or  :x      save and quit
:q!               quit WITHOUT saving (discard changes)
```

> 🚪 **Stuck in vim?** Press `Esc`, then type `:q!` and hit Enter. You're out.

**Git commit messages in vim:** type `i`, write your message, press `Esc`, then `:wq`. To abort the commit, quit with `:q!` and leave the message empty. (Prefer a different editor for git? `git config --global core.editor "code --wait"`.)

### Moving around (Normal mode)

[ [Top](#your-shell-and-your-editor-a-beginners-guide-to-zshrc-oh-my-zsh-and-vim) | [Back](#6-a-quick-tour-of-vivim) | [Home](../README.md#3-terminal--shell) ]

```text
h  j  k  l        left, down, up, right (arrow keys also work)
w  /  b           forward / back one word
0  /  $           start / end of line
gg  /  G          top / bottom of file
42G  or  :42      jump to line 42
Ctrl+d / Ctrl+u   scroll down / up half a page
```

### Entering Insert mode

[ [Top](#your-shell-and-your-editor-a-beginners-guide-to-zshrc-oh-my-zsh-and-vim) | [Back](#6-a-quick-tour-of-vivim) | [Home](../README.md#3-terminal--shell) ]

```text
i     insert before the cursor
a     append after the cursor
I     insert at start of line
A     append at end of line
o     open a new line below
O     open a new line above
```

### Editing (Normal mode)

[ [Top](#your-shell-and-your-editor-a-beginners-guide-to-zshrc-oh-my-zsh-and-vim) | [Back](#6-a-quick-tour-of-vivim) | [Home](../README.md#3-terminal--shell) ]

```text
x         delete the character under the cursor
dd        delete (cut) the current line
dw        delete to the end of the word
yy        yank (copy) the current line
p  /  P   paste after / before the cursor
u         undo
Ctrl+r    redo
.         repeat the last change
```

### The vim "grammar": verb + count + motion

[ [Top](#your-shell-and-your-editor-a-beginners-guide-to-zshrc-oh-my-zsh-and-vim) | [Back](#6-a-quick-tour-of-vivim) | [Home](../README.md#3-terminal--shell) ]

Vim commands combine like words in a sentence. Once this clicks, you don't memorize commands, you compose them:

| Command | Reads as | Result |
|---|---|---|
| `dw` | **d**elete **w**ord | delete to next word |
| `d3w` | **d**elete **3** **w**ords | delete three words |
| `3dd` | **3** × **d**elete line | delete three lines |
| `d$` | **d**elete to end of line | |
| `cw` | **c**hange **w**ord | delete word and enter Insert mode |
| `yG` | **y**ank to end of file | copy everything below |
| `ci"` | **c**hange **i**nside **"** quotes | replace text inside quotes |

### Searching and replacing

[ [Top](#your-shell-and-your-editor-a-beginners-guide-to-zshrc-oh-my-zsh-and-vim) | [Back](#6-a-quick-tour-of-vivim) | [Home](../README.md#3-terminal--shell) ]

```text
/word          search forward for "word"
?word          search backward
n  /  N        next / previous match
:%s/old/new/g  replace every "old" with "new" in the file
:%s/old/new/gc same, but confirm each one
```

### Visual mode (selecting)

[ [Top](#your-shell-and-your-editor-a-beginners-guide-to-zshrc-oh-my-zsh-and-vim) | [Back](#6-a-quick-tour-of-vivim) | [Home](../README.md#3-terminal--shell) ]

```text
v      start selecting characters
V      select whole lines
then move with h/j/k/l, and press:
d      delete the selection
y      yank (copy) it
>  <   indent / un-indent it
```

### A starter `~/.vimrc`

[ [Top](#your-shell-and-your-editor-a-beginners-guide-to-zshrc-oh-my-zsh-and-vim) | [Back](#6-a-quick-tour-of-vivim) | [Home](../README.md#3-terminal--shell) ]

Just like `.zshrc` configures zsh, `~/.vimrc` configures vim. A minimal, beginner-friendly setup:

```vim
syntax on              " syntax highlighting
set number             " show line numbers
set relativenumber     " line numbers relative to the cursor (great for 5j, 3dd)
set tabstop=4          " a tab displays as 4 spaces
set shiftwidth=4       " indent with 4 spaces
set expandtab          " insert spaces instead of tab characters
set autoindent         " keep indentation on new lines
set incsearch          " search as you type
set hlsearch           " highlight search matches
set ignorecase smartcase  " case-insensitive unless you type a capital
set mouse=a            " enable the mouse
```

(In `.vimrc`, comments start with `"` instead of `#`.)

### Keep learning

[ [Top](#your-shell-and-your-editor-a-beginners-guide-to-zshrc-oh-my-zsh-and-vim) | [Back](#6-a-quick-tour-of-vivim) | [Home](../README.md#3-terminal--shell) ]

- Run **`vimtutor`** in your terminal: a built-in, ~30-minute interactive lesson. Highly recommended.
- Practice a little daily. Vim feels slow for about a week, then gets fast.
- Like the keybindings but prefer your IDE? Install the **Vim** extension in VS Code or **IdeaVim** in IntelliJ.

---

## Quick Reference

[ [Top](#your-shell-and-your-editor-a-beginners-guide-to-zshrc-oh-my-zsh-and-vim) | [Home](../README.md#3-terminal--shell) ]

| Task | Command |
|---|---|
| Edit your zsh config | `code ~/.zshrc` or `vim ~/.zshrc` |
| Apply changes | `source ~/.zshrc` |
| Restart the shell cleanly | `exec zsh` |
| Set a permanent variable | add `export NAME="value"` to `.zshrc` |
| Add to PATH | `export PATH="/new/dir:$PATH"` |
| Create an alias | `alias ll="ls -lah"` |
| List aliases | `alias` |
| Find what a command is | `type cmd` / `which cmd` |
| Update Oh My Zsh | `omz update` |
| Quit vim without saving | `Esc` then `:q!` |
| Save and quit vim | `Esc` then `:wq` |
| Learn vim interactively | `vimtutor` |

[ [Top](#your-shell-and-your-editor-a-beginners-guide-to-zshrc-oh-my-zsh-and-vim) | [Home](../README.md#3-terminal--shell) ]
