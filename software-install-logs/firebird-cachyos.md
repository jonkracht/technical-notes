# ASUS Vivobook ("Firebird") running Cachyos

## TODO

## pacman
* brave (disable KDE wallet by selectig Blowfish option and entering no password)
* neovim
* zoxide ("improved" cd command)
* flatpak
* btop  (C++ version)
* starship (terminal prompt)
* libreoffice-still (office suite; 'still' branch is stable and 'fresh' branch includes new features)
* trash-cli
* speedtest++  (supposedly more accurate than speedtest-cli)
* python-matplotlib
* python-pip
* pypy3 (faster python interpreter)
* zathura, zathura-pdf-poppler (pdf reader)
* hyprlock, hypridle (add an exec-once statement to hyrpland.conf to start on boot)
* hyprsunset (add exec-once to autoload; creating hyprsunset.conf from wiki example)
* nodejs, npm (bash-language-server lsp requirements)
* python-shapely (Python geometry package)




## paru
* hyprlauncher





## flatpak
* Including flathub via `flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo`
* G4 Music Player (also called Gapless):  `flatpak install flathub com.github.neithern.g4music`





## Python packages

### pip

### pipx




## cargo

## Github repos
* https://github.com/dharmx/walls.git
* Btop themes:  https://github.com/catppuccin/btop  Copied themes to /usr/share/btop/themes/
* eza-themes for styling eza output.  Soft link desired theme *.yml file to ~/.config/eza/theme.yml


## Other methods of installation
* Dank material shell via curl method

## System mods
* Changed capslock to escape in hyprland.conf via `kb_options = caps:escape` in input section
