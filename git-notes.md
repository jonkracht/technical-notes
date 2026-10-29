# Git

## Background

* Distributed version control system for software projects
* Created by Linus Torvalds and first released in 2005
* Some common web servers for hosting git projects are Github, Gitlab, and Bitbucket.



## Config

Print configuration of git repository. 
`git config --list`

Configuration can be set at three scopes:  system-wide, global (meaning user specific), and local/repository.

Global system information is stored in ~/.gitconfig
Local repo information is stored in ./.git/config

`git config --list --show-scope` shows config parameters and at which level they are set.




## Authentication

* Use memory cache to retain Github user name and login
`git config --global credential.helper cache`

* Set time period to use the cache (timeout parameter in units of seconds)
`git config --global credential.helper 'cache --timeout=3600'`




## Basics

Initialize git in a repository:  `git init`

Check status of files in repository:  `git status`	

Include new files to be tracked in repository:  `git add {file1} {file2}`	

Add modified file(s) to staging area:  `git add {file1} {file2}`

Add all changes into staging area:  `git add .`		

Remove a modified file from staging area: `git restore --staged {file}` 

Adds staged changes to a commit with a short description:  `git commit -m “Commit message here”`	

Revert to most recent commit:  `git reset HEAD~1`

Revert to a previous commit definied by a commit hash:  `git checkout {COMMIT_HASH}` or `git revert {COMMIT_HASH}`

(A commit hash is a long string of alphanumeric characters.)

View history of commits:  `git log`		

`git diff <branch-name>`
shows changes in the code



## Branches

Display current branch:  `git branch`

Create new branch:  `git branch -b {branch-name}`

Delete a branch:  `git branch -d {branch-name}`

Move to different branch:  `git checkout <branch-name>`		



## Connect local repository to remote host (i.e. Github)

### Github  
https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github

Summary:
* Initialize tracking, add all files, commit
* Create empty repository on Github (do not create README, LICENSE, or .gitignore)
* Set location where local repository will be pushed:  `git remote add origin {REMOTE-URL}`
* Push changes to remote `git push origin main`

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
Simply Delete .git folder  `rm -rf .git`



## Clone a remote repository

Via https:  `git clone {URL}`

Via ssh:  `git clone  git@github.com:[USER_NAME]/[REPO_NAME].git`
Must have ssh key recognized by the remote repo.

To use ssh key rather than password validation, clone using SSH method.



## Miscellaneous



### Ignore files

Files listed in the .gitignore are explicitly not tracked by the repository.

Because git does not track empty directories, a placeholder file called .gitkeep is inserted.



### Search commit history

Show all commits:  `git log`

Search for string in all tracked files:  `git log --patch  | less +/searching_string`

Find commit that deleted a file:  `git rev-list -n 1 HEAD -- file_path`
Use git show {COMMIT_HASH} to view commit.
