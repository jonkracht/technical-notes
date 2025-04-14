
## Arguments
Use argv to access information passed in from command line:
`from sys import argv`

unpack arguments:  `arg1, arg2, ... = args`

Use data input by user:  var = input(a_prompt)

## Reading/writing files  
target = open(filename, 'w'); target.write(astring); target.close()

### Determine whether a file exists:  
`from os.path import exists; exists(name)`
Returns a Boolean if file exists (in working directory?)

### Input arbitrary numbers of values into a function:  
`def function(*args)`
unpack


