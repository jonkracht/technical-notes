# Notes for the rhythmbox music player

[Rhythmbox homepage](https://wiki.gnome.org/Apps/Rhythmbox)





## Associated files


On Pop22.04, stored at `${HOME}/.local/share/rhythmbox/`



| File                | Description                                                                                                                                   |
| ---                 | ---                                                                                                                                           |
| `rhythmdb.xml`      | Dictionary-like representation of each file in the music library; contains file paths, song details (title, artist, album, compression, etc.) |
| `playlists.xml`     | Contains information of user-created playlists                                                                                                |
| `podcast-timestamp` | Haven't used rhythmbox for podcast listening so currently a blank file -- perhaps tracks listening progress?                                  |





## Shortcuts


|                         Action |           Shortcut |
|                            --- |                --- |
| Move to currently playing song |         `CTRL + J` |
|                  Play or Pause |         `CTRL + P` |
|    Move cursor to search field |          `ALT + S` |
|                 Show song info |      `ALT + ENTER` |
|    Skip forward/backward by 5s | `ALT + RIGHT/LEFT` |




## Export playlist to a file
* In menu with hamburger-looking icon, View -> Show Source Toolbar 
* A new toolbar should appear 
* Playlist -> Save to File...
* Three formats available:  m3u, pls, xspf
* "pls" retains playlist name when re-loading




## Plugins


### Easy effects

[Easy Effects Homepage](https://github.com/wwmm/easyeffects)

With pipewire increasingly replacing pulseaudio in new Linux releases, PulseEffects package was renamed EasyEffects.

Can apply effects to any audio stream (music, web page audio, microphone)

#### Some effects

* Equalizer: Got some presets from [JackHack96 github](https://github.com/JackHack96/EasyEffects-Presets)







## Miscellaneous

* rhythmbox can be controlled via the command line using rhythmbox-client:
    * [rhythmbox-client info](https://linux.die.net/man/1/rhythmbox-client)



* Encountered error message  "Couldn't find files.  XML file corrupted."  

Deleted it (`rm ~/.local/share/rhythmbox/rhythmdb.xml`) file was automatically recreated by rhythmbox and probably error message went away







## TODO
*  Can't jump to search field when it is not open
