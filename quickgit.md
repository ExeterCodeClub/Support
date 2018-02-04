### Author: Connor Pettitt
### Date  : 02-02-2018


## A quick guide to git 

**Super short summary:** Git is a tool to keep track of all changes to any chosen files within a chosen folder. Typing `git` into the command line will give you a list of commonly used commands. You can get more in depth help on a command by typing `git <command> --help` (e.g. `git add --help`). This guide is by no means a full introduction to all the features, but they are at the core of what it's all about.

**Basic steps at a glance:** init repo (once), create and edit files, add files to index, commit changes.




**Github:** See [github help](https://help.github.com/) for help using git and connecting to GitHub. Github is one of many free online file storage services that seamlessly integrates with git. To upload files to a remote (internet) GitHub repository using git: find your ssh public key (which git uses to communicate), insert it into your github account, create a repository (storage folder) on your github account, set the upstream connection on your computer's git software to the web address of that repository.


Git is a peice of software you need to have installed on your computer, before you can do anything.

**Windows**: Navigate to the git [website](https://git-scm.com/)  and download the latest version.

**Linux**: Should already be installed on most distributions, otherwise try `sudo apt install git`.

**Mac**: Should be already installed, otherwise check out the [website](https://git-scm.com/).


### Summary
`git init`                  start up a git folder where you are

**If nothing else, remember these two**

`git add <file>`            track changes made to a file in the git folder

`git commit -m "<message>"` store changes made to a file in git (separate from 'saving' a file in the usual sense)


`git clone <url>`           download a remote (online) project

`git pull`                  update your local repository with changes stored on the remote repository, best to run before you makelocal edits

`git push`                  update a remote repository with changes you've made on your local repository


### Basics
#### Initialise
Git allows you to initialise a repository anywhere on your computer using `git init` at the command line, while in the chosen folder (you must navigate to the chosen folder within the command line). A repository is a folder where git can track changes to files. git creates a hidden folder called 'git' or '.git' which will store the tracking information. Once a repo is initialised, you don't need to do it again for the chosen folder or any of its subfolders.

#### Track
Once you have a repository, you can freely go about making edits and creating files. Before you Any files you want to track with each editing session will need to be added to the index with `git add <filename>*` (when you issue a command you must be in the repository.) You may type multiple filenames in one after the other like `git add <f1> <f2> <f3> ...`, or you can track all files with `git add -A`. If you edit the file after adding it to the index, which seems counterintuitive.

#### Commit
When you want git to store changes to a file make sure you have added it first, then use the command `git commit -m "<commit reason>"`. Your commit reason can be anything but make it short. This is called a 'commit', and it could be described as a milestone, because these are the points you can return to if you wish to undo changes.

### GitHub integration 
#### Clone 
GitHub is a place to share projects, and it is quick and simple to grab a copy of that project without any special permissions. This is called cloning, and basically means 'download'. Try finding a github project and locate the 'clone or download' green button. It will give you an https or ssh address, which you can insert into the command `git clone <address>`. If you run it, you will se some download output, and a new folder named after that project's repository.

#### Pull
Git is perfect for collaborating with others but this means they will make changes to the remote repository which you (and your computer) do not yet know about. You will need to use `git pull` to bring those changes in. To pull means to 'update'. Pulling will not overwrite your changes, and in the worst cases it will tell you that there is a conflict to resolve by hand in some files, or won't allow you to pull.

#### Remote
If you want to keep your local repository synchronised with a remote repository, you need to tell your git client where to look online. This is a case of using the command `git remote add origin <url>`. This means to add a new remote which we want to call "origin", which is located at the address <url>. 

#### Push
When you have made and committed changes to your local files, you may then want to push, or upload, onto a remote repository for your own benefit, or to share with others. Use the command `git push`. Pushing requires access permissions to the remote repository, and it will not work if you haven't pulled changes from the remote repository. This would mean the administrator of the repository giving your github account access permissions. You will need to link your github account with your computer's git client by following the GitHub help guide.


