## Autostart

Programs executed on system boot
* Specific user: `~/.config/autostart/` directory
* All users:  `/etc/xdg/autostart/`


## Deletion of files and directories

Linux default is the `rm` command
Files are completely removed so no safeguards for user error


### trash-cli

`trash` or `trash-put` to send file to trashcan, by default located at `~/.local/share/Trash/`

`trash-rm /path/to/directory` trashes all files within directory 

`trash-list` to display trashcan contents
Alternatively, nautilus and perhaps other graphical file managers provide a sidebar icon to quickly display trash contents.

`trash-restore` to return a trashed file to its previous location

`trash-empty` to permanently delete trash contents
Alternatively `rm -rf ~/.local/share/Trash/*`








## Drive management (mounting, information, etc.)

lsblk:  List information about block devices

Find available drives and their locations
`sudo fdisk -l`

Mount with
`sudo mount [/PATH/TO/DEVICE] [/PATH/TO/MOUNT/POINT]`

May need to specify filesystem type of drive as well.




## Get computer hardware information

Hardware overview:	`lshw`

CPU architecture:  `lscpu`

PCI devices:	`lspci`

USB devices:  `lsusb`

Graphics card:	`lspci | grep VGA`
Alternatively:	`lshw -C video`



## Change user shell

First, determine available shells:
`cat /etc/shells` or `chsh -l`


Three methods:

1.)  usermod command

`sudo usermod --shell [/PATH/TO/SHELL] [USER_NAME]`

2.)  chsh utility

`chsh -s [/PATH/TO/SHELL]`


3.)  Edit `/etc/passwd` file

Entries are of the form:
`[USER_NAME]:x:1000:1000:[FULL_USER_NAME]:[/PATH/TO/USER/HOME]:[/PATH/TO/SHELL]`

Locate entry for the desired user and edit `[/PATH/TO/SHELL]`



## Group Management

### Display groups of which user is a member
* `groups [USER_NAME]`
* `id -nG [USER_NAME]`

### Add user to a group
sudo usermod -a -G [GROUP_NAME] [USER_NAME]

### Remove user from a group
`gpasswd -d [USER_NAME] [GROUP_NAME]`





## Power management

Controlled by gsettings

Get values of all gsettings:  `gsettings list-recursively`


Set:  `gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-battery-type 'shutdown'`

For power, can set inactive timeout period, lid close action, function to perform when timedout, can choose different actions for times when computer is on AC power or battery




## Creation of the bashrc

Template bashrc is contained in `/etc/skel`
All files in this directory are copied to a new user's home directory when the account is created.
These template files are somewhat distribution specific.





## Disk usage

### df (stands for Disc Free) 
Gives overview of file system disk usage.  Defaults to all mounted file systems but can be tailored by passing a path.

Entries include size, used/available space, mount point

Some flags:
* h: drives sizes shown in human-readable units
* T: include drive type in output
* x: exclude file systems of specified type from output



### du (stands for Disc Used)
Disk usage for individual directories

Some flags:
* h for human-readable units
* --max-depth 
* s for a summary


### ncdu
Pretty front-end to `du`




## watch
Execute command repeatedly and print its output.


## .desktop files

Use `desktop-file-validate` to check for errors in .desktop file 

User's files are in `~/.local/share/applications` and system-wide are in `/usr/share/applications`

After modifying .desktop file, run `sudo update-desktop-database` to alert system to changes

Include `StartupWMClass` to show correct icon (not gear) when exploding open apps
