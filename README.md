# dakboard
Collection of scripts to manage home dakboard

# rpi-hdmi.sh
Turn HDMI port on/off on cron schedule

# etchosts_status.py
Parse a file like /etc/hosts and output a status file with status UP or DOWN depending on the results of a ping. Used to feed dakboard's json scrape.

# lan_status.py
Creates json file to display current status of LAN devices and processes. utput example:
[{"time": "10:59 AM"
},{"pihole": "Up"
},{"garage": "Up"
},{"nas": "Up"
},{"temp": "43.4°"
},{"uptime": "0.14 0.13 0.11"}]

# alias
alias to refresh chromium page for dakboard refresh

# startup
file to place at ~/.config/lxsession/LXDE-pi/autostart to manage boot
