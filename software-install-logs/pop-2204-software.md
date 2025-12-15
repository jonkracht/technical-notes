# Software installed on Pop!_OS 22.04 on ASUS laptop

Entries in each category are roughly in chronological order.



## apt
* nvim (jan 2023: removing and installing from source on github)
* kitty  - removed and installing via source from Github to get a newer version than packaged in Pop repo, pre-built binary method; can update via same curl command as install  `curl -L https://sw.kovidgoyal.net/kitty/installer.sh | sh /dev/stdin`
* exa (ls upgrade)
* brave-browser
* speedtest
* rhythmbox
* ubuntu-restricted-extras (mp3 plugins etc.)
* awesome
* tldr tried Haskell implementation but lost ability to sync with online repo.  Trying recommended nodejs client so also installing nodejs and npm - annoying.  Installing python version with pip.
* vlc
* mpv
* neofetch
* texmaker
* lyx
* vim-plug
* dmenu
    * initially installed via `apt install suckless-tools` but removed and cloned source for dmenu only in order to apply patches 
    * installed libx11-dev, libxft-dev to make 
    * cloned distro-tube's build; stability issues so back to stock repo build
* zsh shell
* fish shell
* cheese
* zathura (pdf viewer)
* ncdu (drive usage tool)
* gnome-tweaks, gnome-shell-extensions (to customize desktop environment)
* compton
* blueman (bluetooth applet to use in awesome)
* Qutebrowser
* pcmanfm-qt
* i3lock (screen locker)
* gimp
* texlive-full (so as to have all Latex packages)
* ubuntu-wallpapers-jammy (stored in /usr/share/backgrounds/)
* flameshot
* mpd, mpc and cantata (music players)
* xbacklight & brightnessctl (provide screen brightness control in awesome; ended up using 'light' instead)
* steam
* scummvm (retro game engine)
* rclone (to backup/sync files)
* pandoc (to convert markdown files to other formats)
* minicom (terminal emulator for Opus Two work)
* wavemon (to monitor wireless connection properties)
* polyglot (required for Stockfish engine to interact with xboard)
* jupyter (via https://itslinuxfoss.com/install-jupyter-notebook-ubuntu-22-04/ ); required python3-pip, virtualenv
* Installing default-jre and libreoffice-java-common packages to silence libreoffice warnings
* obsession for logout, shutdown, suspend, etc management in awesome
* [light](https://github.com/haikarainen/light) package to control screen brightness in awesome; adding user to 'video' group to make light work
* black (aesthetic styling of Python)
* octave (Matlab scripts)
* gnome-books for reading epub files (untested if successful)
* dmg2img to create a MacOS USB installer
* pavucontrol volume control gui
* gparted disc formatting utility to create a macos installer
* xscreensaver to play around with screensavers (configure through GUI of xscreensaver-demo); installing rss-glx, xscreensaver-data-extra, xscreensaver-gl-extra package for complete screensaver set
* picom:  Trying in place of compton while using awesome; installing required packages specified at https://github.com/yshui/picom .  Used sample config file at /usr/share/doc/picom/examples as starting point of config.  Getting some screen tearing so changing backend from xrender to glx; included --experimental-backends flag.  Nov 2023: upgrading to 10.2 by recompiling in order to fix awesome autostart bug.
* alacritty, konsole for a few additional terminals
* Microsoft core fonts via deb package: https://github.com/pop-os/pop/issues/1321
* Installed JetBrainsMono font via downloaded zip and manually moving files to `/usr/share/fonts/jetbrainsmono/`
* Trying JetBrains DataSpell, IDE for data science; non-free so uninstalled
* lilypond for music notation in latex
* deluge torrent client (previously used transmission)
* timeshift for system snapshots
* fzf fuzzy finder for both command line and vim
* kazam screencast utility
* qmmp (winamp clone)
* cookiecutter (tool for creating project outline structures)  Removed in favor of pipx method to get more current version.
* exfat-fuse to format usb drive as exfat to interact with Windows
* librecad for creating 2D floor plans
* Looking for a better file manager:  spacefm-gtk3, pcmanfm
* shellcheck:  tools for detecting errors in bash scripts
* bat (cat command update):  binary is title 'batcat' in order to avoid name conflicts
* rofi
* abiword for editing Word documents
* sxiv image previewer
* thunar file manager (to allow theme standardization unlike nautilus)
* cava music visualizer
* tree (file directory tree)
* systemd-container (to get machinectl command required for gdm-settings)
* virtualenvwrapper
* wkhtmltopdf (pdf engine)



## Apt repository






## PPA
* ckb to configure corsair devices.  Using weekly build PPA:  https://launchpad.net/~tatokis/+archive/ubuntu/ckb-next-git
Modifying /etc/systemd/system/multi-user.target.wants/ckb-next-daemon.service ExecStart line to include --enable-experimental flag



## Flatpak (likely installed via Pop! Shop which is labeled as io.elementary.appcenter in system processes)
* lutris
* Ungoogled Chromium
* EasyEffects (audio effects for pipewire; used to be PulseEffects; flatpak used; config located in `~/.var/app/...`)
* nuclear music player
* spotify
* vscodium
* bottles to run windows software
* cavalier music visualizer
* videodownloader (save local copies of online e.g. youtube videos)
* localsend (fileshare within local network)
* flatseal (modify permissions of other flatpaks)
* signal desktop client  (10/2025:  removing flatpak in favor of recommended source method)
* blanket for ambient noise
* gdm-settings https://github.com/gdm-settings/gdm-settings 
* resources:  view/manage system resources (ex. cpu, gpu, mem)






## Github repos
* EasyEffects-Presets (sensible presets for equalization, reverb, etc:  https://github.com/JackHack96/EasyEffects-Presets )
* lain (widgets for awesome; `git clone https://github.com/lcpz/lain.git ~/.config/awesome/lain`)
* btop (latest-greatest bashtop update; themes located at `/usr/share/btop/themes/`)
* bash scripts for previewing terminal colorschemes (https://github.com/stark/Color-Scripts; https://gitlab.com/dwt1/shell-color-scripts)
* Awesome themes from https://github.com/lcpz/awesome-copycats
* neovim (https://github.com/neovim/neovim/releases/).  April 2025:  Building version 0.11.0 stable from source so runtime files are found.
* lf (terminal file manager):  Installing via a pre-built binary from https://github.com/gokcehan/lf/releases?page=1 
* Alternative kitty icon:  https://github.com/k0nserv/kitty-icon  Overwrote png files in ~/.local/kitty.app/lib/kitty/logo with new icons
* Sweet folders  https://github.com/EliverLara/Sweet-folders.git
* Alacritty color themes:  https://github.com/alacritty/alacritty-theme 
* Wayfire window manager:  https://github.com/WayfireWM/wf-install
* zoxide (smarter cd command) via curl
* fontpreview via make install
* projectm (music visualizer) https://github.com/projectM-visualizer/projectm?tab=readme-ov-file
* Rofi themes https://github.com/newmanls/rofi-themes-collection
* Fontpreview for terminal preview (/usr/local/share/fonts/CaskaydiaCoveNerdFont/CaskaydiaCoveNerdFontMono-Regular.ttf).  Cloning and then install using make


## Python packages via pip
* jupyterlab
* yfinance (pulling stock data)
* nbterm (interact with jupyter from the terminal)
* unoserver (document type conversion such as LibreOffice)


## Pipx
cookiecutter

## Cargo/rust
* typst (pdf engine)


## Other means
* jetbrains toolbox and pycharm (proprietary software so not in repos; installed to /opt; executable below ~/.local/share/Jetbrains/... ; creating symlink in /usr/bin to allow dmenu to find and run it; later removing since it seems no longer necessary)
* zoom via downloaded .deb file
* Microsoft core fonts via deb package: https://github.com/pop-os/pop/issues/1321
* Installed JetBrainsMono font via downloaded zip and manually moving files to `/usr/share/fonts/jetbrainsmono/`
* Swift via tarball; needed some finagling to get it run error-free https://github.com/llvm/llvm-project/issues/55575
* Starship terminal prompt:  via curl installer
* zoom (.deb)
* openrgb (.deb)
* Ventoy for creating bootable USB's with multiple OS's on them
* thorium browser via adding to sources.list.d (https://thorium.rocks/)
* Updated nodejs to version 22.14.0 via Method 2 in https://itsfoss.com/upgrade-node-ubuntu/
* Lua interpreter (downloaded gz, tar and used 'make' to build and install it)





## Browser plugins
* bitwarden (password manager)
* dark reader (sets light/dark mode for eye-friendly webpage viewing);  trying "Dark Mode" an equivalent for Chrome-based browsers
* tabliss (new browser tabs display pictures)
* Great Suspender (halts inactive browser tabs to conserve system resources).  As of Sep 2023, deemed to be adware...  Brave removed automatically from browser extensions.
* Chromium webstore extension to allow anonymous shopping (https://github.com/NeverDecaf/chromium-web-store)
* Bypass paywalls (for select websites)  https://github.com/iamadamdev/bypass-paywalls-chrome
* vimium to allow vim-style navigation of web pages
* Cookie Remover for paywall bypass





## System mods
* Remapped Caps Locks key to an additional Escape (instructions at https://thesynack.com/posts/persistent-capslock-behavior/)
* Adding ssh key from previous Ubuntu install to ssh agent to ease Github communication
* Enabling ufw (uncomplicated firewall) via `systemctl enable ufw`; check if starting on boot
* Fix speakers cracking via https://superuser.com/questions/1493096/linux-ubuntu-speakers-popping-every-few-seconds
* Disabling autostart in Gnome sessions for awesome-only packages (e.g. blueman) by adding `X-GNOME-Autostart-enabled=false` to files located in `/etc/xdg/autostart`
* Modified /etc/gtk-3.0/settings.ini to use Adwaita-dark theming for gtk software
* Creating `my-env-vars` file in `/etc/profile.d` containing environment variables to ease standardizing of theming across various self-configured software
* Adding user to 'dialout' group to facilitate minicom use
* Replacing github ssh key as per https://github.blog/2023-03-23-we-updated-our-rsa-ssh-host-key/
* Installing candy icon set https://github.com/EliverLara/candy-icons
* Attempting to open port 53317 to allow LocalSend to behave properly.  Trying `ufw allow 53317`
* Fixed incorrect xdg-open behavior:  determined current default program via `xdg-mime query default <mime-type>` and set to desired behavior `xdg-mime default <application> <mime-type>` 



## Gnome extensions
Improved workspace indicator (icon displaying current workspace number)


