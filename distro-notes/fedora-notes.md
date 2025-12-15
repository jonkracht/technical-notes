# fedora

## Buzzing speakers when no audio output

`cat /sys/module/snd_hda_intel/parameters/power_save`

If something other than zero, probably the issue.

Change value to 0 in power_save file.


To make persistent, create /etc/modprobe.d/audio_disable_powersave.conf and include:
`options snd_hda_intel power_save=0`


Adding `power_save_controller=N` to /etc/modprobe.d/audio_disable_powersave.conf

Gets overwritten by something else on reboot.

Solution: Joe on 4/26
https://discussion.fedoraproject.org/t/unable-to-automatically-set-snd-hda-intel-power-save-to-0/141784/15


sudo mkdir /etc/tuned/profiles/overrides

Create a new file tuned.conf in the overrides directory with the following contents.
```
[audio]
timeout=0
```

Edit /etc/tuned/post_loaded_profile and add the directory name that was created earlier.
Reboot system or just tuned daemon.
