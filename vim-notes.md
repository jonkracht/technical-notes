# vim

## References
* vimtutor
* 


## TLDR (or most commonly-used  commands)

* Navigation
  * Move to beginning/end of line:  `0` / `$`
  * Move backward one word:  `b`
* Writing (eg. saving file)
    * `:w` to save and continue working
    * `:w [FILENAME]` to specify a new file name
    * `ZZ` to save and exit
* Exit
* Search:  Type '/' and characters of interest; 'n' advances through matches; 'N' reverses through matches
* Cut (d), copy (y for a word; yy for an entire line), paste (p)

Sync vim with settings in config file (init.vim): 
Type ':' and then:  source $MYVIMRC


* Begin a new paragraph above/below: `o` / `O`





## Notes from `vimtutor` tutorial

All commands below must be input while in Normal mode which may be entered into by pressing ESC.

### Lesson 1

#### Cursor navigation


* Navigate left/down/up/right with hjkl keys

* Navigate up/down by one half of a page:  `CTRL` + `u` / `d`

* Navigate up/down a paragraph:  `{` or `}`




#### Exit vim
* Exit without saving changes:  `:q!`
* Save changes and exit:  `:wq` or `ZZ`


#### Text editing

* Delete a character  
    * Move cursor over the character to be deleted and press `x`

* Insert character mid-line
    * Navigate cursor to desired location of new text.  Press `i` and type begin adding text.


* Insert character(s) at the end of a line (appending)  
    * From anywhere in desired line:  `A`  (SHIFT + a)





### Lesson 2



| Action | Command|
| --- | ---| 
| Delete entire word under cursor (see footnote) | `daw`|
| Delete from cursor to end of word| `de` |
|Delete three consecutive words (see additional description below) | `d3w`|
| Delete from cursor to end of line| `d$` or `D` (SHIFT + d)|
| Delete entire line| `dd` |

* vimtutor's description of the command does not match its behvaior in curret install



#### Compound commands

Composed of an operator, a motion and an optional number of repititions.

Some operators include:
| Operator| Description|
|--- | ---|
|d| Delete|



Some motions include: 
| Motion| Description|
|---| --- |
|w| Until start of next word excluding its first character|
|e | Until the end of currect word including the last character|
|$| Until the end of line including last character|


**Prepending a command with a number repeats it that many times**

Commands are of the form:

`[OPERATOR]` `[REPITITIONS]` `[MOTION]`

where `[REPITITIONS]` is an optional modifier.

Examples of navigating by count and motions:

| Action| Command|
|---| ---|
|Move cursor forward by two words |  `2w` |
|Move cursor backward by three words| `3b`|
|Move cursor to end of third word forward|  `3e`|








#### Undo and redo
| Action | Command|
|---|---|
| Undo last command | `u`|
| Return entire line to previous state| `U` (SHIFT + u)|
| "Undo" previous undo's (i.e. redo) | CTRL + R|










### Lesson 3

Various editing commands

|Action| Command|
|---|---|
|Put (i.e. paste) previously deleted text (stored in Vim register) to location of cursor| `p`|
|Copy text to system clipboard| Highlight text and press `y`|
|Replace (or substitute) individual character under cursor| `r` and enter new character|
|Delete to end of word and edit| `ce` and edit as desired|
| Delete to edit of line and edit |`c$` or `C`| 










### Lesson 4

#### Additional cursor navigation

| Action| Command|
|---| ---|
|Navigate to bottom of file| `G` (SHIFT + g)|
|Navigate to top of file| `gg`|
|Navigate to specific line | Enter line number followe by `G`|


#### Searching


| Action| Command|
|---| ---|
|Search forward/backward in document| `/` / `?` |
|Cycle forward/backward through matches| `n` / `N` |

When finished searching, `CTRL + O` returns cursor to its pre-search location.


#### Navigate to matching parenthesis

When cursor is over a parenthesis, `%` will navigate cursor to the matching parenthesis.


#### Substitution

Substitute one piece of text for another.  In the example snippets below, text to be removed is `old` will be replaced by `new`.

|Action | Command|
|---|---|
| First instance in current line|`:s/old/new`|
| All instances in current line| `:s/old/new/g`|
| All instances between two line numbers defined by #'s| `:#,#s/old/new/g`|
| All instances in the document | `:%s/old/new/g`|













### Lesson 5

#### Execute external (shell) commands
* `:![COMMAND]` 
* Ex:  `:!ls` executes the list command in the current directory

#### Insert contents of file
`:r [FILENAME]`

#### Insert output of a shell comand
`:r ![COMMAND]`  
Ex:  `:r !ls` inserts the directory contents into the active file


#### Write block of text to file
* Select desired textblock with cursor (will have entered Visual mode)
* Type `:w [FILENAME]`







### Lesson 6


|Action | Command|
|---|---|
| Insert new line below/above cursor and begin editing | `o` / `O` |
|Insert text after position of cursor| `a`|
|Insert text at end of line| `A`|
|Enter replace mode where new existing text is ovewritten | `R`|


#### Copy ('yank') and paste ('put')
* Highlight text to be copied via mouse or Visual mode
* `y` yanks/copies the highlighted text
* `p` puts/pastes




#### Set options
* Of the form `:set [FLAG]`
* Some common flags
  * `ic` or `ignorecase`:  Ignore upper/lower case where searching
  * `is` or `incsearch`:  Show partial matches for a search phrase
  * `hls` or `hlsearch`:  High all matching phrases
* Prepend 'no' to turn off (ex. `:set noic`)
* Can make these preferences default by including into `vimrc`/`init.vim`





### Chapter 7

7.1:  Getting Help
7.2:  Create a Startup Script (making a vimrc file)

#### Autocompletion
* When entering a command, can type `CTRL + D` to see commands that match input letters
* Press `TAB` to autcomplete command (if multiple matches, chooses first alphabetically)







Notes form Luke Smith's Vim Diesel Youtube Video:
.  reruns previous command

Reload neovim with newly-edited vimrc:
:source $MYVIMRC



## Plugins:

### vim-plug
nerdtree:  CTRL-O to toggle ON/OFF nerd tree (file manager)



How to install new plugs into neovim:
Add new plug definition into vimrc (init.vim)
In vim, run :PlugInstall


## References

* `vimtutor`
* 
