# Rclone

Enables communication (sync, copy, move) between local and cloud storage.
Similar to the rsync command

[Documentation](https://rclone.org/docs/)



## Setup

Run `rclone config` and follow steps detailed:
https://rclone.org/drive/

Optional:  Create client ID to accelerate communication speed

[Description Here](https://rclone.org/drive/#making-your-own-client-id)

Config file by default is located at `~/.config/rclone/rclone.conf`



## Usage

### List all files in remote (recursive option?)

`rclone lsf [REMOTE_NAME]:`

### List files in directory of remote

`rclone lsf [REMOTE_NAME]:[DIR_NAME]`



### Copy local files to remote

`rclone copy [/PATH/TO/LOCAL/DIR] [REMOTE_NAME]:[/PATH/TO/REMOTE_DIR]`

### Copy remote files to local

`rclone copy [REMOTE_NAME]:[/PATH/TO/FILE_OR_DIR] [/PATH/TO/LOCAL/DIR]`



### Sync local and remote (only changing destination)

`rclone sync [/PATH/TO/LOCAL/DIR] [REMOTE_NAME]:[DIR_NAME]`


#### Useful flags:
* `--track-renames` renames files on remote rather than upload duplicate copies of files that have been renamed; successfully removes deleted local files from remote
*  `--exclude` ignores listed files or directories from operation
* `--exclude-from` flag takes a text file listing files/directories to be excluded from an rclone action
* `--verbose` or `-v` gives prints details to stdout


## Most-used command
* `rclone sync [/LOCAL/PATH/TO/ROOT/FOLDER] [GOOGLE-DRIVE-NICKNAME] --track-renames --exclude-from=.rclone-ignore --verbose`

Execute from /mnt/1-tb-hd/organ/ so can find .rclone ignore
rclone sync /mnt/1-tb-hd/organ/ google-drive-organ: --track-renames --exclude-from=.rclone-ignore --verbose

Fractal implementation:
rclone sync /home/jon/Documents/organ/ google-drive-organ:organ --track-renames --exclude-from=.rclone-ignore --verbose

## TODO
*
