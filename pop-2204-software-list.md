# pop-software

List of software and system mods in a Pop.OS 22.04 system.  Entries roughly in chronological order.



## APT
* nvim
* kitty  - removed and installing via source from Github to get a newer version than packaged in default repos, pre-built binary method
* exa
* brave-browser
* speedtest
* rhythmbox
* ubuntu-restricted-extras (mp3 plugins etc.)
* awesome
* tldr (Haskell implementation)
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
* pcmanfm (find gtk3 version to guarantee consistent theming)
* i3lock (screen locker)
* gimp
* texlive-full (so as to have all Latex packages)
* ubuntu-wallpapers-jammy (stored in /usr/share/backgrounds/)
* flameshot
* mpd, mpc and cantata (music players)
* xbacklight & brightnessctl (provide screen brightness control in awesome)
* steam
* scummvm (retro game engine)
* rclone (to backup/sync local file directory to Google Drive)
* pandoc (to convert markdown files to other formats)
* minicom (terminal emulator for potential future Opus Two dealings)
* wavemon (to monitor wireless connection properties)
* polyglot (required for Stockfish engine to interact with xboard)
* jupyter (via https://itslinuxfoss.com/install-jupyter-notebook-ubuntu-22-04/ ); required python3-pip, virtualenv)
* Installing default-jre and libreoffice-java-common packages to silence libreoffice warnings
* obsession for logout, shutdown, suspend, etc management in awesome
* (https://github.com/haikarainen/light)[light] package to control screen brightness in awesome; adding user to 'video' group to make light work




## Flatpak (likely installed via Pop! Shop which is labeled as io.elementary.appcenter in system processes)
* lutris
* Ungoogled Chromium
* EasyEffects (audio effects for pipewire; used to be PulseEffects; flatpak used; config located in `~/.var/app/...`)
* nuclear music player
* spotify


## Github repos
* EasyEffects-Presets (sensible presets for equalization, reverb, etc:  https://github.com/JackHack96/EasyEffects-Presets )
* lain (widgets for awesome; `git clone https://github.com/lcpz/lain.git ~/.config/awesome/lain`)
* btop (latest-greatest bashtop update; themes located at `/usr/share/btop/themes/`)
* bash scripts for previewing terminal colorschemes (https://github.com/stark/Color-Scripts; https://gitlab.com/dwt1/shell-color-scripts)
* Awesome themes from https://github.com/lcpz/awesome-copycats


## Python packages via pip
* jupyterlab



## Other means

* jetbrains toolbox and pycharm (propropietary software so not in repos; installed to /opt; executable below ~/.local/share/Jetbrains/... ; creating symlink in /usr/bin to allow dmenu to find and run it)
* zoom via downloaded .deb file


## Browser plugins
* bitwarden (password manager)
* dark reader (sets light/dark mode for eye-friendly webpage viewing)
* tabliss (new browser tabs display pictures)
* Great Suspender (halts inactive browser tabs to conserve system resources)
* Chromium webstore extension to allow anonymous shopping (https://github.com/NeverDecaf/chromium-web-store)





## System mods
* Remapped Caps Locks key to an additional Escape (instructions at https://thesynack.com/posts/persistent-capslock-behavior/)
* Adding ssh key from previous Ubuntu install to ssh agent to enable Github communication
* Enabling ufw (uncomplicated firewall) via `systemctl enable ufw`; check if starting on boot
* Fixing speakers cracking via https://superuser.com/questions/1493096/linux-ubuntu-speakers-popping-every-few-seconds
* Disabling autostart in Gnome sessions for awesome-only packages (e.g. blueman) by adding `X-GNOME-Autostart-enabled=false` to files located in `/etc/xdg/autostart`
* Modified /etc/gtk-3.0/settings.ini to use Adwaita-dark theming for gtk software
* Creating `my-env-vars` file in `/etc/profile.d` containing environment variables to ease standardizing of theming across various self-configured software


## Gnome extensions
Improved workspace indicator (icon displaying current workspace number)



