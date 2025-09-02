# (GNU) make

## General

Automated build system

Define function blocks called "targets" that perform a set of operations

Execute via `make {TARGET}`

If no TARGET is specified, first command in the Makefile is executed

Within project directory, display available make commands by typing"make " (note space) and pressing TAB

Each line of the commands are effectively run in a new shell.  To have one command affect the other, use semicolon to list multiple commands on a single line.

Alternatively, use `export shell_env_var` to access to an environment variable in all the recipes.


Default shell is `/bin/sh` but can explicitly set via the SHELL variable `SHELL=/bin/bash`


## Logic

### if/else
```
foo = ok

all:
ifeq ($(foo), ok)
	echo "foo equals ok"
else
	echo "nope"
endif
```

Check if variable is defined with `ifdef`



## Dependencies

Structure targets to indicate that one depends on the presence of another.

By default, Make views each target as a file or folder.  When a target is executed, Make will check if the target already exists.  It will only be run if the target does not exist.


### Example of targets requiring other files/folders

'train' requires 'data/training.csv' which in turn requires 'data' (a folder)

```
data:
    mkdir -p data

data/training.csv: data
    curl https://filesamples.com/samples/document/csv/sample1.csv > data/training.csv
    echo "Downloaded data/training.csv"

train: data/training.csv
    python train.py --learning-rate 0.0001 --dataset data/training.csv
```


## .PHONY

Make generally expects to be pointed towards files that are used to create other files

Template of Makefile commands:
```
.PHONY:  COMMAND_NAME
COMMAND_NAME:
    [Place command actions here]
