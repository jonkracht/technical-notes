# Notes on vim/neovim




## Most-used commands

### Navigation
* Words:  w (next word), b (beginning of word), e (end of word)
* Lines:  0 (beginning of line), ^ (first non-blank character in the line), $ (end of line)
* Paragraph:  { (previous), } (next)
* Screen:  H (top of screen), M (middle of screen), L (bottom of screen), CTRL + U (half page up), CTRL + D (half page down)
* File:  gg (beginning of file), G (end of file), specific line of [LINENUM]G
* Next/previous instance of word in file:  *, #

### Writing (e.g. saving a file)
    * `:w` to save and continue working
    * `:w {FILENAME}` to specify a new file name

### Exiting vim
    * Save and quit:  `:wq` (write and quit), `:x` or `ZZ`
    * Quit without saving:  `:q!` or `QZ`

    
### Search 
* Type '/' and enter characters to be search for
* 'n' advances forward through matches; 'N' reverses

### Cut, copy, paste
* Cut (d), copy (y for a word; yy for an entire line), paste before (p) or after (`A`) cursor
* cc:  Delete current line and enter insert mode

### Formatting
 
#### Indenting
* Single line:  in normal mode `>>` and `<<`; in insert mode, CTRL + T and CTRL + D
* Block indent/deindent:  Highlight text in visual mode and press `>` or `<` and then a number of  `.` equal to the desired indentation.

Alternatively, in command mode, type `3>>` to indent lower three lines

When pasting into an indented block, use `]p` to obey local indentation

In insert mode:  `CTRL` + t/d adds/removes indent from beginning of line


#### Block commenting
* Enter Visual-block mode with CTRL + V.  Highlight desired text with navigation keys.  Enter insert mode with SHIFT + I and type commenting character likely (commonly # or %).  Press ESC.
* Remove commenting from a block via CTRL + V, navigation to highlight desired rows and 'x' to delete commenting character

* Added code to init.vim to accomplish:  `,ic` and `,rc` to insert/remove # character



* Sync current vim session to settings in config file (init.vim): 
`source $MYVIMRC`


### Autocomplete
`CTRL + N/P` autocompletes with words in document

 


## Notes from `vimtutor` tutorial

Commands below must be input while in Normal mode which may be entered into by pressing ESC or CTRL + [.  
This enters into Command mode.



### Lesson 1

#### Cursor navigation

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

* Append/add character(s) to the end of a line 
    * From anywhere in desired line:  `A`  (SHIFT + a)





### Lesson 2



| Action | Command|
| --- | ---| 
| Delete entire word under cursor and spaces behind it (see footnote) | `daw`|
| Delete from cursor to end of word| `de` |
| Delete three consecutive words (see additional description below) | `d3w`|
| Delete from cursor to end of line| `d$` or `D` (SHIFT + d)|
| Delete entire line| `dd` |



#### Compound commands

Composed of an operator, a motion and an optional number of repetitions

Some operators include:
| Operator | Description |
| --- | ---|
| d | Delete|



Some motions include: 
| Motion abbreviation | Description |
|---| --- |
| w | Until start of next word excluding its first character|
| e | Until the end of current word including the last character|
| $| Until the end of line including last character|


**Prepending a command with a number repeats the command that many times**

Commands are of the form:

[OPERATOR] [REPETITIONS] [MOTION]

where `[REPETITIONS]` is optional.

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
| "Undo" previous undos (i.e. redo) | CTRL + R|










### Lesson 3

Various editing commands

|Action| Command|
|---|---|
| "Put" (i.e. paste) previously deleted text to cursor's location| `p`|
| Copy text to clipboard| Highlight text and press `y`|
| Replace (or substitute) individual character under cursor| `r` and enter new character|
| Delete to end of word and edit| `ce` and edit as desired|
| Delete to edit of line and edit |`c$` or `C`| 










### Lesson 4

#### Additional cursor navigation

| Action| Command|
|---| ---|
| Navigate to bottom of file| `G` (SHIFT + g)|
| Navigate to top of file| `gg`|
| Navigate to specific line | Enter line number followed by `G`|


#### Searching

| Action| Command|
|---| ---|
| Search forward in document| `/` |
| Search backward in document |  `?` |
| Scroll forward/backward through matches| `n` / `N` |

When finished searching, `CTRL + O` returns cursor to its before-search location.


#### Navigate to matching parenthesis

When cursor is over a parenthesis, `%` will navigate cursor to the matching parenthesis.


#### Substitution

Substitute one piece of text for another.  In the example snippets below, text to be removed is `old` will be replaced by `new`.

|Action | Command|
|---|---|
| First instance in current line| `:s/old/new` |
| All instances in current line| `:s/old/new/g`|
| All instances between two line numbers defined by #'s| `:#,#s/old/new/g`|
| All instances in the document | `:%s/old/new/g` |





### Lesson 5

#### Execute external (shell) commands in Vim
* `:![COMMAND]` 
* Ex:  `:!ls` executes the list command in the current directory


#### Insert file contents into current buffer at location of cursor
`:r {FILENAME}`

#### Insert output of a shell command
`:r !{COMMAND}`  
Ex:  `:r !ls` inserts the directory contents into the active file


#### Write text block to file
* Enter visual mode by pressing 'v' and use cursor to highlight desired text
* Type `:w [FILENAME]`



### Lesson 6


| Action | Command|
|---|---|
| Insert new line below/above cursor and begin editing | `o` |
| Insert new line above cursor and begin editing | `O`|
| Insert text before cursor | `i`|
| Goto beginning of line and enter insert mode | `I`|
| Insert text after cursor| `a`|
| Insert text at end of line| `A`|
| Enter replace mode in which new text overwrites previous content | `R`|



#### Copy ('yank') and paste ('put')
* Highlight text
    * Via mouse drag highlight
    * Via Visual Mode:  Enter visual mode (type 'v') and either
        * Type number of lines to be copied, type direction (k for up, j for down)
        * Use 'j' and 'k' to drag highlight
* `y` yanks/copies the highlighted text
* `p` puts/pastes




#### Set options
* Of the form `:set [FLAG]`
* Some common flags
  * `ic` or `ignorecase`:  Ignore upper/lower case where searching
  * `is` or `incsearch`:  Show partial matches for a search phrase
  * `hls` or `hlsearch`:  High all matching phrases
* Prepend 'no' to turn off (ex. `:set noic`)

* Full list available at:
https://neovim.io/doc/user/options.html

Defined in config (vimrc or init.vim)





### Chapter 7

#### 7.1:  Getting Help
#### 7.2:  Create a Startup Script (making a vimrc file)

#### Autocompletion
* When entering a command, can type `CTRL + D` to see commands that match input letters
* Press `TAB` to autocomplete command (if multiple matches, chooses first alphabetically)



## Miscellaneous
Delete inside characters (parentheses, quotation marks, etc):  `di(`

Toggle character's case (upper/lower):  `~`


## Multiple vim sessions

### Splits

Splitting vim into subsections

| Action | Shortcut |
| --- | --- |
| Create new horizontal split (up/down) | `:split {FILENAME}` or `:sp` |
| Create new vertical split (left/right) |`:vsplit {FILENAME}` or `:vs`|
| Toggle split being edited | Hold CTRL and press w twice|
| Toggle positions of splits | CTRL + W then R |
| Close a split | `:q` |


Define splitting behavior in the vimrc
* Create new splits below/right of existing
`set splitbelow splitright`


### Tabs
`:tab help foo` open help for `foo` in a new tab
:tabedit [FILE] Edit file in new tab
:tabclose
:tabn or tabp Go to next/previous tab OR `gt` or `gT`

Navigate to tab numbered 'n':  `ngt`




### Buffers

Edit another buffer:  `:e {FILENAME}`
Tab completion may be used.

Navigate forward/backward in buffer history:  `:bn`  and `:bp`  (stands for buffer next/previous)

Create an empty buffer:  `:enew`
Must save buffer to a file name before navigating to another buffer

Delete a buffer:  `:bd`



## Plugins

Third-party plugins provide additional functionality to vim.


### vim-plug (plugin manager)
* (Vim-plug)[https://github.com/junegunn/vim-plug]


Install new plugs into neovim:
Add new plug definition into vimrc (init.vim)
In vim, run `:PlugInstall`




### NERDTree

Hotkey set to <Leader> + o

#### Some NERDTree commands
(complete listing shown via `:help NERDTree`)

|Action | Command|
|---|---|
| Toggle quick help menu | `?`|
| Close NT window | `q` |
| Open file | `o` |
| Open file but leave cursor in NT| `go`|
| Open file in a new tab | `t` |
| Open file in new tab but keep focus in NT| `T` |
| Open selected file in a split window| `i` |
| Open in split but leave cursor in NT| `gi`|
| Open in vsplit | `s`|
| Open in vsplit but keep cursor in NT| `gs` |
| Edit current directory | `e` |
| Toggle display of hidden files ON/OFF | `I` |
| Display NT menu | `m` |
| Maximize/minimize window |`A` |




### vimwiki

Open index file `<Leader>ww`

#### Links
[[linkName]]  Creates a file named `linkName`
[[dir/linkName]]  Use folder hierarchy
[[/path/to/link|Description of link]]  Give link a different name than its path 

Tab key navigates to next link; SHIFT + TAB navigates to previous link
Backspace navigates to index file

CTRL/SHIFT + Enter open link in a split

Rename file <Leader>wr



## TODO
* Fix GOYO affecting transparency and colorscheme upon exit


## References

* `vimtutor`
* [MIT Lecture and notes](https://missing.csail.mit.edu/2020/editors/)
* [Cheat sheet](https://devhints.io/vim)
* [Comprehensive cheat sheet](https://vim.rtorr.com/)
