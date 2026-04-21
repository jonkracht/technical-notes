# kitty terminal emulator


## Config

To bring up config file in new window `kitty_mod + F2`
To reload config after changes are made  `kitty_mod + F5`

### Example config
Was located at `/usr/share/doc/kitty/examples/kitty.conf`
Moved to `~/.local/kitty.app/share/doc/kitty/..`


### Sections
* Fonts
* Cursor customization
* Scrollback
* Mouse
* Performance tuning
* Terminal bell
* Window layout
* Tab bar
* Color scheme
* Advanced
* OS specific tweaks
* Keyboard shortcuts
* Clipboard
* Scrolling
* Window management
* Tab management
* Layout management
* Font sizes
* Select and act on visible text
* Miscellaneous





## Shortcuts

Many use 'kitty_mod' as prefix which by default is CTRL + SHIFT

### Scroll up/down
By line:  km + UP/DOWN
By page:  km + PAGEUP/PAGEDOWN


### Window/tab management

Previous/next window:
Default was km + [ or ]
Remapped to km + h/l

Create new tab:  km + t

Previous/next tab:
km + left/right


Change layout:  km + l
Remapped to:  km + z

Create new window inside of existing kitty session:
km + ENTER


Move window position earlier/later within stack:
km + f/b

Change window size:  
Enter resizing menu with km + r
Use w(ider), n(arrower), t(aller), s(horter) to resize



### Misc

Change font size:  km + minus/plus

Edit config file:  km + f2

See environment variables:  CTRL + ALT + a


Change transparency window:
Requires `dynamic_background_opacity` be set to 'yes' in config (some performance loss, apparently)
km + a then m        increases opacity by 0.1
km + a then l        decreases opacity by 0.1
km + a then 1        sets to completely opaque



See effective config with `debug_config` or `CTRL + SHIFT + F6`
Reload config `CTRL + SHIFT + F5`


Open kitty shell        kitty_mod + ESC

Insert a unicode character (ex. symbol or emoji)        kitty_mod + u


## Theming

### Included themes
Enter into a kitty shell via `kitty_mod + ESC`
Type `kitten themes` to view list

###  `https://github.com/dexpota/kitty-themes`
Add `include [/PATH/TO/CONFIG]` to config file
Imports pre-defined color palettes (ex. background, foreground, color0, color1 ...)

### Theme preview
`kitty @ set-colors -a "[/PATH/TO/CONFIG]"`

### Define coloring manually
Provide hex code for colors, background, foreground, etc


## Font

kitty can be only rendered using a monospace font.  Has to do with how graphics are rendered by the CPU/GPU.
`kitty list-fonts` lists compatible fonts.
Include `--psnames` to get PostScript name of font which is required for some software





## Change kitty icon

Adding a new icon via instructions at https://github.com/k0nserv/kitty-icon
Edited kitty.desktop to use 128 pixel icon for launcher and dock
.desktop file may be in `/usr/share/applications/` or `~/.local/[AP_NAME]/share/applications/` depending how software was installed

Alternatively, can place an image named kitty.app.png in the config directory.  Some chance system detects and sets this icon properly.



## Parameters modified by JK
initial_window_width
initial_window_height
enabled_layouts  (reordered list of layouts through which to cycle)

Border color of active/inactive window:  `active_border_color` and `inactive_border_color`

inactive_text_alpha    fade text in inactive windows

hide_window_decorations
Hides title-bar and window borders.  Interaction with awesomewm







## Questions

* Difference between `window_margin_width` and  `window_padding_width`?



## TODO
*  Is it possible to input a command (such as next_layout) without using a hotkey (perhaps like vim)?
