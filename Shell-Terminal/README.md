# Console (Terminal, Shell) Lab Level 1

[ [Home](../README.md#3-terminal--shell) ]

## Contents <!-- omit from toc -->

[ [Top](#console-terminal-shell-lab-level-1) | [Home](../README.md#3-terminal--shell) ]

- [Console (Terminal, Shell) Lab Level 1](#console-terminal-shell-lab-level-1)
- [Part 1](#part-1)
  - [1.1 Objectives](#11-objectives)
  - [1.2 Overview](#12-overview)
    - [1.2.1 Other commands worth knowing](#121-other-commands-worth-knowing)
  - [1.3 Unit Test](#13-unit-test)
  - [1.4 Pre-lab \&\& Important Notes](#14-pre-lab--important-notes)
  - [1.5 Instructions](#15-instructions)
- [Part 2](#part-2)
  - [2.1 Objectives](#21-objectives)
  - [2.2 Overview](#22-overview)
  - [2.3 Instructions](#23-instructions)
    - [2.3.1 Creating files and directories](#231-creating-files-and-directories)
      - [2.3.1.1 Creating files with touch](#2311-creating-files-with-touch)
      - [2.3.1.2 Editors](#2312-editors)
      - [2.3.1.3 Creating directories](#2313-creating-directories)
    - [2.3.2 Copying, moving, and renaming](#232-copying-moving-and-renaming)
    - [2.3.3 Destroying files and directories](#233-destroying-files-and-directories)
    - [2.3.4 The Art of Redirection](#234-the-art-of-redirection)
      - [2.3.4.1 Backgrounding](#2341-backgrounding)
- [Part 3](#part-3)
  - [3.1 Other Resources](#31-other-resources)
  - [3.2 Links:](#32-links)

# Part 1

[ [Top](#console-terminal-shell-lab-level-1) | [Home](../README.md#3-terminal--shell) ]

## 1.1 Objectives

[ [Top](#console-terminal-shell-lab-level-1) | [Back](#part-1) | [Home](../README.md#3-terminal--shell) ]

1. In this lab students will learn to navigate their file system using only the terminal
2. Students will practice using the following commands to traverse directories and investigate their contents: `pwd`, `ls`, `cd`, `cat`, `less`, `grep`
3. Why? well, for forever coders have used the shell to interact with a computer, as it can be, with practice, very efficient and _fast_.

## 1.2 Overview

[ [Top](#console-terminal-shell-lab-level-1) | [Back](#part-1) | [Home](../README.md#3-terminal--shell) ]

The console (also referred to as the command line, terminal, or shell) is an essential tool for programmers to be familiar with. The command line shell we will be using is called zsh (the default shell on every Mac). This lab will focus on the basics for navigating and investigating the file system through the command line. In this lab we will only be using the command line in interactive mode, typing one command at a time. Here are the commands we will focus on:

- `pwd` - "Print Working Directory" prints out your current location (known as your current working directory or 'cwd')
- `ls` - lists contents of the cwd
- `cd` - change directory. This is how you move around the file system. You can specify the destination as an absolute or relative path.
- `echo` - prints text to the terminal
- `cat` - concatenates zero or more files. Often used to print the contents of a file to the terminal. [Often misused](https://en.wikipedia.org/wiki/Cat_(Unix)#Useless_use_of_cat)
- `less`/`more` - Display contents of a file one page at a time ...just remember that less is more ([more or less](http://unix.stackexchange.com/questions/81129/what-are-the-differences-between-most-more-and-less)) and you'll be fine.
- `grep` - search for the specified text or pattern

### 1.2.1 Other commands worth knowing

[ [Top](#console-terminal-shell-lab-level-1) | [Back](#12-overview) | [Home](../README.md#3-terminal--shell) ]

- `head` - display the first lines of a file
- `tail` - display the last lines of a file

## 1.3 Unit Test

[ [Top](#console-terminal-shell-lab-level-1) | [Back](#part-1) | [Home](../README.md#3-terminal--shell) ]

This lab is an instructional introduction to terminal. There are no unit tests.

## 1.4 Pre-lab & Important Notes

[ [Top](#console-terminal-shell-lab-level-1) | [Back](#part-1) | [Home](../README.md#3-terminal--shell) ]

It's a good practice to have a directory called `Projects` inside your home directory for all development work. You can create one in Finder (right click -> New Folder) or in the terminal (`mkdir ~/Projects`). This directory will come in handy in case things go horribly wrong, or if you want to back up all of your work. You should always make sure you are working in `Projects` or a directory inside of it during this course.

## 1.5 Instructions

[ [Top](#console-terminal-shell-lab-level-1) | [Back](#part-1) | [Home](../README.md#3-terminal--shell) ]

- Open up a terminal (Applications->Utilities->Terminal)
- Find out what directory you're in using `pwd`
- You know where you are, but not what's around you. Take a look around with `ls`
- You probably started in your home directory, but just in case, tell the terminal to move to your home directory with `cd ~`. Use `pwd` again to confirm.
- Change into your Projects directory with `cd Projects`. If you don't have one you should create one (see above)
-  Now let's try printing the contents of a file. First we need to create the file. One quick way to do that is with the command `echo "Hello Terminal" >myFile.txt`. We'll explain this command in greater detail in the next lab.
-  Use `ls` to list the contents of your directory after running that command to see what changed.
-  Now show the contents of that new file using the `cat` command.
-  You can use `cat` to print the contents of multiple files; Create another file the same way you created myFile.txt and then print them both together (eg: `cat myFile.txt myFile2.txt`)
-  Using `cat` is fine for small files, or when you just want to print the entire contents of a file, but if you want to read through a large file it's not great. Try using cat on the file `/etc/zshrc`
-  That file's a bit big for `cat`; try viewing it again with `less`. You can move around in `less` using ENTER, SPACE, and your arrow keys. To exit less, press the letter `q`.
-  The last command for you to try out is `grep`. You can use this to search for a pattern in a file or other body of text. Try using it on that first file you created like this: `grep Hello myFile.txt`. Notice that the result is the whole line where the text you searched for occurs. What happens if you use grep to search for something that isn't in the file?

# Part 2

[ [Top](#console-terminal-shell-lab-level-1) | [Home](../README.md#3-terminal--shell) ]

## 2.1 Objectives

[ [Top](#console-terminal-shell-lab-level-1) | [Back](#part-2) | [Home](../README.md#3-terminal--shell) ]

1. After this lab students will know how to create, remove, and modify files and directories using the terminal
3. By completing this lab students will gain exposure to man pages and the use of shell commands with arguments and options.

## 2.2 Overview

[ [Top](#console-terminal-shell-lab-level-1) | [Back](#part-2) | [Home](../README.md#3-terminal--shell) ]

In Part 1 lab you learned to navigate your file system in the terminal. In Part 2 you will learn how to actually make changes to the file system and where to find documentation to get a better grasp on commands you are already familiar with as well as those you haven't seen before. The commands you will practice in this lab are:

- `touch`
- `mkdir`
- `rmdir`
- `rm`
- `cp`
- `mv`
- `<`,`>`,`>>`,`|`

## 2.3 Instructions

[ [Top](#console-terminal-shell-lab-level-1) | [Back](#part-2) | [Home](../README.md#3-terminal--shell) ]

### 2.3.1 Creating files and directories

[ [Top](#console-terminal-shell-lab-level-1) | [Back](#23-instructions) | [Home](../README.md#3-terminal--shell) ]

In lab 1 you learned one way to create a file using the `echo` command and output redirection. That can be useful but there are other methods that make more sense sometimes. Here we'll focus on two other methods:

- the `touch` command.
- file editors.

#### 2.3.1.1 Creating files with touch

[ [Top](#console-terminal-shell-lab-level-1) | [Back](#231-creating-files-and-directories) | [Home](../README.md#3-terminal--shell) ]

To create a file using touch, simply type the command followed by the name of the file you want to create, like this: `touch filename`. Touch is actually meant to update the timestamp on files, but as a side effect it creates files that are named but don't already exist. It's time to practice `touch`ing files

- Use `touch` to create two files, called myfile1 and myfile2
- Try using `touch` to create three more files, but all in the same command. Just give touch the filenames you want one right after the other, separated by a space
- Use the `ls -lT` (that's a lowercase 'L' after the dash) command to see the full timestamps of the files you just created. Notice that the first two are different but the last three are all the same.

#### 2.3.1.2 Editors

[ [Top](#console-terminal-shell-lab-level-1) | [Back](#231-creating-files-and-directories) | [Home](../README.md#3-terminal--shell) ]

There are many text editors out there. In the terminal we will be using `nano`: it has no modes, and the commands you need are always printed along the bottom of the screen. (`^` means hold down `control`.) Here are the `nano` commands we'll use:

- `Ctrl-O` - Write Out; saves the file. `nano` asks for the file name; press `Enter` to accept it.
- `Ctrl-X` - Exit `nano`. If you have unsaved changes it asks "Save modified buffer?": `Y` saves, `N` throws the changes away.
- `Ctrl-K` - Cut the current line.
- `Ctrl-U` - Paste the line you just cut.
- arrow keys - move the cursor around.
- Let's create a file with nano. Start it with a file name: `nano myfile6`
- Type the message "Hello Editor!"
- Save the file with `Ctrl-O` (press `Enter` to accept the name), then exit with `Ctrl-X`. List the contents of your directory to confirm that you created the file, and `cat` it to see what's inside.
- Open that file again with `nano myfile6`. Let's make that message a little more specific: delete the word 'Editor' and replace it with 'nano'. Save the changed file.
- Add a few more lines of text to the file. Then move the cursor to one of them, cut it with `Ctrl-K`, move somewhere else, and paste it back with `Ctrl-U`.
- Save and exit. `cat` the file to check your work.

The [NanoEditor lab](../NanoEditor/README.md) goes further with `nano`, including writing your first Python files with it.

#### 2.3.1.3 Creating directories

[ [Top](#console-terminal-shell-lab-level-1) | [Back](#231-creating-files-and-directories) | [Home](../README.md#3-terminal--shell) ]

- Use `mkdir` to make a directory with your name
- make two more directories inside of that one called "dir1" and "dir2"
- You can make directories in other places than your current directory, without `cd`ing into it, make a directory inside dir1. When you give the location of a file or directory relative to your current position that's called a relative path
- Try making a directory inside dir2 by giving an absolute path. Absolute paths list the exact location of a file -- you've seen this before with the pwd command.

### 2.3.2 Copying, moving, and renaming

[ [Top](#console-terminal-shell-lab-level-1) | [Back](#23-instructions) | [Home](../README.md#3-terminal--shell) ]

- use the `cp` command to copy the file you wrote in the last section. Try using the man file for cp to see what the correct syntax is (anything between [] braces is optional)
- Make a new directory and then move the copied file you just created into that directory using the `mv` command.
- Let's change the name of that file. The `mv` command doesn't have to move a file to a new location; it can simply change the name of the file in place. Change the name to something that starts with a dot (.) such as ".myFile"
- Now check the contents of your directory with `ls`. Where is the file you just renamed? In Linux and Unix systems, files and directories with names starting in "." are hidden, so by renaming your file you actually made it a hidden file. Let's see how we can view hidden files with `ls`
- The `man` command lets you view the man(ual) pages for any command that is documented. Try viewing the man pages for ls, cp, and mv. Once you've looked at each of these and have a feel for how they are laid out, take another look at the ls man page and see if you can figure out how to view hidden files (remember, hidden files begin with a dot '.' ) <sub>**hint**: viewing man pages is like using less; you can move up and down in the file with the keyboard and when you want to exit you can press the 'q' key*</sub>

### 2.3.3 Destroying files and directories

[ [Top](#console-terminal-shell-lab-level-1) | [Back](#23-instructions) | [Home](../README.md#3-terminal--shell) ]

- Make three files and two directories any way you like; create a file inside one of those directories.
- The `rm` command deletes files, try using that on one of the files you created.
- Another way to delete a file is the `unlink` command. Use this to delete the second file.
- Sometimes you want to make sure you are deleting the right files (particularly if you use the * wildcard). use `rm -i` to delete the last file and notice that you have to confirm it before it's deleted.
- Try to delete one of those directories with `rm`. Notice that on its own it won't delete directories.
- Use `rmdir` (or `rm -d`) to delete the empty directory, then try it on the directory with a file in it.
- Directories can only be deleted when they are empty; this could get painful if you have a lot of files and directories inside of one you want to delete. Try deleting that directory again with the `rm -R` command. The `-R` flag tells `rm` to recursively delete the contents of each directory it encounters and then delete the directory.
- **Bonus**: run the command `echo "Hello" >-toughFile` and then try to delete the file created by that command. There are at least two ways to do this.

### 2.3.4 The Art of Redirection

[ [Top](#console-terminal-shell-lab-level-1) | [Back](#23-instructions) | [Home](../README.md#3-terminal--shell) ]

Remember in the previous lab when you typed the command `echo "Hello Terminal" >myfile.txt`? That 'greater than' sign is actually a special character in the shell used for redirecting output to a file. There are several of these operators for redirecting output and input. The main redirection operators to be aware of are as follows:

- `<` - Redirects input to come from the specified file. By default input comes from a stream called STDIN (STandarD INput)
- `>` - Redirects output to the specified file (if the file exists its contents are erased first). By default normal program output is directed to a stream called STDOUT (STandarD OUTput) and errors are directed to a stream called STDERR (STandarD ERRor -- Redirect STDERR using `2>` instead)
- `>>` - Appends output to the specified file instead of overwriting it
- `|` - redirects the output from the previous command to be the input of the next command.
- Use the `find` command to search for all files on your machine with "core' in the name. You can do that with `find / -name core`.
- That's a lot of "Permission denied" errors, and they make it hard to see the useful output from that command. Fortunately that's where output redirection becomes helpful: Those errors all go to STDERR, while the output we want is going to STDOUT. Use the commands above to redirect STDERR to `/dev/null`, effectively throwing away the output from STDERR.
- That's a little better. We want to search for specific core files in this output, so let's redirect STDOUT to a file called `corefiles.log`.
- Next, use `grep` to search for any lines that contain the string 'lib'. We want the search to be case insensitive so we'll use the `-i` flag like so: `grep -i lib corefiles.log` (**note**: your file may have very few lines in it if your computer is rather new and has not had many programs installed yet. It may seem silly to use grep to search for a particular line in a file with only two lines, but when you're searching for an error that occurred only once in over 10000 lines of debugging output you will want to know this tool well.)
- Great, but there's a quicker way to do this without creating a file and running two separate commands. Try using the `|` (pipe) character to redirect the output from `find` to the input for `grep`. Don't forget to throw out the STDERR output; we don't need grep to search through that since we already know it won't contain the files we're looking for.

#### 2.3.4.1 Backgrounding

[ [Top](#console-terminal-shell-lab-level-1) | [Back](#234-the-art-of-redirection) | [Home](../README.md#3-terminal--shell) ]

Did you notice how you had to wait a few seconds every time you ran that find command? Sometimes you may need to use a long-running command and don't want it to lock up your terminal the whole time it's running. That's when you would want to run it in the background (by default, any command you run on a terminal runs in the foreground. Let's play with backgrounding and foregrounding a bit.

- Run that same `find | grep` command that you used in the last step, but add the background operator, `&`, to the end of it. Notice that you immediately get a prompt, but after a few seconds the result of the grep prints to the command line.
- For now we won't worry about that output getting in the way, but this is another good example where you may want to redirect STDOUT to a file.

Now let's practice one more backgrounding technique with a different command.

- Run the command `python3 -m http.server`. This will run forever until you kill it with ~~fire~~ `Ctrl`+`C`
- Now you're stuck without your prompt; but we can fix that! Press `Ctrl`+`Z` to suspend (not kill) that program.
- Now you've got your terminal back, but if you type `jobs` you'll see that python is currently stopped. You can bring it back with `fg`, but that will block your prompt again; instead, use `bg` to resume it in the background.
- Now that you've resumed python in the background, you can see it listed as running in `jobs`. Bring it back to the foreground with `fg` and then kill it with `Ctrl`+`C`

# Part 3

[ [Top](#console-terminal-shell-lab-level-1) | [Home](../README.md#3-terminal--shell) ]

## 3.1 Other Resources

[ [Top](#console-terminal-shell-lab-level-1) | [Back](#part-3) | [Home](../README.md#3-terminal--shell) ]

- For more practice with the basics of the terminal, try the [Command Line Crash Course](http://learnpythonthehardway.org/book/appendixa.html).

- Curious about vim, the other editor you'll see people use? See the vim tour in [zsh-and-vim-guide.md](zsh-and-vim-guide.md), or type `vimtutor` on your command line for a built-in lesson.


## 3.2 Links:

[ [Top](#console-terminal-shell-lab-level-1) | [Back](#part-3) | [Home](../README.md#3-terminal--shell) ]

1. "Often misused" https://en.wikipedia.org/wiki/Cat_(Unix)#Useless_use_of_cat
2. "more or less" http://unix.stackexchange.com/questions/81129/what-are-the-differences-between-most-more-and-less
3. "Command Line Crash Course" http://learnpythonthehardway.org/book/appendixa.html
4. "VIM 101" https://www.linux.com/learn/vim-101-beginners-guide-vim
5. "Oh My Zsh and Powerlevel10k in macOS" https://www.lorenzobettini.it/2024/01/oh-my-zsh-and-powerlevel10k-in-macos/

[ [Top](#console-terminal-shell-lab-level-1) | [Back](#part-3) | [Home](../README.md#3-terminal--shell) ]
