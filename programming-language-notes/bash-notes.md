# bash

## General
Primarily a scripting language
Commands used in a text editor NOT directly in terminal

Convention is to give bash scripts a .sh extension

The !# (shebang) at the beginning of the file defines which interpreter is to be used.

Most common is `#!/bin/bash`

Alternatively, use the 'env' executable to locate first instance of bash in the PATH:  `#!/usr/bin/env bash`

Available shells are listed in `/etc/shells`




File must be exectuable.
`chmod a+x /path/to/file.sh`
May need to execute with sudo privileges

Alternatively, use three digit syntax:  `chmod 755 /path/to/file.sh`
(read = 4, write = 2, execute = 1; sum desired permissions; first entry owner, second group, third others)

Print to stdout via `echo` commands
Include -n flag to not print new line at end of output.



## Variables

* Create a variable
`myvar='Monkies'`     (no spaces allowed)

Convention is to use lowercase for variable names so as not to conflict with system variables.

Variable contents are accessed by prepending their name with $
ex.  `$myvar`




## Arrays
1 dimensional data structure

### Create array 
`newArr=('thing1' 'thing2')`
(BASH is fairly picky about spaces before/after equals sign)

### Delete element(s) of array
`unset newArr[2]`

### Printing elements

Single element:  `echo "${newArr[1]}"`
All elements (@ represents all):  `echo "${newArr[@]}"`
Print indices:  `echo "${!newArr[@]}"`
Print length of array (#):  `echo "${#newArr[@]}"`




## Input
Use "read" function to query user for input.
`read variable_name`

Include a prompt in the query:
`read -p "Text to input a variable: " [variable_name]`




## Logic

### IF/THEN

Syntax:
```
if [ logical statement ]
then 
    some action
elif [other logical]
    then some other action
else 
    a final action
fi
```

Logical operators:  surround by square brackets
* -eq 
* -neq 
* -gt 
* -lt  

Can use traditional comparison operator (<, >, =) when expression is surrounded by ()

Use && for logical AND  (ex. if [ condition1 ]  && [ condition2 ]

Logical OR is achieved using ||


### Case statements

```
case EXPRESSION in 

    PATTERN_1)
        COMMANDS
        ;;

    PATTERN_2)
        COMMANDS
        ;;

    *)
        COMMANDS
        ;;
esac
```

Asterisk commands are executed if none of the above patterns are matched
Can include `|` in a pattern to employ OR logic.





## Loops

### for loop

```
for i in {start..ending..increment}
do
    some operations
done
```

Alternatively:
`for (( i=0; i<5; i++ ))`


### while loop

```
while [ condition ]
do
   some operations
done
```

'until' loops are written in the same manner

'break', 'continue' functions breaks out of current loop




## Functions 

## Function definition

```
someFunction() {
    actions
}
```

### Function call
`someFunction;`




## Debugging

* Include -x flag in execution
`bash -x ./path/to/scipt.sh`

-OR-

* Include -x flag after shell declaration in script
`#!/bin/bash -x`

Debug a specific block of code:
```
set -x
[CODE 
TO 
DEBUG]
set +x
```

## Data streams

### Input to script

`/path/to/script.sh input1 input2`

Within the script, these inputs may be accessed via $1, and $2.
$0 is the script name

Allow for arbitrary number of inputs:
Within script:  `args=("$@")`

Number of arguments input:  `$#`


### Output

Storing application STDOUT to a variable
`some_variable=$(some_application)`





'0' refers to standard input
'1' refers to standard output
'2' refers to standard error

`ls -al 1>file1.txt 2>file2.txt`
Above snippet, saves std output/error to file1/2

Send both output/error to same file
`ls -al >file1.txt 2>$1`
-- OR -- 
`ls -al >& file1.txt`


### Transferring between scripts

Use export command 
`message='hi'; export message`


Variable maybe accessed in another script via `$message`




## Math

`$(( $var1 + $var2 ))`
(spaces surrounding math expression are required)

Alternatively:
`$(expr $var1 + $var2)`

Multiplication is achieved via \* 
(single asterisk refers to the wildcard symbol)



## Comments

* Single line - prepend with #

* Multi-line 
```
: '  
some text 
over many lines
'
```

## Miscellaneous

* Check if file directory exists
```
if [ -d "$DIRNAME" ]
then
  SOME ACTIONS
```

Analagous syntax for checking existence of files using -f flag

Check if string is empty
`if [-z STRING]`


Shellcheck tool detects errors in bash scripting
