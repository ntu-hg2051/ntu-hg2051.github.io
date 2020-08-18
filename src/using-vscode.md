---
title: Using Visual Studio Code
---

## Getting Started

There is a wealth of introductory information available at
<https://code.visualstudio.com/docs/>, including guides and videos.

In addition, when you start Visual Studio Code and get the welcome
screen, there's a "Learn" section with some interactive ways to learn
about the program from within the program.

## Accepting Assignments

When you receive a link to accept a new homework assignment, you will be
directed to GitHub and it will give you the URL of your newly created
project. Now we can download ("clone") the repository. From the project
page, copy the URL of the Git repository via the green "Code" button:

![*Copy the Repository URL*](static/github-git-url.png)

Now go to Visual Studio Code and pull up the "Command Palette"
(<kbd>F1</kbd> or *View* > *Command Palette*). Type "clone" and select
"Git: clone", then paste the URL you copied and select "Clone from URL".
You may alternatively do "Clone from GitHub" and search for your
repository by typing "ntu-hg2051/" and the name of the repository. In
this case you don't need to get the URL from the project page. Visual
Studio Code will next ask you where to store the repository. This is the
folder into which the repository will be cloned, so you should choose
your "HG2051" folder.

![*Clone the Repository*](static/vscode-git-clone.png)

Once it has downloaded, you'll see its folder in the explorer sidebar.

## Working on Assignments

## Submitting Assignments

When you've saved some files in your assignment, you'll notice the SCM
icon (a Git graph with 3 nodes on the left) has a number in a circle
indicating how many files have been modified. When you're ready to
commit some or all of those changes, click that icon to get the
source-control view. Files with an **M** are "modified", those with
**U** are "untracked" (i.e., new to Git), and those with **D** are
"deleted" (i.e., tracked in Git, but deleted locally). All of these
changes need to be "added" to Git (even deleted files) in order to be
recorded in the repository's history. To add a change, hover your mouse
over a file name and click the `+` icon to stage a change. When you're
finished staging changes, type in a commit message in the "Message" box
and click the checkmark to commit. Once you've made one or more commits,
don't forget to "sync" the commits with GitHub by clicking the
circular-arrow icon at the bottom of the window.

![*Committing and Syncing Changes*](static/commit-and-sync.gif)
