import os,sys
import time

time.sleep(10)

with open('/home/pi/api/away') as f:
	status = f.readline()

if status == "away":
	os.system('sudo /home/pi/rpi-hdmi.sh off')
else:
	os.system('sudo /home/pi/rpi-hdmi.sh on')
