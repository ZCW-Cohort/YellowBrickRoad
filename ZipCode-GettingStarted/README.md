# Getting Started (on Day One of Unified Python Course)

[ [Home](../README.md#1-getting-started) ]

## Contents <!-- omit from toc -->

- [Getting Started (on Day One of Unified Python Course)](#getting-started-on-day-one-of-unified-python-course)
  - [Yo! Y'all have Apple silicon Macs](#yo-yall-have-apple-silicon-macs)
    - [gmail and zipcode.rocks](#gmail-and-zipcoderocks)
    - [github](#github)
    - [iCloud](#icloud)
    - [Passwords](#passwords)
  - [DO NOT USE "Find My Mac" - It makes Gloria's life terrible, and you don't want that. Nope, you surely don't.](#do-not-use-find-my-mac---it-makes-glorias-life-terrible-and-you-dont-want-that-nope-you-surely-dont)
    - [DO NOT USE "Find My Mac" - It makes Gloria's life terrible, and you don't want that. Nope, you surely don't.](#do-not-use-find-my-mac---it-makes-glorias-life-terrible-and-you-dont-want-that-nope-you-surely-dont-1)
      - [DO NOT USE "Find My Mac" - It makes Gloria's life terrible, and you don't want that. Nope, you surely don't.](#do-not-use-find-my-mac---it-makes-glorias-life-terrible-and-you-dont-want-that-nope-you-surely-dont-2)
    - [Slack](#slack)
    - [Discord](#discord)
    - [Terminal/Shell](#terminalshell)
      - [Option 1](#option-1)
      - [Option 2](#option-2)
    - [git](#git)
    - [Brew](#brew)
    - [Python](#python)
    - [VSCode](#vscode)
  - [End of First Day Installs](#end-of-first-day-installs)

**This section is for students who are taking the ZipCode course in person.**

Get your Mac onto the classroom wifi. How? Look around.

**Important**: It should go without saying that anytime you are asked to create an account you should ALWAYS:

- **Make sure to use a professional username/handle.** We recommend the username incorporates your name.
- Be sure to add an appropriate avatar (picture or image) to your profile.

## Yo! Y'all have Apple silicon Macs

[ [Top](#getting-started-on-day-one-of-unified-python-course) | [Home](../README.md#1-getting-started) ]

This is important, **DO NOT download x86 or x64_86 programs.**
You will cry. 

**Download** the `apple silicon` or arm64, M1, M2, or M3 versions of things!!

### gmail and zipcode.rocks

[ [Top](#getting-started-on-day-one-of-unified-python-course) | [Back](#yo-yall-have-apple-silicon-macs) | [Home](../README.md#1-getting-started) ]

IF you have not already gotten a **professional email address** for use within the course

- Visit [gmail.com](https://www.google.com/gmail/about/) and create an account.
- make *sure* you choose a *business friendly* username.

Instructors will be handing out a `@zipcode.rocks` email address in a week or so.

### github

[ [Top](#getting-started-on-day-one-of-unified-python-course) | [Back](#yo-yall-have-apple-silicon-macs) | [Home](../README.md#1-getting-started) ]

If you haven't already,

- Visit [github.com](https://github.com/) and signup for an account.
- we will walk thru you getting access to the Github student pack stuff (https://github.com/education/students)

### iCloud

[ [Top](#getting-started-on-day-one-of-unified-python-course) | [Back](#yo-yall-have-apple-silicon-macs) | [Home](../README.md#1-getting-started) ]

Use your spiffy new business gmail account to create an iCloud account (if you don't already have one from your iPhone).
Even if you're an *android-head*, use iCloud for certain things when you're using Apple products. You can always login later on [iCloud](iCloud.com) to access stuff from windoze or android.

### Passwords

[ [Top](#getting-started-on-day-one-of-unified-python-course) | [Back](#yo-yall-have-apple-silicon-macs) | [Home](../README.md#1-getting-started) ]

Use the built-in macOS password manager to manage all of your accounts. (This way you can keep track of your Admin password for MySQL, which I guarantee you will otherwise forget.)
Be sure to get a free iCloud account using your "professional email address" if you don't already have one tied to an iPhone.

## DO NOT USE "Find My Mac" - It makes Gloria's life terrible, and you don't want that. Nope, you surely don't.

### DO NOT USE "Find My Mac" - It makes Gloria's life terrible, and you don't want that. Nope, you surely don't.

#### DO NOT USE "Find My Mac" - It makes Gloria's life terrible, and you don't want that. Nope, you surely don't.

### Slack

[ [Top](#getting-started-on-day-one-of-unified-python-course) | [Back](#yo-yall-have-apple-silicon-macs) | [Home](../README.md#1-getting-started) ]

- Visit [Slack's](https://slack.com/downloads/mac) download page.
- Download the dmg for the latest release.
- Use the downloaded dmg to install the application.
- Sign in to the zcw workspace.

### Discord

[ [Top](#getting-started-on-day-one-of-unified-python-course) | [Back](#yo-yall-have-apple-silicon-macs) | [Home](../README.md#1-getting-started) ]

- Visit [Discord's](https://discord.com/new/download) download page.
- Download the dmg for the latest release.
- Use the downloaded dmg to install the application.
- Join the ZCW Active Cohort channel at https://discord.gg/7KbwdZqh

### Terminal/Shell

[ [Top](#getting-started-on-day-one-of-unified-python-course) | [Back](#yo-yall-have-apple-silicon-macs) | [Home](../README.md#1-getting-started) ]

#### Option 1

- Command (or Cmd) ⌘ - Space bar to open the Spotlight search field.
- Type "Terminal".
- Press Enter.

#### Option 2

- Open Finder
- Navigate to /Applications/Utilities/
- Double click on Terminal.app

Good. Now you're getting acclimated.

### git

[ [Top](#getting-started-on-day-one-of-unified-python-course) | [Back](#yo-yall-have-apple-silicon-macs) | [Home](../README.md#1-getting-started) ]

Using Terminal, issue the following command:

```bash
git --version
```

This should return the a line similar (or an even later version) to:

```bash
git version 2.21.1 (Apple Git-122.3)
```

You may need run the following in order to install git along with other various command line tools.

```bash
xcode-select --install
```

### Brew

[ [Top](#getting-started-on-day-one-of-unified-python-course) | [Back](#yo-yall-have-apple-silicon-macs) | [Home](../README.md#1-getting-started) ]

- Using terminal,
- Visit [https://brew.sh/](https://brew.sh/).
- Follow the directions under "Install Homebrew".

### Python

[ [Top](#getting-started-on-day-one-of-unified-python-course) | [Back](#yo-yall-have-apple-silicon-macs) | [Home](../README.md#1-getting-started) ]

- do a `brew install python@3.14`

### VSCode

[ [Top](#getting-started-on-day-one-of-unified-python-course) | [Back](#yo-yall-have-apple-silicon-macs) | [Home](../README.md#1-getting-started) ]

- install VSCode on macOS
- https://code.visualstudio.com/download
- Download the dmg for the latest release.
- Use the downloaded dmg to install the application.

## End of First Day Installs

[ [Top](#getting-started-on-day-one-of-unified-python-course) | [Home](../README.md#1-getting-started) ]

:upside_down_face:
