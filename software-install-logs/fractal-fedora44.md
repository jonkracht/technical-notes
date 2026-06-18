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
* vlc
* multimedia codecs not included with Fedora:  https://rpmfusion.org/Howto/Multimedia?highlight=%28%5CbCategoryHowto%5Cb%29
* transmission (torrenting)
* zathura, zathura-pdf-poppler (pdf reader)
* pandoc (markdown format converter; installs pandoc-cli and pandoc-common packages)
* texlive-scheme-full (installs all TexLive packages (~5k) including pdflatex)
* python3-ipykernel, jupyterlab
* python3-yfinance
* python3-virtualenv (Python package manager)
* inxi (command line sysinfo tool)


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
* Changing kitty icon by copying /usr/share/applications/kitty.desktop to ~/.local/share/applications/ and editing `Icon` parameter to path of desired icon
* Change dns to Google's:  IPv4:  8.8.8.8, 8.8.4.4    IPv6:  2001:4860:4860::8888, 2001:4860:4860::8844
* Configure dnf to use fastest mirror and allow up to 10 downloads via:  `sudo dnf config-manager setopt max_parallel_downloads=10 fastestmirror=True`
