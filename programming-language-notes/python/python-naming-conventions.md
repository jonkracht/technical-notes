# Common naming conventions in Python

Double underscore is abbreviated as "dunder"


## Single leading underscore
* Variable/method:  hint (ie. not enforced by interpreter) indicating only intended for internal use
* Function:  names beginning with an underscore will not be imported by a wildcard import (`import *`)


## Single trailing underscore
* Used when most clear name for a variable/function is a Python keyword  (if `class` was desired, non-conflicting name would be `class_`


## Leading dunder
* Python recasts variable/method name so that it less likely to create name conflicts - called "name mangling"
* Use case?  Maybe experiencing naming collisions when creating new classes that inherit from 


## Leading and trailing dunders
* Reserved for special use (ex. __init__ or __call__) so generally avoid using
* May be called dunder methods or magic methods


## Single underscore
* Denotes that a variable is temporary or insignificant
* Use case:  unpacking components of a tuple and some are not needed
* In Python REPL's, holds result of previous command





## Camel case

## Snake case
