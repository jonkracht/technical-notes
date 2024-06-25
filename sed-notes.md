# sed

Stream editor

## Substitute text
`sed 's/REGEX/SUBSTITUTION/'`

where [REGEX] is some regular expression and [SUBSTITUTION] is text to be substituted


## Regular expressions

### Common patterns

Preface with `\` or invoke sed with `-E` flag

`.`  any single character (except newline)
`\.` match exactly a period (escape character is required)
`*` zero or more characters preceding match
`+` one or more characters preceding match
`[abc]` any one character of a, b, or c
`[0-6]` matches to a single number in the range
`[A-Z]` case-sensitive match in the range
`\w` matches any of [A-Za-z0-9_]
`\D` any non-digit character
`(RX1|RX2)` matches one of
`^` start of the line
`$` end of the line
`\d` any single digit from 0 to 9
`\s`  any whitespace (space, tabl, new line and carriage return)

`^` negates regex
`\?b` allows b to optionally appear in matches 

### Repetitions
Match character(s) number of times in a specified range `[wxy]{2,6}`


### Capture groups

Surround text to be captured from regex by parentheses
Access later via \1, \2, etc
