# Package management


## Background

Ways to install software include:
* .deb files (Debian-based distributions)
* .rpm (Red Hat derived distributions)
* ppa (personal package archive)
* snaps
* flatpak
* app images


View installed repos:
`apt policy` or `ls /etc/apt/sources.list.d`


## .deb packages

### Install `.deb` package

Using apt:  Navigate in filesystem to location of .deb and
`sudo apt install ./filename.deb`



## .rpm packages


## snap packages

### Find snaps
* Online at https://snapcraft.io/store
* In terminal: `snap find [PACKAGE_NAME]`

### Install snap packages
`sudo snap install [PACKAGE_NAME]`

### Display snaps installed on system
`snap list`

### Remove
`sudo snap remove [PACKAGE_NAME]`





## PPA 

### Add a PPA to your system
`sudo add-apt-repository ppa:[PPA_NAME]`
`sudo apt install [PPA_NAME]`

### Remove PPA
`sudo add-apt-repository --remove ppa:ppa_name`



## flatpak

Files (including configs) are generally installed into `~/.var/app` 

