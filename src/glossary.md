---
title: Glossary
---

## A

[Absolute Path](#absolute-path){#absolute-path}

  : A [path](#path) that is fully specified from the filesystem root (in
    Linux and macOS) or the drive (in Windows).

## C

[Command](#command){#command}

  : A statement or instruction which is interpreted and executed by the
    computer.

[Command Prompt](#command-prompt){#command-prompt}

  : In a [shell](#shell), the command prompt is where a user enters
    [commands](#command). It often has some info such as the user name,
    machine (host) name, or [current directory](#current-directory). In
    Linux and macOS, it generally looks like this:

    ```console
    user@host:~/hg2051$
    ```

    And in Windows it looks like this:

    ```console
    C:\Users\user\hg2051>
    ```

[Current Directory](#current-directory){#current-directory}

  : The [directory](#directory) where an executed [command](#command)
    takes place. Any [relative paths](#relative-path) in the command
    begin at the current directory. In a [path](#path), `.` represents
    the current directory.

## D

[Directory](#directory){#directory}

  : A location on a computer's file system that contains a listing of
    files or subdirectories. Synonymous with "folder". Also see [current
    directory](#current-directory) and [parent
    directory](#parent-directory).

## I

[Integrated Development Environment (IDE)](#ide){#ide}

  : A program that combines a [text editor](#text-editor) with other
    tools that aid in software development, such as debuggers or
    integration with a [terminal](#terminal) or [version control
    system](#vcs).

## P

[Parent Directory](#parent-directory){#parent-directory}

  : The [directory](#directory) above the [current
    directory](#current-directory). In a [path](#path), `..` represents
    the parent directory.

[Path](#path){#path}

  : A pointer to a location on a filesystem, similar to how URLs point
    to locations on the internet. For instance,
    `C:\Users\user\Desktop\hello.py` is a Windows path that points to
    the file `hello.py` on the user's desktop. In macOS and Linux, it
    might look similar to `/home/user/Desktop/hello.py`. Also see [absolute path](#absolute-path) and [relative path](#relative-path)

[Platform](#platform){#platform}

  : The kind of operating system used to run some software. Examples
    include Windows, macOS, and Linux. 

## R

[Relative Path](#relative-path){#relative-path}

  : A partial path that begins at the [current
    directory](#current-directory). For instance, `hw1-user/hw1.py` is a
    relative path to the file `hw1.py` in the subdirectory `hw1-user/`
    within the current directory.

## S

[Shell](#shell){#shell}

  : A program that [prompts](#command-prompt) a user for
  [commands](#command), then interprets and executes them on the system
  and returns their output. Examples of shells are Powershell, Bash, and
  zsh.


## T

[Terminal](#terminal){#terminal}

  : A program that handles the interaction between a user and a
    [shell](#shell). Also called a "terminal emulator" or sometimes a
    "console". Examples of terminals are Terminal.app, Windows Console,
    and Visual Studio Code's integrated terminal.

[Text Editor](#text-editor){#text-editor}

  : A program that edits text files. See also [IDE](#ide).

## V

[Version Control System (VCS)](#vcs){#vcs}

  : Software that manages the versions and history of files.
