# Fedora 44 on Fractal 
Installed May 2026

## TODO

## DNF
* neovim
* kitty
* zoxide
* fastfetch
* eza
* gnome-tweaks (restore maximize button)
* cargo (rust toolchain)
* python3-pip
* tldr
* speedtest-cli
* btop
* video-downloader (previously used flatpak)
* rclone


## Copr
* alternateved/keyd key remapping daemon (specifically for remapping CAPS to ESC).  Creating `/etc/keyd/default.conf` softlinked to dotfile repo.  https://github.com/rvaiya/keyd 
* starship (terminal prompt) atim/starship


## RPM


## Flatpak
* Tauon-box (music player).  Giving access to music folder via `flatpak override com.github.taiko2k.tauonmb --filesystem=/home/jon/Documents/Music/`.  Milkdrop visualizations downloaded to `/home/jon/.var/app/com.github.taiko2k.tauonmb/data/TauonMusicBox/presets/`
* gnome-shell-extension-manager  https://flathub.org/en/apps/com.mattjakeman.ExtensionManager

## Pip


## Pipx


## Cargo
* vivid

## Gnome-shell-extensions
* Blur-my-shell (blur terminal in Gnome)


## Github
* kitty-themes (https://github.com/dexpota/kitty-themes)  collection of themes for kitty terminal
* wallpaper pack:  https://github.com/dharmx/walls.git

## Other installation methods
* brave-browser
* Downloaded Noto, DejaVu, and Fira nerd fonts and installed to `/usr/share/fonts`.  Other nerd fonts:  https://www.nerdfonts.com/font-downloads
* FreeTube (private Youtube client).  Downloaded .rpm file and install via `sudo dnf install /path/to/package.rpm`

## System mods
* Creating `~/.bashrc.d` directory to hold bash modification files
