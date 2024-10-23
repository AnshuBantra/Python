# Study guide: Git

In any Git project, there are three sections: the Git directory, the working tree, and the staging area. This study guide provides some basic concepts and commands that can help you get started with Git as well as guidelines to help you write an effective commit message.

## Git config command

The Git config command is used to set the values to identify who made changes to Git repositories. To set the values of user.email and user.name to your email and name, type:

: ~$ git config  - -global user.email “[me@example.com](mailto:me@example.com)”

: ~$ git config  - -global user.name “My name”

## Git init command

: ~/checks$ git init

The Git init command can create a new empty repository in a current directory or re-initialize an existing one.

## Git ls -la command

: ~/checks$ ls -la

The Git ls - la command checks that an identified directory exists.

: ~/checks$ ls -l .git/

The ls-l.git command checks inside the directory to see the different things that it contains. This is called the Git directory. The Git directory is a database for your Git project that stores the changes and the change history.

## Git add command

:~/checks$ git add disk_usage.py

Using the Git add command allows Git to track your file and uses the selected file as a parameter when adding it to the staging area. The staging area is a file maintained by Git that contains all the information about what files and changes are going to go into your next commit.

## Git status command

:~/checks$ git status

The Git status command is used to get some information about the current working tree and pending changes.

## Git commit command

:~/checks$ git commit

The .git commit command is run to remove changes made from the staging area to the .git directory. When this command is run, it tells Git to save changes. A text editor is opened that allows a commit message to be entered.

## Guidelines for writing commit messages

A commit message is generally broken into two sections: a short summary and a description of the changes. When the git commit command is run, Git will open a text editor to write your commit message. A good commit message includes the following:

**Summary:** The first line contains the summary, formatted as a header, containing 50 characters or less.

**Description:** The description is usually kept under 72 characters and provides detailed information about the change. It can include references to bugs or issues that will be fixed with the change. It also can include links to more information when relevant.

Click the link to review an example of a commit message: [https://commit.style/](https://commit.style/)
