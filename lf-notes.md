# lf terminal file manager

Documentation:
`lf -doc`


## Config

### Theming
* Colors and icon set are set in ~/.config/lf/{icon,colors}
* Alternatively, lf inherits environment variable `LS_COLORS`
* vivid tool is used to create color themes


## Commands

### Cut, copy, paste

* Uses vim bindings (d, y, p)

* To move multiple files, select files with spacebar, navigate to destination, and cut/copy and paste (d/y then p).


* Quit  `q`

* Run shell command:  `$ {command}`


* Rename:  `r`

* Open file with $EDITOR:  `e`

* Open a file: `o`  (defaults to xdg-open)

* Change sorting method:  press 's' and a menu of sort options (time, type, extension, size) appears;  pressing 'z' presents other sorting options


## Selection
* Spacebar toggles a file's selection state 
* `u` unselects file
* `v` inverts which files are selected in directory
* Selected files are stored in `~/.local/share/lf/[tags,history,files]`
* `clear` empties copy/cut buffer; mapped to `c` by default 


## Misc

* Return to terminal from lf:  `w`


## Wiki tips (i.e. cookbook)
https://github.com/gokcehan/lf/wiki/Tips




## TODO
* Font preview not working because ImageMagick packaged by Ubuntu is out of date
