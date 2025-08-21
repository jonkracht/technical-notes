## TODO
* openrgb packages  (must add acpi_enforce_resources=lax to /etc/default/grub)
* adwaita-qt (for theming QT apps in an Adwaita-like way)
* projectM visualizer
* ckb-next
* element (messenger)
* DNS server
* cyberpower utility





## DNF
* tldr
* kitty
* neovim
* zoxide
* python3-pip
* btop
* cargo (rust package manager and build tool)
* trash-cli
* ripgrep (installed out of the box)
* lutris
* hyprland
* vlc
* zathura, zathura-plugins-all (especially need pdf-poppler for pdf viewing)
* pandoc
* texmaker
* gimp
* rclone
* texlive-xetex
* gnome-tweaks
* easyeffects
* nvtop (GPU process monitoring)
* nodejs
* pipx
* fastfetch (no-longer developed neofetch replacement)
* gnome-music (laggy and uses ~7GB RAM with current music library)
* gnome-pomodoro (time management utility)
* pychess  (front-end for chess engines)
* hwinfo (hardware information tool)
* bat (modernized cat command)
* alacritty
* steam  (desktop launcher fails https://www.reddit.com/r/Fedora/comments/1kk0gak/psa_steam_crashing_loop_fix/ ; unsetting DRI_PRIME env variable)
* python3-ipykernel (interactive python kernel for jupyter)
* Requirements of jupyter-nbconvert to pdf:  texlive-collection-fontsrecommended, texlive-collection-latexextra
* ffmpegthumbnailer (used to create video preview in lf)
* fontawesome-fonts-all (icons for latex documents)
* xdotool
* transmission (torrenting client)
* rhythmbox-alternative-toolbar (compact toolbar that allows theming)
* speedtest-cli
* inxi (system information tool)
* waybar
* dmenu
* flameshot (screenshot utility)
* dunst (notification daemon for hyprland)
* rocm-smi (dependency for btop to show gpu info)
* xev (keyboard event detection utility)
* python3-virtualenvwrapper (for ccds virtual env management)
* hyprlock, hyperidle (hyprland screen lock on timeout)


## Copr
* lf  (via `dnf copr enable pennbauman/ports;  dnf install lf`)
* mtn (video previewer for lf https://copr.fedorainfracloud.org/coprs/wahibre/mtn)
* yazi (terminal file manager) via lihaohong/yazi 
* cosmic desktop environment (https://github.com/pop-os/cosmic-epoch)
* solopasha/hyprland (https://copr.fedorainfracloud.org/coprs/solopasha/hyprland) for utilities (hyprpaper) not yet packaged by Fedora



## RPM
* msttcore-fonts (https://linuxcapable.com/install-microsoft-fonts-on-fedora-linux/)



## Flatpak
* VideoDownloader
* LocalSend (file transfer)
* Shortwave (music streaming)
* Resources (system monitor)
* Cavalier (music visualizer)
* Blanket (ambient sound player)
* gdm-settings (customize gdm)
* gpt4all
* quadrapassel

## Pip
* jupyterlab (https://shape.host/resources/step-by-step-guide-on-installing-jupyterlab-on-fedora-39)




## Pipx
* virtualenv
* cookiecutter  (project templates https://github.com/cookiecutter/cookiecutter)
* cookiecutter-data-science (comes with `ccds` binary to setup new data science project)




## Cargo
* vivid (generator for LS_COLORS env variable; used by ls, tree, etc)
* Starship prompt
* eza
* hyprsome (workspace configuration in hyprland)





## Github
* eza-themes
* JK's kickstarter.nvim  (symlinked folder to ~/.config/nvim)
* keyd (key remapping especially for Wayland.  built from source.  daemon runs via systemctl.  creating config in dotfiles repo and sim-linking to /etc/keyd/default.conf)
* Alternative kitty icon (https://github.com/k0nserv/kitty-icon; Icon field of /usr/share/applications/kitty.desktop changed to path of desired icon)
* hyprshot (screenshot utility for hyprland) executable linked to /usr/local/bin


## Other installation methods
* brave-browser  (via `dnf config-manager addrepo ...` command)
* nerd fonts (nerdfonts.com/font-downloads; extracted to `/usr/share/fonts/`)
* signal (using `config-manager add repo ...` method from https://software.opensuse.org/download.html?project=network:im:signal&package=signal-desktop)
* Pycharm:  Downloaded compressed files abd extracted to /usr/local/share/.  Soft linked executable to /usr/local/bin/.  Created launcher via Tools -> Create Desktop Entry within PyCharm.
* lua compiler:  Via build instructions https://www.lua.org/download.html.  Extracted files moved to /usr/local/share/.  Binary soft-linked to /usr/local/bin/
* pypy3 (faster implementation of python):  https://pypy.org/download.html
* geekbench6 (PC benchmarking tool):  Downloaded executabl
* Bash scripts to increment/decrement workspaces in hyprland https://github.com/sopa0/hyprsome/issues/14  installed to /usr/local/bin/



## Browser extensions
* vimium
* bitwarden
* dark reader
* tabliss
* bookmark sidebar
* xBrowserSync





## Gnome shell extensions






## System mods
* Add ssh key to agent via `ssh-add`
* Change location of XDG_MUSIC_DIR in ~/.config/user-dirs.dirs to ~/Documents/Music
* Disabling audio power save via https://itsfoss.com/buzzing-noise-speaker-linux/
* Forcing brave to use wayland rather than xwayland via brave://flags/#ozone-platform-hint


## Already installed (perhaps by distro or as a dependency for something else)
* fzf
* ripgrep 
* tree
* gnome-maps
* ffmpeg
* npm
* stockfish (chess engine) 
