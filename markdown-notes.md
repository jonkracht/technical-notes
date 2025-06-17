# Markdown


## Headings
Use #'s.  Additional # decreases heading importance.


## Text styling

*Italicized text*       (single asterisk)
**Bold text**           (double asterisk)
~~Strikethrough text~~  (double tilde)
==Highlight==  (double equals sign)


## Horizontal line 

* Three hyphens (---)
* Three asterisks



## Lists

### Ordered list
Use numbers, starting at 1, followed by a period

```
1.  Text
2.  More text
3.  Etc
```


### Unordered list
Use either hyphen, minus sign or plus sign for entries (without mixing)

``
* First item
* Second item
``

### Checkboxes

```
- [] Item 1
- [] Item 2
- [] Item 3
```


## Line breaks

### Single-spaced break  
End line with two spaces or <br/>




## Code segments

### Inline
Surround with backticks  (eg. `sudo apt update`)

### Fenced block

```[LANG] 
SOME CODE
MORE CODE
```

where [LANG] is language of block (Python, C, HTML, etc) and may allow syntax highlighting



## Links

Link text in brackets and URL in parentheses.

`[link text](www.link.url)`

Some example of other link formats:
https://www.uv.es/wikibase/doc/cas/pandoc_manual_2.7.3.wiki?123



## Images

### Local file
![image-name](/path/to/image/)

### Remote file
![image-name](https://www.domain.sthing/path/to/image.png)

### HTML-style syntax is also valid
`<img src = '/path/to/image'>`


### Image resizing/realigning 

```
<p align="center">
<img src="[/PATH/TO/IMAGE]" width=600>
</p>
```




## Tables

### Table template
```
|Header1 |Header2  | Header3|
|--- | --- | ---|
|**bold style**| `code block`|data3|
|\|escape pipe|\`backtick|data13|
```

### Column justification
Set with in second line of table defintion
* Left: `:---`
* Center:  `:---:`
* Right:  `---:`


## Metadata blocks

https://pandoc.org/chunkedhtml-demo/8.10-metadata-blocks.html

### pandoc_title_block

Include document information at the beginning of the document

```
% title
% author(s) separated by semicolons
% date
```

Leave blank space for entries to be omitted


### yaml_metadata_block

Bookended by three hyphens (---)
Second line must be blank

Example:

```
---
title:  'This is the title: it contains a colon'
author:
- Author One
- Author Two
keywords: [nothing, nothingness]
abstract: |
  This is the abstract.

  It consists of two paragraphs.
---
```


## Math notation
Use LaTex syntax with dollar signs surrounding block.

Ex.  Euler's equation is $e^{i \pi} = -1$.


## Footnotes
This is example text [^1] with a couple of footnote tags [^2]

[^1] Footnote 1 text
[^2] Footnote 2 text
