# swift

Developed by Apple and open source community.
Released in 2014.
Inspired by but not derived from Objective C


## repl  (read evaluate print loop)

Enter into by `swift repl`


## General
* Use TAB key to get autocompletion suggestions
* Multiple commands per line are possible by separation with a semi-colon




### Comments
* Single line   `//`
* Multi-line comment `/*` and `*/`

Can nest multi-line comments


## Data types

### Constant
`let myConstant = 42`

### Variable
`var myVariable = 50`

Can explicitly set variable type in its definition:
`let myVariable: Double = 70`

## Floating point numbers
* Float:  32 bit
* Double (default):   64 bit


## Boolean


### Tuple

Elements may be of differing data types
Can not add/remove elements


#### Definition
* Positional:  `var aTuple = ([entry1], [entry2], ...)`
* Named element:  `var company = (product: "Photoshop", version: 2.1)`


#### Working with
* Access element by position `aTuple.1` or by name if defined in that manner `company.product`
* Cannot remove 



### Arrays

var fruits = ["apples", "lemons", "kiwi"]

Comments:
* Zero indexed 
* Arrays defined via a 'let' command are immutable
* `.append` method adds elements to mutable arrays and dictionaries



### Dictionary

Collection of key/value pairs
Unordered

`var occupations = [
    "Malcolm": "Captain",
    "Kaylee": "Mechanic",
]`


Create empty array/dictionary:
`let emptyArray: [String] = []`
`let emptyDictionary: [String: Float] = [:]`


### Missing values

Called optionals.
Objects with possibly missing values are identified via '?':
`var optionalString: String? = "Hello"`

Provide a default value:
`let myString = "Hi \(possibleMissingVal ?? defaultVal)"`




## Logic

### if

### Switch/case statement

Analagous to if, elif,... block

```
let someVar = [SOME_VAL]
switch someVar {
case [SOME_VAL1]:
    [ACTION]
case [SOME_VALE2]:
    [ACTION]
:
default:
    [DEFAULT ACTION]
}
```


## Loops


### for loop

#### Iterate over dictionary
`for (a, b) in someDict {
    [ACTIONS]
}`
where 'a' are the keys and 'b' are values


#### Use loop index
```
for i in [minVal]..<[maxVal+1] {
    [ACTIONS]
}
```

May omit the '<' to include endpoint.



### while loop
```
while [someLogical] {
    [ACTIONS
}

```

Alternate form to ensure loop is run at least once:
```
repeat {
    [ACTIONS]
} while [someLogical]
```



### Functions


```
func sayHello(to name: String, onDay day: String) -> String {
    return "Hello \(name), the day is \(day)"
}
```

* Right arrow (->) indicates return type of the function; not required if function has no return
* To return multiple values, use a tuple:  `... -> (val1: val1Type, ...){`


Use different variable names inside function from those of its call:
```
func greet(_ person: String, on day: String) -> String {
    return "Hello \(person), today is \(day)."
}
greet("John", on: "Wednesday")
```

Here, the function call requires no identify for the name and 'on' for the day.  Inside the 'greet' function, they are mapped to 'person' and 'day' respectively.

** What is the use case for this functionality? **



#### Function calls
* Pass variables into functions by prefixing name with &




### Closures

Often a synonym for anonymous functions



### enum (short for enumerate) 






### Structures




### Classes

#### Definition
```
class [className] {
    [Property declarations; methods/function declarations
}
```

'init' method allows properties to be given to instance when created

Example:
```
class NamedShape {
    var numberOfSides: Int = 0
    var name: String

    init(name: String) {
        self.name = name
    }

    func simpleDescription() -> String {
        return "A shape with \(numberOfSides) sides."
    }
}
```


#### Create an instance of the class
`var [classInstance] = [className]()`


#### Access/modify properties/methods of instance
Set property value: `[classInstance].[classProperty] = [VAL]`


### Sub/super classes

Definition:  `class [subClass]:  [superClass]`

Subclass methods that conflict with superclass methods must be identified with `override` in the function defintion
`override func [funcName]....`

Refer to methods of superclass by `super.[methodName]`



### Getters & setters



### Modules

#### GLIBC

#### Darwin


### Concurrency

Run code asynchronously to let other process happen while waiting.





### Error handling

#### Error protocol

Definition:
```
enum PrinterError: Error {
    case Error1
    case Error2
    :
}
```

Label a function that could throw an error with 'throws'.
Use 'throw' to identify an error.

Example:
```
func aFunc([inputs]) throws  -> String {
    if [ERROR LOGICAL] {
        throw PrinterError.Error1
    }
```


#### do-catch

```
do {
    let printerResponse = try send(job: 1040, toPrinter: "Bi Sheng")
    print(printerResponse)
} catch {
    print(error)
}
// Prints "Job sent"
```


### Swift package manager







## References:
* [A Swift Tour](https://docs.swift.org/swift-book/GuidedTour/GuidedTour.html#//apple_ref/doc/uid/TP40014097-CH2-ID1)
