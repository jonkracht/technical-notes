# lua

Notes from cheat sheet accessed using `curl cht.sh/lua/:learn`

## Comments
* Single line:  Two dashes (--) start line
* Multiline:  Surround text block with --[[ and --]]


## Variables
* Number are doubles

### Strings
* Strings defined by 'text' or "text" are immutable
* Multiline string definition can be accomplished by double brackets [[ text ]]
* Concatenation is accomplished with '..'  ex. 'STRING1' .. 'STRING2'

## if statements

## Loops

### while

### for
```lua
for i = 1, 100 do -- The range includes both ends.
  monkey = monkey + i
end
```


## Input & Output

* Write to stdout:  `io.write('[SOME_TEXT]')`
* Read from stdin:  `io.read()`

## Functions

## Tables

## Modules
* Include contents of another file with 'require' commad
```lua
local mod = require('mod') -- Run the file mod.lua
```

## Miscellaneous
* 
