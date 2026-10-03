# FirstRepo

[ [Home](../README.md#4-firstrepo) ]

Read [Git and GitHub Basics](Git_and_GitHub_Basics_Whitepaper.md) first. It walks through every step of this lab.

## Contents <!-- omit from toc -->

[ [Top](#firstrepo) | [Home](../README.md#4-firstrepo) ]

- [FirstRepo](#firstrepo)
  - [How to Download](#how-to-download)
    - [Part 1 - Forking the Project](#part-1---forking-the-project)
    - [Part 2 - Navigating to _forked_ Repository](#part-2---navigating-to-forked-repository)
    - [Part 3 - Cloning _forked_ repository](#part-3---cloning-forked-repository)
  - [Make Changes](#make-changes)
  - [How to Submit](#how-to-submit)
    - [_Pushing_ local changes to remote repository](#pushing-local-changes-to-remote-repository)

## How to Download

[ [Top](#firstrepo) | [Home](../README.md#4-firstrepo) ]

### Part 1 - Forking the Project

[ [Top](#firstrepo) | [Back](#how-to-download) | [Home](../README.md#4-firstrepo) ]

- navigate to `https://github.com/ZCW-Cohort/FirstRepo`
- To _fork_ the project, click the `Fork` button located at the top right of the project.
- this makes a copy of the code IN YOUR Github ACCOUNT

### Part 2 - Navigating to _forked_ Repository

[ [Top](#firstrepo) | [Back](#how-to-download) | [Home](../README.md#4-firstrepo) ]

- Navigate to **your github account** to find the _newly forked repository_.
- This is your copy of the code, not the original copy of ZipCode's
- Copy the URL of the project to the clipboard.

### Part 3 - Cloning _forked_ repository

[ [Top](#firstrepo) | [Back](#how-to-download) | [Home](../README.md#4-firstrepo) ]

Clone the repository from **your account** into the `~/Projects` directory.

- if you do not have a `~/Projects` directory, make one by executing the following command in terminal when you are in your home directory:
  - `cd`
  - `mkdir ~/Projects`
- navigate to the `~/Projects` directory by executing the following command:
  - `cd ~/Projects`
- clone the project by executing the following command:
  - `git clone https://github.com/YOUR-USERNAME/FirstRepo` (the URL of **your fork**, with your GitHub username in it)
- navigate to the `FirstRepo` directory by executing the following command:
  - `cd FirstRepo`

_Please note, __Projects__, is just a suggestion. Over the years, some have made it __Code__, __Source__, __src__ or even just __p__. _kristofer did that for decades._
Generally, though, you should keep all your source code together in a _folder/directory_. _

## Make Changes

[ [Top](#firstrepo) | [Home](../README.md#4-firstrepo) ]

Edit the `name` variable in the `hello.py` file inside the _FirstRepo_ directory, by adding your name to the file.

## How to Submit

[ [Top](#firstrepo) | [Home](../README.md#4-firstrepo) ]

This is what we refer to as **The 'holy' Triad**, `git add`, `git commit`, `git push`

### _Pushing_ local changes to remote repository

[ [Top](#firstrepo) | [Back](#how-to-submit) | [Home](../README.md#4-firstrepo) ]

- from a _terminal_ navigate to the root directory of the _cloned_ project.
- from the root directory of the project, execute the following commands:
  - add all changes

    ```bash
    git add .
    ```

  - commit changes to be pushed

    ```bash
    git commit -m 'I have added changes'
    ```

  - push changes to your repository

    ```bash
    git push
    ```

- now, check that the code has been copied UP to the Github site.
  - navigate to your fork of the repo, the one in **your account**.
  - make sure the commit message is correct and up to date.
  - look in `hello.py` up on the github site to make sure your name is there.

You can do it, we know you can. Ask around if confused, you're not the only one confused.

[ [Top](#firstrepo) | [Back](#how-to-submit) | [Home](../README.md#4-firstrepo) ]
