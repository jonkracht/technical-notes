## Produce a pdf

`pandoc [FILENAME] -o [OUTPUT_NAME].pdf`


## Referencing in document

https://github.com/lierdakil/pandoc-crossref


## Hyperlinks

### Render links in color
Include in preamble (at the beginning of the document):
```
---
colorlinks: true
---
```


## Errors
If receive warning `[WARNING] [makePDF] LaTeX Warning: Float too large for page by 24.48112pt on input line 128.`

Include `{width=80%}` in the image input call.
