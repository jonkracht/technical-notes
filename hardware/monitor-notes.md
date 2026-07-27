# monitors

## Refresh rate

Measures frames per second.

Must be able to keep up with number of frames output by GPU.

60 Hz is the lowest and 240 is the highest.


## Response time

Time a pixel takes to change color.  Typically 1 - 3ms.



## Resolution

Measures number of pixels

1080p is baseline
1440 is known as QHD
4k is to quality; more expensive


## Brightness

Measured in nits


## Contrast ratio


## Adaptive sync

Mathces monitor refresh rate to GPU frame rate

NVIDIA:  Gsync
AMD:  FreeSync


TODO:  How is variable refresh rate different?



## Monitor technologies

### In-plane switching

### VA

### TN 

### OLED
Best and most expensive.







## Monitor problems


### Visual static problem

#### Symptoms
* visual static when switch workspaces, exploding windows
* audio crackling at similar times as visual static, changing volume triggers
* image temporarily appears on wrong screen
* visual static does not appear on screen recording


### Hardware specs

#### GPU
  XFX Speedster SWFT210 Radeon RX 7600 XTProcessor:  AMD Ryzen 9 7900X x 24

#### Ubuntu 24.04.02:Gnome 46
* Kernel 6.8.0-52-generic  (released March 2024; as of Feb 2025, 6.13 is most recent)(Ubuntu 24.10 uses 6.11 kernel)
* Mesa 24.2.8   (Mesa is an open source implementation of graphics API specifications like Open GL, vulkan)
Up to date mesa driver option:  https://launchpad.net/~oibaf/+archive/ubuntu/graphics-drivershttps://itsfoss.com/install-mesa-ubuntu/


#### Misc

Monitors run at 60 Hz.
Tearing?
Switched to a supposedly higher quality displayport cable and symptoms seem unchangedUpgraded OS to newer kernel  (Fedora 42 on 6.14.9)
Fractional scaling at 150%?

AMD FreeSync help?
Try disabling freeSYnc in monitor's settings
Screen refresh rate?
Occurs on both monitors but more often on the left



### Monitor not waking up after system idle

Settomg "Fast Wakeup" to ON on both Dell monitors 
