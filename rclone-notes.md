# Rclone

Communicate (sync, copy, move) between local and cloud storage from the terminal

[Documentation](https://rclone.org/docs/)

## Configuration

Run `rclone config` and follow steps detailed:
https://rclone.org/drive/

Optional:  Create client ID detailed to accelerate communication speed

[Detailed Here](https://rclone.org/drive/#making-your-own-client-id)

Config file created at `~/.config/rclone/rclone.conf`

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


Useful flags:
* `--track-renames` renames files on remote rather than upload duplicate copies of files that have been renamed; succesfully removes deleted local files from remote
*  `--exclude` ignores listed files or directories from operation
* `--exclude-from` flag takes a text file listing files/directories to be excluded from an rclone action

### TODO
* Is there .gitignore-type functionality?  i.e. files to be excluded can be listed in a text file
