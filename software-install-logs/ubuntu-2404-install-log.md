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
* gdm-settings (customize gdm login screen)
* gnome-maps
* gnome-music
* gnome-shell-pomodoro (time-management app)
* pychess  interface to use chess engines
* hwinfo
* OpenRGB-required packages (https://gitlab.com/CalcProgrammer1/OpenRGB/-/blob/master/Documentation/SMBusAccess.md) i2c-tools
* nvtop (CLI GPU monitoring tool)






## Flatpak
* VideoDownloader
* LocalSend
* Shortwave (internet radio streaming)
* Resources (system monitor GUI)
* cavalier (music visualizer)


## PIP
* tldr (https://pypi.org/project/tldr.py/)
*

## Pipx
* yfinance (as of July 2024, doesn't work via pipx)
* cookiecutter-data-science  (function is named 'ccds')
* jupyterlab


## Github repos
* kitty-themes    
* vim-plug via curl command
* yazi (terminal file manager)
* projectM-visualizer (https://github.com/projectM-visualizer/projectm?tab=readme-ov-file) and frontend -- WON'T BUILD SUCCESSFULLY YET...
*

## Other
* brave-browser  adding keyring and entry to /etc/apt/sources.list.d; updated incorrect architecture warning according to https://community.brave.com/t/solved-linux-deb-install-gives-error-when-you-apt-update-a-repository/464626
* Starship prompt via curl  
* GPT4ALL (allows large language models to be run locally:  https://docs.gpt4all.io/gpt4all_desktop/quickstart.html
* ckb-next via apt repository for control of Corsair device lighting control
* openrgb via download .deb file
* element (downloading keyring and adding repo to /etc/apt/sources.list.d)



## Brave browser extensions
* Vimium
* Bitwarden
* Dark reader
* Tabliss
* Bookmark Sidebar

## Other mods
* Mapped caps lock to escape
* Fixed speaker crackling according to itsfoss.com/buzzing-noise-speaker-linux
* Nerd fonts via download:  Ubuntu, Fira, Caskaydia  Installed to /usr/local/share/fonts.  Update the font cache after moving via fc-cache.
* Changed value of XDG_MUSIC_DIR to $HOME/Documents/music so that music can be found by gnome-music
* Including `acpi_enforce_resources=lax` into /etc/default/grub so that OpenRGB can find RAM
