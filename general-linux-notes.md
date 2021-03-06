#### Autostart

Programs that will execute when systems boots
* Specific user: `~/.config/autostart/` directory
* All users:  `/etc/xdg/autostart/`


#### Trash

Trashed files go to `~/.local/share/Trash/`

Can empty via most graphical file managers (eg. nautilus) or by in the terminal with something like:
`rm -rf ~/.local/share/Trash/*`

`trash-cli` is an often-recommended command line utility for trash management.

For removable drives, trash folder is something like:




### Drive mounting

lsblk

Find available drives and their locations
`sudo fdisk -l`

Mount with
`sudo mount [\PATH\TO\DEVICE] [\PATH\TO\MOUNT\POINT]`

May need to specify filesystem type of drive as well.




### Get computer hardware information

Hardware overview:	`lshw`

CPU architecture:  `lscpu`

PCI devices:	`lspci`

Graphics card:	`lspci | grep VGA`
Alternatively:	`lshw -C video`



### Change user shell

First, determine available shells:
`cat /etc/shells` or `chsh -l`


Three methods:

1.)  usermod command

`sudo usermod --shell [/PATH/TO/SHELL] [USER_NAME]`

2.)  chsh utility

`chsh -s [/PATH/TO/SHELL]`


3.)  Edit `/etc/passwd` file

Entries of the form:
[USER_NAME]:x:1000:1000:[FULL_USER_NAME]:[/PATH/TO/USER/HOME]:[/PATH/TO/SHELL]

Locate user of entry for the desired user and edit `[/PATH/TO/SHELL]`
