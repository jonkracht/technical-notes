# terminal notes


## Navigation
Navigate through words in a command:  CTRL + Left/Right Arrow
Navigate to beginning/end of a line:  CTRL + A/E


## Deletion:
Cursor to previous space:  CTRL + W
Cursor to previous punctuation:  ALT + Backspace
Cursor to beginning of line:  CTRL + U
Cursor to end of line:  CTRL + K
Cursor to end of word:  ALT + D

CTRL + L  -or- type 'clear'  Clears terminal screen

Paste most recently deleted text:  CTRL + Y

View more terminal commands with `stty -a`

## Autocomplete 
Begin typing command and hit TAB for available completions


## Run application as a background task
Append '&' to the end of the run command
ex: `gedit &` launches gedit as a background task leaving terminal functional

Send a process to background with CTRL + Z
Bring it back to foreground with 'fg'

Enlarge/shrink terminal text size:
CTRL + SHIFT + PLUS/MINUS



## Navigating the filesystem
cd stands for 'change directory'
`cd`      navigate to user's home directory (ex. /home/USER/)
`cd /`   navigate to root directory
`cd ..`  navigates to parent directory i.e. one level higher in hierarchy
`cd -`    navigates to previous directory

pwd  print working directory
./ : means current directory


## Navigate filesystem using a list of locations
pushd, popd, dirs commands

### Add current location to list
`pushd`

### Add location to list
`pushd [/PATH/TO/DIR]`

### Navigate to entry in list
`pushd +1` 

### Print list of tagged locations
`dirs -v`

### Remove item from list
`popd +1`

### Clear entire list
`dirs -c`


### Path nomenclature
`/` means "start from root directory"
`~` means "start from user's home directory" 
(~ is an alias for /home/[USER_NAME])


## Create new directory
In current folder:  `mkdir dir1 dir2 ...`
At a specific location:  mkdir /path/to/folder/new_folder_name
Create nested folders (recursively):  mkdir -p dir4/dir5/dir6  (-p indicates create parent directories)
Create file with spaces in its name:  mkdir "folder 1" or 'folder 1' or folder\ 3




## ls command
Stands for 'list'

`ls`  lists contents of the current directory
`ls [/PATH/TO/FOLDER]`  lists contents of a specific location
`ls ..`  Show directory contents one level higher
`ls ../..` Show contents of directory two levels higher

`ls > [FILE.TXT]`  saves output of ls command to file

Some flags:
-l  Print one file per line (called a long list)
-a  Show hidden files (file name start with a period)
-h  Display file size in human-readable units (e.g. KiB, MiB, etc.)
-S  Order output by size
-t  Print files by time modified
--time-style

Several aliases containing ls are often defined in bashrc (ll, la, lf)


Similar utilities:
* exa
* tree






## File permissions

Permitted actions for various user types can be controlled independently

Users are classified in one of three groups:
u - user who owns the file 
g - users in the file's group
o - users not in the file's group
a - all users

Actions:
r - read 
w - write
x - execute

'+' adds the desired actions; '-' removes it

`chmod u-w [FILE]`  Removes write permission from user
`chmod u+w [FILE]`  Adds write permission to user

May need sudo privileges

Alternative method:
`chmod [THREE DIGIT NUMBER]`
First digit represent permissions of owner, second the group and third others.
4 stands for read, 2 is write, 1 is execute and 0 is no permission.
Sum desired permissions for each digit.

Ex:  `chmod 751 [FILE]` would grant r/w/x permissions for owner, r/x for groups, etc.




## Ownership
chown (CHange OWNership)
`sudo chown [owner_name]:[group_name] [file_name.txt]`
include -r flag to change all files in this manner

Permission string:
l stands for link
d stands for directory




## cat function
cat (comes from conCATenate):
Default behavior is to write to stdout but can be redirected elsewhere

copy contents of file1 to file2:  
`cat file1.txt > file2.txt`  (if file2 DNE, created; otherwise, overwrite)

Use double greater than (>>) to append contents to end of specified file

Create new file by appending two files together:  
`cat file1.txt file2.txt > combinedfile.txt` (or >> to append)


Wild card characters: ?, *
? represents any single character
* represents any combination of characters

`cat test_?`  prints all files whose names are test_ followed by any single character
`cat test_*`  prints all files whose names test_ followed by zero or more characters

'n' flag will display line numbers in output

### Related functions
`tac` concatenates/prints in reverse order
`bat` cat clone with syntax highlighting and git integration




## Printing to standard output

echo 'Print some text to the standard out.  Yay.'
Text which includes apostrophes mus be enclosed by double quotation marks; \" for double quotes

Include variables:
`my_var=[VAL]; echo "Here is some text $my_var"`
Include functions in a similar manner:  
`echo "Some text $A_FUNCTION"`

Various escape functions enabled with -e option

Create new files with echo:
`echo "Some text." > new_file.txt`
Use '>>' to append to existing file


### Related commands

printf

`column -t` prints are columnated form of text/file

Head/tail commands prints to screen first/last portions of a text document

more, less
Better for larger files.  
Use Up/Down, Page Up/Down and Home/end to navigate.  
'q' to exit

tee command reads from standard input and writes to stdout or file



## File manipulation

Moving files:
`mv [FILE] [/PATH/TO/DIR]`
`mv filename.txt ..` Move to parent directory
`mv [/PATH/TO/DIR]/* .` move everything from DIR to current directory
`mv file1 file2 ... [/PATH/TO/DIR]`  Move multiple files


Rename a file:  Uses the move command
`mv old_name.txt new_name.txt`


Create a copy of a file:
`cp [path/to/file] .`  Creates a copy of [file] in current directory
`cp [path/to/file] [NEW_FILE_NAME]`   Create a copy with new name in pwd


Delete file: 
rm (standing for remove)

`rm [FILENAME]`

Some flags
-i interactive; query user before removing
-p parent; deletes parent directories
-r recursively; deletes folders within desired folder
-f:  force action; doesn't ask for permission

Delete folder:
`rmdir [DIRECTORY]` removes an empty directory
`rm -rf [DIRECTORY]` removes a NON-EMPTY directory




## Searching for files

Find files possessing the desired extension
`find [/ROOT/OF/PATH] -name '*.ext'`


Flags:
name, iname:  Sensitive/insensitive search
type:  f (file), d (directory)
not:  return files not matching criteria
delete:  Remove files matching criteria
or:  Multiple criteria

Perform some action on identified files:
`find {some valid expression} -exec COMMAND {} +`
{} placeholder for the names of located files
'+' indicates end of command




## Chaining commands
* Separate with semi-colon ';'
* Perform command ONLY IF previous succeeds:  Separate with double ampersands &&
* Perform command ONLY IF previous FAIL:  Separate with double pipe symbols ||




Search terminal command history:  
* CTRL + R to enter search
* Type text for which to search
* CTRL + R iterates through matches


history | less :  only displays the first few, with the rest viewable with successive pressing of ENTER

Execute a command returned in history list:  ![commandnumber] where [commandnumber] is returned by history

To not save a command in history, insert a single space before the command
(Also HISTCONTROL must be set appropriately in .bashrc or elsewhere)





Grep:  tool used to find a string in a file or group of files
grep -c "Astring" filename:  counts instances of Astring


Argument of previous command:  !$
!! called a "bang bang":  previously entered command
Use case:  Command fails because super user privilege is needed.  sudo !!

Cycle between arguments or recent commands:  ALT + .


Empty, but not delete, a text file:  > filename

# Terminate a process

For non-responsive process, say.

For a hung terminal process:  `CTRL + C`

Kill by process id (pid):  
Find pid:  `pidof [PROCESS_NAME]` or use `ps -ef` to print all process to debug and located pid; then `kill -15 [PID]`.  If this doesn't work `kill -9 [PID]` terminates immediately.

Terminates all instances of a process:  `killall -9 [PROCESS_NAME]`


Print date:  date; format various ways - date +%D displays MM/DD/YY

Count words:
wc -l TEXT_FILE.txt

Piping (vertical line is called a pipe)
Use a previous command's output and input to a new function
ex. ls ~ | wc -l     Save number of lines return by list files in home directory (~ refers to home directory)
connects standard output (STDOUT) to standard input (STDIN)

sudo - superuser/switch user do


Show network information
ip adr


## Environment variables
`echo $PATH`  print path environment variable
`echo $USER`  print current user
`echo $HOME`  address of home and user

Create new variable:  `newVariable=123abc`
Delete variable:  `unset newVariable`


Create a global variable; can be string, int, etc.
`export [VAR]=[SOME_VAL]`
`unset a_variable`    removes a_variable from being a global variable

To create variables that are saved across sessions/users:
For user:  include definition in ~/.bashrc
For all users:  include definition in /etc/environment 

Display environment variables
env -OR- printenv


*** Text Editors ***
gedit is the default graphical text editor in Ubuntu 20.04

vim
View file:  vim filename.txt
Exit:  Press escape and then :q! (to exit w/o saving) or :wq to (to save) and then Enter
OR
Type "ZZ" t save and quit or "ZQ" to quit without saving

nano is a terminal-based text editor



touch:
Used to update modification times of files.  Can be used to create new files.

Create an empty file
touch file.txt  

Create multiple empty files
touch file1.txt file2.txt




Zip/unzip (compress/decompress):

Single file:

## .gz files

Compressed file will have a .gz extension is appended to the original file name)
Decompress: `gzip -d path/to/file.gz`


gunzip filename.txt.gz

Multiple files zip/unzip or archive:
zip:  
tar cvf new_folder_name.tar file1.txt file.c
unzip:  
tar xvf new_folder_name.tar

View contents of a tar file verbosely
tar tvf [FILE_NAME.tar]



which command returns the location of the binary for a certain software package
whereis is similar but returns a bit more information



Create new aliases in the .bashrc file located at ~/.bashrc

Synchronize current shell to contents of bashrc:
`source ~./bashrc`

Display a list of aliases:
Run 'alias' command in terminal

df command shows disc usage for mounted drives


fzf (FUzzy finder) commands:
CTRL-T, CTRL-R, ALT-C


## Calculator
`bc` basic calculator


Navigate to beginning/end of line:
CTRL + a/e

Print return code of previously executed command:
echo $?

Value of 0 is no error
A non-zero code indicates an error occured

Suppress errors from output by sending to null directory (a black hole of sorts)
[SOME_CODE_HERE] 2> /dev/null

Number 0 represent standin, 1 standout, and 2 stderr




## Getting help or documentation while in the terminal

### man
* Run `man [COMMAND_NAME]` to view official documentation
* Search man page by pressing `/` and typing text to search; scroll through matches with `n`


### cheat.sh

View software cheat sheets curated by cht.sh website
[Documentation](https://github.com/chubin/cheat.sh)


#### General commands
* Info on a UNIX/Linux command:  `curl cht.sh [COMMAND_NAME]`
* May use https protocol if desired
* Retrieve documentation for a keyword:  `curl cht.sh/~[KEYWORD+STRING]`
* Including the `\?T` flag turns off syntax highlight which is useful for exporting to plain text


#### Programming language specific

Use `curl cht.sh/[LANG_NAME]/[FLAG]` where `[FLAG]` can be
* Basic description of programming language:  `curl cht.sh/[LANG_NAME]/:learn`  
* Cheat sheet for a function (like above):  `curl cht.sh/[LANG_NAME]/[FUNCTION_NAME]` ex. tar, curl, cd, etc.
* List all cheat sheets for language:  `curl/cht.sh/[LANG_NAME]/:list`  





### tldr

* Usage:  `tldr [COMMAND_NAME]`
* Periodically run `tldr -u` to sync local install to database


