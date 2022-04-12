** TLDR section **

Saving:  'w:' to save and continue working; 'ZZ' to save and exit
Exit:  
Search:  Type '/' and characters of interest; 'n' advances through matches; 'N' reverses through matches
Cut (d), copy (y for a word; yy for an entire line), paste (p)

Sync vim with settings in config file (init.vim): 
Type ':' and then:  source $MYVIMRC





Chapter 1:

Navigating with hjkl:
   ^
   k
<h   l>
   j
   v

Jump up/down half a page:  CTRL + u / d

Jump up/down a paragraph:  { or }



Enter NORMAL mode by pressing ESC

Exit vim:
Discard changes :q! or Z then Q
Save changes :wq or Z then Z


Save while editting (i.e. don't exit):  :w

Delete a character:  x
Move cursor over the character to be deleted and press x

Insert character mid line:  i
Navigate cursor to desired location of new text
Press 'i' and type additions


Insert character end of line (appending):  A  (Shift + a)
Navigate cursor anywhere in line of which additions are to be added
Press SHIFT + a (e.g. capital A) and type additions

--- OR ---

Navigate to end of line and press 'a'



Start new paragraph below/above:  o or O



Lesson 2 - Deletion commands

Delete a word:
Navigate to first character of word to be deleted and type 'dw'

Delete to end of line:
Navigate to left-most character to be deleted and type 'd$' or simply 'D' 

Delete from cursor to end of word:
Type 'de'


Typing a number with an operator repeats it that many times


Navigating by count and motions:

Move two words forward:  2w
Move end of third word forward:  3e
Move to start of line:  0

Move backward a word: b

Delete consecutive words:
Navigate to beginning of first word to be deleted and type d3w

Delete an entire line:
dd  -OR- 2dd to delete two lines etc.



Undo and redo actions:
u undoes last command
U returns line to its original state
CTRL + R to undo previous undo's




Lesson 3

Paste a deleted segment with 'p'

Copy text to system clipboard:  
Highlight and press 'y'

Replace a character with 'r' and new character

Replace end parts of a word:  Type 'ce' and then characters to be added

Change til end of word:  cw
Change til end of line:  c$

Delete til end of line and insert:  C





Lesson 4

Cursor Location:
CTRL + g gives filename and line number within file
G navigates to bottom of the file
gg navigates to start of the file
LINE_NUM + G navigates to LINE_NUM


SEARCH:

Typing  /  followed by a phrase searches FORWARD for the phrase.
Typing  ?  followed by a phrase searches BACKWARD for the phrase.

After a search type  n  to find the next occurrence in the same direction
or  N  to search in the opposite direction.

CTRL-O takes you back to older positions, CTRL-I to newer positions.

Navigate to parentheses mate:  %


Subsitution:

To substitute new for the first old in a line 	:s/old/new
To substitute new for all 'old's on a line 	:s/old/new/g
To substitute phrases between two line #'s 	:#,#s/old/new/g
To substitute all occurrences in the file 	:%s/old/new/g
To ask for confirmation each time add 'c'       :%s/old/new/gc



Lesson 5

Execute external (shell?) commands by :![SHELL_CMD]
Ex.  :!ls displays contents of current directory

Save file:  
:w FILE_NAME

Select a block of text with 'v'

Save block of text to file:
Highlight using 'v'
Type ':' and then w FILE_NAME

Insert text from a file:
:r FILENAME



LESSON 6

  1. Type  o  to open a line BELOW the cursor and start Insert mode.
     Type  O  to open a line ABOVE the cursor.

  2. Type  a  to insert text AFTER the cursor.
     Type  A  to insert text after the end of the line.

  3. The  e  command moves to the end of a word.

  4. The  y  operator yanks (copies) text,  p  puts (pastes) it.

  5. Typing a capital  R  enters Replace mode until  <ESC>  is pressed.

  6. Typing ":set xxx" sets the option "xxx".  Some options are:
        'ic' 'ignorecase'       ignore upper/lower case when searching
        'is' 'incsearch'        show partial matches for a search phrase
        'hls' 'hlsearch'        highlight all matching phrases
     You can either use the long or the short option name.

  7. Prepend "no" to switch an option off:   :set noic





Alternative method:
Select text in Visual mode (mode or keyboard)
Enter 'y' to yank (copy) text
Move to new location and enter 'p'





LESSON 7

7.1:  Getting Help
7.2:  Create a Startup Script (making a vimrc file)
7.3:  Autocompletion






Notes form Luke Smith's Vim Diesel Youtube Video:
.  reruns previous command

Reload neovim with newly-edited vimrc:
:source $MYVIMRC



Plugins:

nerdtree:  CTRL-O to toggle ON/OFF nerd tree (file manager)



How to install new plugs into neovim:
Add new plug definition into vimrc (init.vim)
In vim, run :PlugInstall
