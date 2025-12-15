# Modularized vim kickstart

Fork of:  https://github.com/dam9000/kickstart-modular.nvim

Take single config file of original kickstart project and separates into task-specific modules


## Directory structure

### `init.lua`

Load modules via require method:  options, keymaps, lazy-bootstrap, lazy-plugins
These are .lua files located in ./lua


### lua folder

#### custom folder

##### init.lua
Define user-specific plugins

##### nvim-colorizer.lua


#### kickstart folder

##### health.lua
Check if system is setup properly

##### plugins folder
For each plugin, contains a lua file defining installation and configuration
Named `PLUGIN_NAME.lua`


#### keymaps.lua
Configure navigation, motions

#### lazy-bootstrap.lua
Ensure lazy plugin manager is installed prior to installing plugins

#### lazy-plugins.lua
Define plugins to incorporate into vim instance

#### options.lua
Configure vim settings 

