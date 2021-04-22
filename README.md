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
You need to commit many times per day as to not have a lot of rework. As commiting late in the day with many changes, when git status is typed, you could be in for a shock at the amount of changes you have to work through.
git push to push your file up to the repository.
git pull may get a conflict with files merging.

If so, make the changes to the code, keeping the parts you want, deleteing the 'noise' in the conflict warning. Then:
git add -A
git commit
If a -m "message is not inclueded in the commit of the merge, it will get stuck. To escape type: escape, colon, wq"
esc:wq
After recommitting with a message (-m)
git push 

This is all from Youtube video:
https://youtu.be/0fKg7e37bQE


