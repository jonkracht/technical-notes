systemd-network and ifupdown are also used commonly to handle network connections

Can turn on/off by editting /etc/NetworkManager/NetworkManager.conf
Turn on by setting:  managed=false
And vice versa for OFF

Only one networking service should be enabled at each time


Tools included with NetworkManager:
nmcli - command line tool to configure
nmtui - a terminal user interface (TUI)
nm-applet - applet for GNOME desktop environments


nmcli:
Show all past connections:  nmcli c show
Include the --active flag to show presently available
Edit current connection parameters:  nmcli c modify <connect_id> <param> <val> 

Show available wireless networks  
`nmcli dev wifi`

Tool for mapping network strength?
