COMMAND COUNT MOTION


Turn on relative line numbers
Set cursor to be fat

Insert text:  'i' inserts before, 'a' inserts after
Insert text beginning of line  I
Insert text at end of line  A

Create new line and enter insert mode:
Below o (lowercase)
Above O (uppercase)





Visual line mode:  Shift + V


## Command mode actions

Line extremes:
Underscore '_' -> first non-empty character in the line
0 -> beginning of line (i.e. first column)
$ -> to end of line

Find:
Find next instance of a character say (:  f(
Same but navigate just before first instance:  t(

Repeat these processes:  next character instance ;  (semicolon)
                            previous instance ,  (comma)

Navigate to previous character instance:  F( and T(

Now, combine these navigation motions with actions:
df(  deletes from cursor to first instance of (
yf(  yanks from cursor to first instance of (
vf(  highlights

Analogous commands with t instead of f to select until character




## Vertical movements

Move by paragraph (contiguous non-white space):  
{ (up) or }

Jump half page:
Up  CTRL + U
Down  CTRL + D 


Center view:  zz
Perhaps add remap to append 'zz' to CTRL+d/u
`nnoremap("<C-d>", "<C-d>zz")`
(non-recursive remap)

Navigate to top:  gg
Navigate to bottom:  G

Navigate to specific line:  `:[LINE_NUM]`



## Search

Center incremental search matches in screen:
nnoremap("n", "nzzzv")
nnoremap("N", "Nzzzv")


Search forward for character under cursor:  `*`
Increment matches:  Forward `n`, backward `N`
Backward search `#`



## Advanced Motions Part 1

vimbegood game to practice vim cmomands

Delete word and enter insert mode:  `ciW`

Navigation by words:
w jumps forward to start of next word
W same as 'w' but words can contain punctuation marks

e jumps to end of word
E same as 'e' but words can contain punctuation

b jumps backward to start of nearest word
B



Copy everything inside parentheses:  `yi(`  # 'i' stands for inside
Include parentheses `ya(`  # a stands from all

Select entire word:  `viw`



## Advanced Motions Part 2

Correctly indent paragraph `=ap`






## Miscellaneous

Move cursor to matching parenthesis, bracket, curly brace:  %
From normal mode, move to end of word and enter insert mode  ea

While in insert mode, indent line  CTRL + t
De-indent line  CTRL + d

Add line break during insert mode  CTRL + j

Join line with one below separated by a space:  Shift + j

Delete til end of line and enter insert mode  Shift + c

Toggle case of character ~

Indent/deindent:  >>  <<



Telescope is a vim plugin that eases file system navigation
Also, harpoon.




Enter netrw (vim's file manager):  `:Ex`

Create new file:  %
Create new directory:  d

`:so` sources current file



HeRE IS SOME TEXT
And some more
