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

### Scroll up/down
By line:  CTRL + SHIFT + UP/DOWN
By page:  CTRL + SHIFT + PAGEUP/PAGEDOWN


### Window/tab management

Previous/next window:
Default was kitty_mod + [ or ]
Remapped to kitty_mod + h/l

Create new tab:  kitty_mod + t

Previous/next tab:
kitty_mod + left/right


Change layout:  kitty_mod + l  (current unbound)

Create new window inside of existing kitty session:
kitty_mod + ENTER


Move window position earlier/later in stack:
kitty_mod + f/b

Change window size:  
kitty_mod + r to enter menu
w(ider), n(arrower), t(aller), s(horter) to resize



### Misc

Change font size:  kitty_mod + minus/plus

Edit config file:  kitty_mod + f2

See environment variables:  CTRL + ALT + a


Change transparency during session:
Requires `dynamic_background_opacity` be set to 'yes' in config (some performance loss, apparently)
kitty_mod + a then m        increases opacity by 0.1
kitty_mod + a then l        decreases opacity by 0.1
kitty_mod + a then 1        sets to completely opaque



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
Imports a bunch (background, foreground, color0, color1, etc.) of hex color variables

### Theme preview
`kitty @ set-colors -a "[/PATH/TO/CONFIG]"`

### Define coloring manually
Provide hex code for colors, background, foreground, etc


### Font

kitty can be only rendered using a monospace font (something about how the graphics are rendered by the GPU).
`kitty list-fonts` prints compatible fonts.
Include `--psnames` to get PostScript name of font which is required for some software

Some available fonts as of 10/2022:
* Courier
* Courier10PitchBT-Roman
* FreeMono
* UbuntuMono-Regular


### Change kitty icon

Adding a new icon via instructions at https://github.com/k0nserv/kitty-icon
Edited kitty.desktop to use 128 pixel icon for launcher and dock
.desktop file may be in `/usr/share/applications/` or `~/.local/[AP_NAME]/share/applications/` depending how/where software was installed

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
