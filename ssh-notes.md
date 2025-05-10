# ssh-notes

## About

Private/public pairs

Types  
* ed25519 (stronger)
* rsa


## Generating ssh keys
`ssh-keygen`

Permissions
(tecmint.com/set-ssh-directory-permissions-in-linux

* Read, write, and execute for the user and not accessbile for user and group (700)
* Set via: `chmod u+rwx, go-rwx ~/.ssh` or `chmod 0700 ~/.ssh`


## Add to ssh-agent

`ssh-add /path/to/private/key`

Also, ensure ssh-agent is autostarted by installation


## Modify repos to use SSH rather than https

`git remote set-url origin git@github.com:jonkracht/technical-notes`


## Config file
Use various ssh keys for various servers

Located at `~/.ssh/config`

Series of entries of the form:
```
Host {Host/server url}
[single space]{path/to/private/ssh/key}
```
