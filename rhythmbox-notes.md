# rhythmbox notes 

[Rhythmbox homepage](https://wiki.gnome.org/Apps/Rhythmbox)





## Associated files


Stored at `${HOME}/.local/share/rhythmbox/`



| File | Description  |
|--- | --- |
|`rhythmdb.xml`| Contains information for files in music library (such as paths and song info) |
| `playlists.xml`| Contains user information of user-created playlists|
|`podcast-timestamp`| I've never used rhythmbox to listen to a podcast  so currently a blank file...|





## Shortcuts


| Action | Shortcut  |
|--- | --- |
| Move to currently playing song| `CTRL + J`|
| Play or Pause| `CTRL + P`|
| Move cursor to search field| `ALT + S`|
| Show song info| `ALT + ENTER`|
| Skip forward/back in a song| `ALT + RIGHT/LEFT`|




## Export playlist to a file
In the hamburger-looking icon: View -> Show Source Toolbar.  
New toolbar appear.  Playlist -> Save to File...

Three formats available:  m3u, pls, xspf
Use pls to retain playlist name when re-loading


## Plugins


## Miscellaneous


* Error message:  Couldn't find files.  XML file corrupted.  

Remove it:  `rm ~/.local/share/rhythmbox/rhythmdb.xml`

* Use `rhythmbox-client` to control and query info from rhythmbox on the command line

[rhythmbox-client info](https://linux.die.net/man/1/rhythmbox-client)


# Easy effects

[Easy Effects Homepage](https://github.com/wwmm/easyeffects)

With pipewire increasingly replacing pulseaudio in new Linux releases, PulseEffects package was renamed EasyEffects.

Can apply effects to any audio stream (music, web page audio, microphone)

## Some effects

* Equalizer: Got some presets from [JackHack96 github](https://github.com/JackHack96/EasyEffects-Presets)

