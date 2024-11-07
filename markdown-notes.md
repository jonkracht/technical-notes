# Headings
Use #'s.  Additional # decreases heading importance.


# Text styling

*Italicized text*       (single asterisk)
**Bold text**           (double asterisk)
~~Strikethrough text~~  (double tilde)
==Highlight==  (double equals sign)


# Horizontal line 

* Three hyphens (---)
* Three asterisks

# Lists

## Ordered

Use numbers, starting at 1, followed by a period

1.  Text
2.  More text
3.  Etc


## Unordered
Use hyphen, minus sign or plus sign for entries  (but don't mix)

``
* First item
* Second item
``
## Checkbox
- [] Item 1
- [] Item 2
- [] Item 3


# Line breaks

## Single-spaced break  
End line with two spaces or <br/>




# Code segments

## Inline
Surround with backticks "\`"

Ex. `sudo apt update` updates your repo lists

## Fenced block
```[LANG] 
SOME CODE
MORE CODE
```

where [LANG] provides syntax highlighting and can be Python, C, HTML, vim etc



# Links

Link text in brackets and URL in parentheses.

[link text](www.link.url)




# Images

## Local
![image-name](/path/to/image/)

## External
![image-name](https://www.domain.sthing/path/to/image.png)

## May also use html syntax:
<img src = '/path/to/image'>


## Resizing 

<p align="center">
<img src="[/PATH/TO/IMAGE]" width=600>
</p>



# Tables

|Header1 |Header2  | Header3|
|--- | --- | ---|
|**bold style**| `code block`|data3|
|\|escape pipe|\`backtick|data13|


## Column justification
Set with in second line of table defintion
* Left: `:---`
* Center:  `:---:`
* Right:  `---:`


# Metadata blocks

## pandoc_title_block

Include document information at the beginning of the document

```
% title
% author(s) separated by semicolons
% date
```

Leave blank space for entries to be omitted


## yaml_metadata_block

Bookended by three hyphens (---)
Second line must be blank

Example:
---
title:  'This is the title: it contains a colon'
author:
- Author One
- Author Two
keywords: [nothing, nothingness]
abstract: |
  This is the abstract.

  It consists of two paragraphs.
...


# Math
Use LaTex syntax with double dollar sign before and after code segment


# Footnotes
This is example text [^1] with a couple of footnote tags [^2]

[^1] Footnote 1 text
[^2] Footnote 2 text
