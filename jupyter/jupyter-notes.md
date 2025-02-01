# Jupyter

Name is a combination of Julia, Python, and R (a few languages first implemented)

Successor to IPython (`i` stands for interactive)

Current flavors include Notebook, Lab and Hub.  Notebook version is being deprecated so switch to Lab.





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
Run current cell and move cursor to next cell:  SHIFT + ENTER

ENTER:  Edit mode so as to modify a cell
ESC:  Command mode so as to modify notebook


## Command-mode actions

### Navigation
Move up/down with arrows or vim-style j/k

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
Hold SHIFT + Up/Down  Select multiple cells


### Grouping
SHIFT + M  Merge cells
CTRL + SHIFT + MINUS:  Split active cell at cursor

### Commenting
Highlight code and CTRL + /





## Misc

### Execute shell commands
Prepend command with !
Ex.  `!ls` prints contents of current directory


### Text formatting
Markdown syntax can be used to format text (ex. bold, italics, list, links, etc.)

Color can be control via:  `<font color='green'>Enter text here</font>`

Tabbing can be done by including '\t' in markdown



### Latex
$[LATEX_CODE_HERE]$

### Centering
Centered text:  <center>some text<center>

### Documentation
While cursor is on command, hold SHIFT + TAB
or type `?[FUNCT_NAME]`  

Help:  Type [Command_NAME] followed by ?



### Images

#### Local 
Must be in subpath of notebook i.e. can't be "above" the notebook in the filesystem
`<img src "[/PATH/TO/IMAGE]" />`

#### Remote
`!([/URL/TO/IMAGE])`





## TODO

look into extensions.  puzzle piece on left dock
in settings menu, enable "close brackets" feature
look into jupytext extension to version control only code portions of .ipynb (removes metadata information)
"Show contextual help" to display function descriptions
Look into jupyter_contrib_nb_extensions for autocomplete  and install Hinterland
SHIFT + SPACE brings up function description
to enable autocompletion when editing python files outside of notebook, install jupyterlab-lsp and jedi-language-server
