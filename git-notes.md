# Git

* Distributed version control system for software projects
* Created by Linus Torvalds and first released in 2005
* Some common web servers for hosting git projects are Github, Gitlab, and Bitbucket.



## Config

Check configuration of git. Information is stored in ./.gitconfig:
`git config --list`

Configuration can be set at three scopes:  system-wide, global (meaning user specific), and local/repository.

`git config --list --show-scope` shows config parameters and from which level they are set.


Repo settings (origin, location, etc.) are stored in `.git/config`


## Authentication

* Use memory cache to retain Github user name and login
`git config --global credential.helper cache`

* Set time period to use the cache (timeout parameter in units of seconds)
`git config --global credential.helper 'cache --timeout=3600'`




## Basics

Initialize git tracking in a repository:  `git init`

Check status of files in a repository:  `git status`	

Include files to be tracked in repository:  `git add {file1} {file2}`	

Add changes in specific files to staging area:  `git add {file1} {file2}`

Add all changes into staging area:  `git add .`		

Remove a modified file from staging area: `git restore --staged {file}` 

Adds staged changes to commit described by a short description:  `git commit -m “Commit message here”`	

Revert to most recent commit:  `git reset HEAD~1`

Rever to a previous commit definied by a commit hash:  `git checkout {COMMIT_HASH}` or `git revert {COMMIT_HASH}`

(A commit hash is generally a long string of alphanumeric characters.)

View history of commits:  `git log`		

`git diff <branch-name>`
shows changes in the code



## Branches

Display current branch:  `git branch`

Create new branch:  `git branch -b {branch-name}`

Delete a branch:  `git branch -d {branch-name}`

Move to different branch:  `git checkout <branch-name>`		



## Connect local repository to remote location such as Github 

### Github  
https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github

Summary:
* Initialize tracking, add all files, commit
* Create empty repository on Github (do not create README, LICENSE, or .gitignore)
* Set location where local repository will be pushed:  `git remote add origin {REMOTE-URL}`
* Push changes to remote via `git push origin main`

Alternatively:
* Create new repo on Github
* Clone locally
* Add files to be included in repo
* Push back to Github



## Merge  
Integrate a branch's changes into another branch

`git merge <branch_name>`


## Fork
Create a local copy of some other repository



## Push 
Send code to a remote repository

`git push --set-upstream origin <BRANCH-NAME>`

`git push -u origin <BRANCH-NAME>`



## Pull
Update local repository from some remote counterpart

Good description:  https://stackoverflow.com/questions/71768999/how-to-merge-when-you-get-error-hint-you-have-divergent-branches-and-need-to-s/71774640#71774640



Methods to handle merge conflicts between local and remote versions of the repository.

### Fast-forwarding

### Merge

### Rebase



## Pull request
Request remote branch to download code from you.






## Remove git tracking
Delete .git folder:  `rm -rf .git`



## Clone a remote repository

Via https:  `git clone {URL}`

Via ssh:  `git clone  git@github.com:[USER_NAME]/[REPO_NAME].git`
Must have ssh key recognized by the remote repo.

To use ssh key rather than password validation, clone using SSH method.



## Miscellanehous



### Ignore files

Files listed in the .gitignore are explicitly not tracked by the repository.

Because git does not track empty directories, a placeholder file called .gitkeep is inserted.



### Search commit history

Show all commits:  `git log`

Search for string in all tracked files:  `git log --patch  | less +/searching_string`

Find commit that deleted a file:  `git rev-list -n 1 HEAD -- file_path`
Use git show {COMMIT_HASH} to view commit.
