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
