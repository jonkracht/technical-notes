Automated build system

Define rules that execute desired operations



Execute via `make {RULE}`


## .PHONY

Make generally expects to be pointed towards files that are used to create other files

Template of Makefile commands:
```
.PHONY:  COMMAND_NAME
COMMAND_NAME:
    [Place command actions here]
