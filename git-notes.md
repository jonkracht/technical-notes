# Git

* Distributed version control system for software projects
* Created by Linus Torvalds
* Some common web servers for hosting git projects are Github, Gitlab, and Bitbucket.



## Config

Check configuration of git. Information is stored in ./.gitconfig:
`git config --list`

Configuration can be set at three levels:  system-wide, global (meaning user specific), and local/repository.

`git config --list --show-scope` shows config parameters and from which level they are set.


Repo settings (origin, location, etc.) are stored in  ./.git/config


## Authentication

* Use memory cache to retain Github user name and login
`git config --global credential.helper cache`

* Set time period to use the cache (timeout parameter in units of seconds)
`git config --global credential.helper 'cache --timeout=3600'`




## Basics

`git init`
Initialize git tracking in a repository

`git status`	
Check for status of files in a repository

`git add {file1} {file2}`	
Adds files to those to be tracked

`git add {file1} {file2}`
Add changes in specified to files to staging area

`git add .`		
Add all changes into staging area


`git commit -m “Message”`	
Adds staged changes to history and described by a short message

## Undo a commit

Revert to most recent commit
`git reset HEAD~1`


Go to a previous point in the code’s development defined by hash
`git checkout {COMMIT_HASH}` or `git revert {COMMIT_HASH}`

where a commit hash is generally a long string of alphanumeric characters
`git log`		



View history of commits

`git diff <branch-name>`
shows changes in the code





## Branches


Display current branch
`git branch`				

Create new branch
`git branch -b {branch-name}`

Delete a branch
`git branch -d {branch-name}`

Move to different branch
`git checkout <branch-name>`		








## Connect local repository to Github or other remote destination:

### Github  
https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github

Summary:
* Initialize tracking, add all files, commit
* Create empty repository on Github (do not create README, LICENSE, or .gitignore)
* Set location where local repository will be pushed:  `git remote add origin {REMOTE-URL}`
* Push changes to remote via `git push origin main`





## Merge  
Integrate a branch's changes into another branch

`git merge <branch_name>`


## Forking
Create a local copy of some other repository



## Push 
Send code out often to a remote repository

`git push --set-upstream origin <BRANCH-NAME>`

`git push -u origin <BRANCH-NAME>`



## Pull
Update local repository from some remote counterpart

Good description:  https://stackoverflow.com/questions/71768999/how-to-merge-when-you-get-error-hint-you-have-divergent-branches-and-need-to-s/71774640#71774640


### Fast-forwarding

### Merge

### Rebase



## Pull request
Request remote branch to download code from you.

















## Remove git tracking
Navigate to repo and delete .git directory via `rm -rf .git`



## Download a copy of a repository
git clone https://some.url.com
or
via ssh

Note: To use ssh key rather than password validation, clone using SSH rather than HTTPS
Ex.  git clone  git@github.com:[USER_NAME]/[REPO_NAME].git



## Ignore files

Create a file named ".gitignore" in the repo and list file names to ignore

