# Notes regarding package management

## Background
Ways to install software include:
* .deb
* PPA (personal package archive)
* Snaps
* Flatpak 


Distro repos - defined in /etc/apt/sources.list

List enabled repos:
apt policy
-or-
ls /etc/apt/sources.list.d


## .deb packages

Install `.deb` package

* Using apt
Navigate in terminal to location of file and run
`sudo apt install ./filename.deb`




## snap packages

Snap is a packaging system use to bundle software.

Find snaps:
* Online at https://snapcraft.io/store
* Terminal via `snap find [PACKAGE_NAME]`

Install snap packages
`sudo snap install [PACKAGE_NAME]`

Display snaps installed on system:
`snap list`

Remove  
`sudo snap remove [PACKAGE_NAME]`





## PPA 

Adding a PPA to your system
`sudo add-apt-repository ppa:[PPA_NAME]`
`sudo apt install [PPA_NAME]`

Remove PPA
`sudo add-apt-repository --remove ppa:ppa_name`

