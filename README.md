To sync with Github repository, at Terminal type:
git clone

After some work is done, you can see if it is in the Main at Terminal type:
git status

It should return an untracked file:
Untracked files:
  (use "git add <file>..." to include in what will be committed)
	alien_invasion.py
We are told to use "git add..."

In Terminal type:
git add alien_invasion.py
git status

Terminal should show:
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	new file:   alien_invasion.py

A new file has been uploaded, and it now needs to be committed (as line 21 states):

At Terminal type:
git commit -m "Alien_Invasion game started."

At this point the file has been committed to the repository, but is still on my machine.
It is locked into the Repository, but not synced up with my machine.
To sync my machine with github, I need to push my project to the repository.

At Terminal type:
git push

To work with a project from the repository, I have to be in the correct path in Terminal, then type:
git pull
This will pull the file down to my machine.

Adding files to Repository.
You can add individual files:
git add alien_invasion.py
or, you can add all of them in your directory via two options:
git add .
git add -A

***To make all this work in a typical day, you would start your day by starting the computer, go to the correct directory***:
git pull - This will make all my files up to date with whatever was last worked on by other people.
git add -A   Would be used after modifying your files.
git commit -m    Is need after to commit the changes... It is better each individual file as -m "Can have a clearer description of the changes."
You need to commit many times per day as to not have a lot of rework. As committing late in the day with many changes, when git status is typed, you could be in for a shock at the amount of changes you have to work through.
git push to push your file up to the repository.
git pull may get a conflict with files merging.

If so, make the changes to the code, keeping the parts you want, deleting the 'noise' in the conflict warning. Then:
git add -A
git commit
If a -m "message is not included in the commit of the merge, it will get stuck. To escape type: escape, colon, wq"
esc:wq
After recommitting with a message (-m)
git push

This is all from Youtube video:
https://youtu.be/0fKg7e37bQE

Git Commands:

usage: git [--version] [--help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone     Clone a repository into a new directory
   init      Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add       Add file contents to the index
   mv        Move or rename a file, a directory, or a symlink
   restore   Restore working tree files
   rm        Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect    Use binary search to find the commit that introduced a bug
   diff      Show changes between commits, commit and working tree, etc
   grep      Print lines matching a pattern
   log       Show commit logs
   show      Show various types of objects
   status    Show the working tree status

grow, mark and tweak your common history
   branch    List, create, or delete branches
   commit    Record changes to the repository
   merge     Join two or more development histories together
   rebase    Reapply commits on top of another base tip
   reset     Reset current HEAD to the specified state
   switch    Switch branches
   tag       Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch     Download objects and refs from another repository
   pull      Fetch from and integrate with another repository or a local branch
   push      Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
See 'git help git' for an overview of the system.
