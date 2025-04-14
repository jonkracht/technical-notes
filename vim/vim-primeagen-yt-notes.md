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









Notes from 0 to LSP video:






Remove previous files at ~./config/nvim and ~/.local/share/nvim



Create ~/.config/nvim and enter into it.  

Open vim via `vim .`

You are now in "Netrw", vim's default file tree.

Type `:h rtp` to view README on runtimepath i.e. locations neovim looks for files on startup. 

Create new file with %.

Make init.lua in ~/.config/nvim

Create a new directory with 'd'.

Create a directory named 'lua'.  Any directory inside will be "require-able" by lua.

Inside lua directory, create a new directory named for user say jon
Within this directory, create an init.lua file.
Add `print("Some text here")`

Return to Netrw via `:Ex`
Enter into ~/.config/nvim/init.lua and include `require("jon")`

Make a shortcut to return to Netrw:
Create ~/.config/nvim/lua/jon/remap.lua
```
vim.g.mapleader = " "  # maybe put this in set.lua (later on)
vim.keymap.set("n", "<leader>pv", vim.cmd.Ex)
```

Source current file via `:so`

Require in ./lua/jon/init.lua `require("jon.remap")`




# Plug-in manager

Follow installation instructions on github

Create ./lua/jon/[plug-in-manager-name].lua

Restart vim and source this lua file

Run sync function on the plug in manager




# Install telescope (fuzzy finder)
Into plug-in-manager-name.lua


Create shortcut:
Create folder ./after
Inside after, create plugin directory
Inside plugin, create telescope.lua

Enter
```
local builtin = require('telescope.builtin')
vim.keymap.set('n', '<leader>pf', builtin.find_files, {})
vim.keymap.set('n', '<C-p>', builtin.git_files, {})  # control + p; search git files
vim.keymap.set('n', '<leader>ps', function()
        builtin.grep_string({ search = vim.fn.input("Grep > ") });
end)
```

Source this file.  Leader-pf should now fuzzy find in the current project.



# Add a colorscheme

Goto rosepine's github.  Add via plug in manager in ./lua/jon/[plugin-manager].lua

Indent properly via `=ap`
Source file and sync new plugins.


[8 min]
Enter after/plugin and create colors.lua

```
function Coloring(color)
        color = color or "rose-pine"
        vim.cmd.colorscheme(color)

        vim.api.nvim_set_hl(0, "Normal", { bg = "none" })
        vim.api.nvim_set_hl(0, "NormalFloat", {bg = "none" })

end

Coloring()

```


# Treesitter

Parser tool

Go to Github page.  Go to [plugin-manager].lua

Add Treesitter installation commands.  Sync

If coloring is altered, execute `:lua Coloring()` to restore.

In after/plugin create treesitter.lua.  Paste in configuration from treesitter's github.
In particular, examine `ensure_installed` list.
Make sure "help" and other languages of interest.
Also highlight block to include `enable = true`
Set additional_vim_regex_highlighting = false, auto_install = true

Source the file.
Do something with `:e`.  May need to restart vim for highlighting to take effect.


# Treesitter playground

Treesitter command are accessible via `:TS` prefixes




# Harpoon

Install in lua/jon/[plugin-manager].lua

Create configuration in after/plugin/harpoon.lua

```
local mark = require("harpoon.mark")
local ui = require("harpoon.ui")

vim.keymap.set("n", "<leader>a", mark.add_file)
vim.keymap.set("n", "<C-e>", ui.toggle_quick_menu)

vim.keymap.set("n", "<C-h>", function() ui.nav_file(1) end)
vim.keymap.set("n", "<C-t>", function() ui.nav_file(2) end)
vim.keymap.set("n", "<C-n>", function() ui.nav_file(3) end)
vim.keymap.set("n", "<C-s>", function() ui.nav_file(4) end)
```
Source this file.



# Undotree

Shows a tree of recent changes to a file.

Add to plugin manager and sync.  Create after/plugin/undotree.lua.
Search github for remap.  "vim.keymap.set("n", ...")
Source.


# tpope/vim-fugitive

Git integration.  (Maybe not necessary now).

Create after/plugin/fugitive.lua






# LSP

LSP-Zero
VonHeikemen/lsp-zero.nvim on Github

Follow installation instructions.  Add to plugin manager, source file and update plugins. 

Create config file in after/plugin/lsp.lua

Basic settings:
```
local lsp = require('lsp-zero')

lsp.preset('recommended')
lsp.setup()
```

Prime has some additional personal preferences

Uses mason under the hood





# Other formatting
Remove hello statement from ~./config/nvim/init.lua
Remove hello state from lua/jon/init.lua

Create ~/.config/nvim/lua/jon/set.lua
Add "require("jon.set")" to lua/jon/init.lua

Leader gd should navigation to set.lua

Other configs:  https://github.com/ThePrimeagen/init.lua/blob/master/lua/theprimeagen/set.lua





# Remaps

https://github.com/ThePrimeagen/init.lua/blob/master/lua/theprimeagen/remap.lua

