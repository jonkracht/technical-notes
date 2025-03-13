Installed Ubuntu 24.04 on newly-built Fractal system in May 2024

## APT
* neofetch
* btop
* lutris
* kitty
* git 
* neovim
* zoxide
* signal
* fzf
* ttf-mscorefonts-installer (Microsoft fonts)
* lf
* flatpak
* gnome-software-plugin-flatpak
* vlc
* zathura
* pandoc
* texmaker
* gimp
* rclone (rsync for commercial cloud storage)
* jupyter (installs nbconvert, notebook)
* virtualenv
* pipx (install Python packages system wide.  Debian/Ubuntu changed how Python packages are managed)
* python3-venv, python3-pip (required for pipx)
* python3-ipykernel (allow virtual environments within Jupyter)
* texlive-xetex texlive-fonts-recommended texlive-plain-generic (for nbconvert exporting to pdf:  https://nbconvert.readthedocs.io/en/latest/install.html#installing-tex)
* gnome-tweaks
* eza (modern ls; fork of now-unmaintained exa)
* easyeffects (collection of audio plugins; formerly PulseEffects)
* gnome-shell-extension-manager
* gdm-settings:  Customize GDM login screen (also called a display manager).  Installed to increase font size to accommodate higher resolution monitors.  Out of box setting was Ubuntu Sans Regular 11. 
* gnome-maps
* gnome-music
* gnome-shell-pomodoro (time-management app)
* pychess  interface to use chess engines
* hwinfo
* OpenRGB-required packages (https://gitlab.com/CalcProgrammer1/OpenRGB/-/blob/master/Documentation/SMBusAccess.md) i2c-tools
* nvtop (CLI GPU monitoring tool)
* tldr-hs
* bat (clone of cat with syntax highlighting).  Invoked by `batcat`
* ffmpeg Needed for lf video preview
* ffmpegthumbnailer for lf previewing
* xdotool, nsxiv (dependencies for fontpreviewer)
* vivid (generate color themes for ls command)
* trash-cli (includes commands trash-put, trash-empty, trash-restore, trash-rm)
* alacritty
* eza (updated ls command).  Version in Ubuntu 24.04 repo (18.2) is quite behind.  Removing and using keyring/source method.
* libcupsimage2-dev (to get Epson printer to work)
* adwaita-qt (for theming QT apps in an Adwaita-like way)
* font-manager
* ripgrep (executable is named rg)
* steam



## Flatpak
* VideoDownloader
* LocalSend
* Shortwave (internet radio streaming)
* Resources (system monitor GUI)
* cavalier (music visualizer)


## PIP
* tldr (https://pypi.org/project/tldr.py/); update broke perhaps because of no recent development.  Switching to Haskell implementation (tldr-hs in Ubuntu repo).


## Pipx
* yfinance (as of July 2024, doesn't work via pipx)
* cookiecutter-data-science  (function is named 'ccds')
* jupyterlab
* black (code formatting)


## Github repos
* kitty-themes    
* vim-plug via curl command
* yazi (terminal file manager)  Version 0.3.3 released in Sep 2024.  Placed files in ~/.local.  Source file repo (https://github.com/sxyazi/yazi/tree/shipped) cloned to ~/repos so as to acquire template config files (keymap.toml, theme.toml, yazi.toml)
* projectM-visualizer (https://github.com/projectM-visualizer/projectm?tab=readme-ov-file) and frontend -- WON'T BUILD SUCCESSFULLY YET...
* fontpreview for previewing in terminal (https://github.com/sdushantha/fontpreview).  Cloning repo and then install with make
* Collection of alacritty color themes:  git@github.com:alacritty/alacritty-theme.git
* eza-themes







## Other installation methods
* brave-browser  adding keyring and entry to /etc/apt/sources.list.d; updated incorrect architecture warning according to https://community.brave.com/t/solved-linux-deb-install-gives-error-when-you-apt-update-a-repository/464626
* Starship prompt via curl  
* GPT4ALL (allows large language models to be run locally:  https://docs.gpt4all.io/gpt4all_desktop/quickstart.html)
* ckb-next via apt repository for control of Corsair device lighting control
* openrgb via download .deb file.  Trying experimental branch rather than stable.
* element (downloading keyring and adding repo to /etc/apt/sources.list.d)
* pycharm community edition.  Downloaded compressed file (both .gz and .tar), extracted, moved to ~/.local/ and ran installer shell script; creating .desktop file in ~/.local/share/applications
* mtn (video thumbnailer)  Adding apt repository
* eza via keyring/source method  https://github.com/eza-community/eza/blob/main/INSTALL.md
* geekbench (downloaded) http://support.primatelabs.com/kb/geekbench/geekbench-6-command-line-tool
* Epson printer driver via downloaded .deb
* Stockfish chess engine:  Downloaded zip file with executable inside.  Placed in `~/Documents/games/chess/` but not required.



## Brave browser extensions
* Vimium
* Bitwarden
* Dark reader
* Tabliss
* Bookmark Sidebar



## Gnome shell extensions
* blur-my-shell
* clipboard history
* user themes
* highlight focus  - looks ugly.  find something better.


## Other system mods
* Mapped caps lock to escape
* Fixed speaker crackling according to itsfoss.com/buzzing-noise-speaker-linux
* Nerd fonts via download:  Ubuntu, Fira, Caskaydia  Installed to /usr/local/share/fonts.  Update the font cache after moving via fc-cache.
* Changed value of XDG_MUSIC_DIR to $HOME/Documents/music so that music can be found by gnome-music
* Including `acpi_enforce_resources=lax` into /etc/default/grub so that OpenRGB can find RAM
* Enabling command completion in bash shell via eval command in bashrc:  https://askubuntu.com/questions/1026332/does-pip-have-autocomplete
