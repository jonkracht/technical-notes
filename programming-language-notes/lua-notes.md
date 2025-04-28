# lua

Reference manual:  https://www.lua.org/manual/

Notes from cheat sheet accessed using `curl cht.sh/lua/:learn`

REPL can be accessed from the command line via `lua`


## Datatypes
* nil
* Boolean
* number
* string
* table
* function
* userdata
* threads 

`type(var)` commands returns datatype of a variable



## Comments
* Single line:  Two dashes (--) start line
* Multiline:  Surround text block with --[[ and --]]


## Variables

* By default, variables are global in scope.
* Create local variable via `local var = 3`
* Unset a variable via `var = nil`




### Strings

* Strings (defined via `var ='text'` or `var = "text"`) are immutable
* Multiline string definition can be accomplished by double brackets [[ text ]]
* Concatenate strings (use two periods): `STRING1 .. STRING2`
* String length is given by hash symbol:  `print(#'Hello World') -- 11 chars`


## if/elseif/else statements

``` lua
if num > 40 then
  print('over 40')
elseif s ~= 'walternate' then  -- ~= is not equals.
  -- Equality check is == like Python; ok for strs.
  io.write('not over 40\n')  -- Defaults to stdout.
else
  -- Variables are global by default.
  thisIsGlobal = 5  -- Camel case is common.

  -- How to make a variable local:
  local line = io.read()  -- Reads next stdin line.

  -- String concatenation uses the .. operator:
  print('Winter is coming, ' .. line)
end
```



## Loops

### while

``` lua
while num < 50 do
  num = num + 1  -- No ++ or += type operators.
end
```

### repeat

### for

```lua
for i = 1, 100 do -- Range includes both ends .
  monkey = monkey + i
end
```


## Input & Output

* Write to stdout:  `io.write('[SOME_TEXT]')`
* Read from stdin:  `io.read()`





## Functions

```lua
function fib(n)
  if n < 2 then return 1 end
  return fib(n - 2) + fib(n - 1)
end
```

Can pass an arbitrary number of parameters to a function using an ellipsis
`local some_function = function(...)`


## Tables

Lua's only compound data structure.  They are associative arrays.

### Definition


`t = {key1 = 'value1', key2 = false}`

Have string keys by default.
Access values with dot notation:  `print(t.key1)`


### Modify contents
Add new key/val pair:  `t.newKey = {}`
Remove key from table:  `t.key2 = nil`


### Iterating over table's key/val pairs
``` lua
for key, val in pairs(u) do
  print(key, val)
end
```

Difference between pairs and ipairs?


### Using table as a list/array

```lua
v = {'value1', 'value2', 1.21, 'gigawatts'}
for i = 1, #v do  -- #v is the size of v for lists.
  print(v[i])  -- Indices start at 1 !! SO CRAZY!
end
-- A 'list' is not a real type. v is just a table
-- with consecutive integer keys, treated as a list.
```




## Metatables


## Class-like tables



## Modules

Include contents of another file with 'require' command
`local mod = require('mod') -- Run the file mod.lua`

## Miscellaneous
* Assert command exists
* `_G` is a special table of all globals 
