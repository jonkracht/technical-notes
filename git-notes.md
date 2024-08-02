# Git

* Distributed version control system for software projects
* Created by Linus Torvalds
* Some common web servers for hosting git projects are Github, Gitlab, and Bitbucket.



## Create new repository

First, make new repo on Github
Clone into folder locally
Then add files on local computer and push to remote





## Config

Check configuration of git. Information is stored in ./.gitconfig:
`git config --list`

Configuration can be done at three levels:  system-wide, global (meaning user specific), and local/repository.

`git config --list --show-scope` shows config parameters and from which level they are set.


Repo settings (origin location etc.) are stored in  ./.git/config


## Authentication
Use memory cache to retain Github user name and login
git config --global credential.helper cache

Set time period to use the cache (timeout is in seconds)
git config --global credential.helper 'cache --timeout=3600'

Git configurations (name, email, etc.) is stored in $HOME/.gitconfig





`git init`
Initialize git tracking in a folder

`git status`	
Check for status of files in a repository
Shows edited or newly-added files

`git add file1 file2`	
Adds file1, file2 to tracked files

`git add .`		
Add all changes into staging area


`git commit -m “Message”`	
Adds staged changes to history and described by a short message

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








Connect local repository to Github or other remote destination:
`git remote add origin git@github.com:[GITHUB_USERNAME]/[REPO_NAME].git`
`git branch -M master`
`git push -u origin master`

Check remote origins connected to repo
git remove -v




## Merge  
Integrate a branch's changes into another branch

`git merge <branch_name>`


## Forking
Create a local copy of some other repository



## Push 
Send code out

`git push --set-upstream origin <BRANCH-NAME>`

`git push -u origin <BRANCH-NAME>`



## Pull
Update local repository from a remote counterpart

Good description:  https://stackoverflow.com/questions/71768999/how-to-merge-when-you-get-error-hint-you-have-divergent-branches-and-need-to-s/71774640#71774640

### Fast-forwarding

### Merge

### Rebase



## Pull request
Request main branch of something to download code from you.




## Undo a commit

Revert to most recent commit
`git reset HEAD~1`


Go to a previous point in the code’s development defined by hash
`git checkout {COMMIT_HASH}` or `git revert {COMMIT_HASH}`

where a commit hash is generally a long string of alphanumeric characters













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

