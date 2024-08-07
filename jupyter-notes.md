# Jupyter
name chosen as a combination of Julia, Python, and R, a few of its first languages

Successor to IPython (i stands for interactive)

Current flavors include notebook, lab and hub


## Installation


## Basics

Create an instance:  
`jupyter notebook`  or `jupyter-notebook`

Can only navigate to children folders of location from which notebook was started.
To have access to files across entire file system, first navigate to root directory and launch jupyter notebook.


Exporting notebook to another format:
`jupyter-nbconvert --to='[html, markdown, pdf, latex, etc]' [NOTEBOOK_NAME]`

Alternatively, within notebook, File -> Download As


Run current cell:  CTRL + ENTER
Run current cell and move cursor next cell:  SHIFT + ENTER

ENTER:  enters into edit mode so as to modify a cell
ESC:  enters into command mode so as to modify notebook


## Command-mode actions

### Insert a new cell
a  insert cell above
b  insert cell below

### Convert a cell's type
m  converts active cell to Markdown
y  converts active cell to code

### Deletion
dd  delete active cell
z  undo cell deletion

### Selection
SHIFT + Up/Down  Select multiple cellsi


### Grouping
SHIFT + M  Merge cells
CTRL + SHIFT + MINUS:  Split active cell at cursor

Mass comment/uncomment:
Highlight code and CTRL + /


## Misc

### Execute shell commands
Prepend any shell command with !
Ex.  !ls prints contents of current directory


Formatting can be accomplished via Markdown syntax
(bold, italics, list, links, etc.)

Latex:  $math equations etc.$

Centered text:  <center>some text<center>


Get documentation on a function:
Hold SHIFT + TAB or ?[FUNCT_NAME]  


Color:
<font color='green'>Enter text here</font>

Tabbing can be done by including '\t' in markdown

Help:  Type [Command_NAME] followed by ?



Insert images:

Local (must be in subpath of notebook i.e. can't be "above" the notebook in the filesystem)
<img src "[/PATH/TO/IMAGE]" />

From URL:
!([/URL/TO/IMAGE])
