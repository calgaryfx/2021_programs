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

At this point the file has been commited to the repository, but is still on my machine.
It is locked into the Repository, but not synced up with my machine.
To sync my machine with github, I need to push my project to the repository.

At Terminal type:
git push

To work with a project from the repository, I have to be in the correct path in Terminal, then type:
git pull
This will pull the file down to my machine.


