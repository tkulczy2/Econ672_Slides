# Econ672_Slides
Slides composed of material presented in lecture by Matias Cattaneo during Winter 2018

## Getting started with git

### Installation and setup

If you have never used git before, start by following the installation instructions here (Mac OS X may already have git installed):

https://www.atlassian.com/git/tutorials/install-git

Then sign up for a github account if you don't already have one (NOTE: you will need to tell Theo your github username before you add changes to the project):

https://github.com/

Then you can copy all of the files for the project using the following command (do this in the directory where you want to store the lecture slides):

```git clone https://github.com/tkulczy2/Econ672_Slides.git```

In Windows, enter https://github.com/tkulczy2/Econ672_Slides.git as the "Source Location" and enter whatever directory on your computer you want to keep the lecture slides in as the "Target Directory" (must be a new directory).

### Contributing to the slides

After you have done your first `git clone`, follow these general steps to add your notes to the files:

#### Mac/Linux/general command line

* Before you start editing files, *always* do `git pull` first to make sure that you have incorporated changes that other people have already made. You have to be in the "Econ672_Slide" directory when you do this.
* Edit the files as you normally would
* If you create any new files or folders that you want everyone else to have access to, you need to do `git add [filename]` for each one.
* After you have added your new files, you can do `git status` to view information about the changes you have made
* When you are ready to "save your changes to the cloud" so that others can see them, do the following 2 commands:
  -  `git commit -am 'a short message about what changes you have made'`
  -  `git push origin master` (you will need to enter your github username and password after this)

#### Windows GUI

* Before you start editing files, *always* do the following:
  - Select `Remote > Fetch from > origin` (hit "Okay" or "Continue" in the dialog boxes)
  - Select `Merge > Local merge` (hit "Okay" or "Continue" in the dialog boxes)
* Edit the files as you normally would
* When you are done editing files, you just need to click each of the 5 buttons on the lower middle portion of the GUI
  - `Rescan` checks for new and changed files
  - `Stage changed` just prepares to program to use the new/changed files
  - Type a short commit message, then `Sign off` adds your personal info to the end of the message
  - `Commit` saves all of your changes (other people still can't see them though)
  - `Push` sends your changes to the repository on the cloud so others can see/use them (you will need to enter your github username and password after this).

## Want to learn more?

There are tons of other tutorials. Using git is very helpful for managing code, so it's good to start learning it now!

### Command line

This website has a decent (brief) explanation of what git does, and what each of the commands mean:

https://codio.com/docs/ide/editing/git/git-primer/

This website explains how to configure git so that you don't have to enter your github username and password every time you push changes to the repo (you might need to remove "-user1" everywhere in these instructions, and don't enter a password after `ssh-keygen`):

https://www.keybits.net/post/automatically-use-correct-ssh-key-for-remote-git-repo/

### Windows GUI

This seemse like a decent resource for doing basic stuff on Windows:

https://code.tutsplus.com/tutorials/git-on-windows-for-newbs--net-25847

## If git is too much trouble at the moment...

If right now isn't the best time in your life for the headache of figuring out how to use git, then just pick a lecture, download that .tex file from this website, edit it to your heart's content, and then send it to Theo or post it on Slack. I'll take care of the rest.
