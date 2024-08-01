# ssh-notes

## About

Private/public pairs

Types:  ed25519 (stronger), rsa


## Generating ssh keys
ssh-keygen


## Add to ssh-agent
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
