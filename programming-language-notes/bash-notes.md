# bash

Primarily a scripting language
Commands used in a text editor NOT directly in terminal

Convention is to give bash scripts a .sh extension

The !# (shebang) at the beginning of the file defines which interpreter is to be used.

Most common is `#!/bin/bash`

Alternatively, use the 'env' executable to locate first instance of bash in the path:  `#!/usr/bin/env bash`

Available shells are listed in `/etc/shells`




Make file executable:
`chmod a+x [/path/to/file.sh]`
May need to execute with sudo privileges

Alternatively, use three digit syntax:  `chmod 666 [/path/to/file]`
Can also use three-digit syntax to alter permissions



## Variables

* Create a variable
myvar='Monkies'     (no spaces allowed)

Convention is to use lowercase for variable names so as not to conflict with system variables

Variable contents are accessed by prepending their name with $
ex.  $myvar




Arrays:  
1 dimensional data structure
Create array with newArr=('thing1' 'thing2')
(BASH is fairly picky about spaces before/after equals sign)

Delete element(s) of array:
unset newArr[2]

Printing elements:
Single element:  echo "${newArr[1]}"
All elements (@ represents all):  echo "${newArr[@]}"
Print indices:  echo "${!newArr[@]}"
Print length of array (#):  echo ""${#newArr[@]}


## Input
Use "read" function to query user for input.
Syntax:  `read variable_name`

Include a prompt in the query:
`read -p "Text to input a variable: " [variable_name]`


IF/THEN syntax:
if [ logical statement ]
then 
    some action
elif [other logical]
    then some other action
else 
    a final action
fi


Logical operators:  -eq, -neq, -gt, -lt  when surrounded by []
Can use traditional operators (<, >, =) when expression is surrounded by ()

Use && for logical AND  (ex. if [ condition1 ]  && [ condition2 ]
OR is achieved using ||



Loops:

* for loop
for i in {start..ending..increment}
do
    some operations
done


Alternatively:
for (( i=0; i<5; i++ ))


* while loop
while [ condition ]
do
   some operations
done


* 'until' loops are written in the same manner

'break', 'continue' functions breaks out of current loop



Storing application STDOUT to a variable
some_variable=$(some_application)
ex. fooVar=$(who)


Function definition:
someFunction() {
    actions
}

Function call:
someFunction;



Debugging bash script: Include -x flag
bash -x ./path/to/scipt.sh

-OR-

include -x flag after shell declaration in script
ex. #! /bin/bash -x

Can debug only a portion of code with:
ex:  set -x
[CODE 
TO 
DEBUG]
set +x


Inputting arguments into a bash script via standard in (STDIN):
In the terminal:
/path/to/script.sh input1 input2 [etc]

Within the script, these inputs may be accessed by referencing $1, $2, etc.
$0 is the script name

Allow for arbitrary number of inputs:
Within script:
args=("$@")

Number of arguments input:
$#




Data streams:

'0' refers to standard input
'1' refers to standard output
'2' refers to standard error

ls -al 1>file1.txt 2>file2.txt
Above snippet, saves std output/error to file1/2

Send both output/error to same file
ls -al >file1.txt 2>$1
-- OR -- 
ls -al >& file1.txt



Transferring between scripts:

Use export command 
message='hi'; export message


Variable maybe accessed in another script via `$message`


## Math

$(( $var1 + $var2 ))
(spaces surrounding math expression are required)

alternatively:
$(expr $var1 + $var2)

Multiplication is achieved via \* 
(single asterisk refers to the wildcard symbol)



## Comments
* single line - prepend with #

* multi-line 
: '  
some text 
over many lines
'


## Miscellaneous

* Check if file directory exists
Check if a directory with desired name exists
if [ -d "$DIRNAME" ]
then
  SOME ACTIONS

Analagous syntax for checking existence of files using -f flag


* shellcheck tool detects errors in bash scripting
