# -*- coding: utf-8 -*-
import os
import re
import psutil
from gpiozero import CPUTemperature
import datetime
import decimal
#time
currentDT = datetime.datetime.now()
print("[{\"time\": \"" + currentDT.strftime("%-I:%M %p") + "\"")
#check pihole up
if "pihole-FTL" in (p.name() for p in psutil.process_iter()):
        print("},{\"pihole\": \"Up\"")
else:
        print("},{\"pihole\": \"Down\"")
#check garadget
response_garage = os.system("ping -c 1 -w2 " + "10.0.0.31" + " > /dev/null 2>&1")
if response_garage == "0":
	print("},{\"garage\": \"DOWN\"")
else:
	print("},{\"garage\": \"Up\"")
#check NAS
if os.path.isdir("/media/NAS/Media/") == True & os.path.isdir("/media/NAS2/Media/") == True & os.path.isdir("/media/NAS3/Backup/") == True:
	print("},{\"nas\": \"Up\"")
else:
	print("},{\"nas\": \"Down\"")
#get temp
cpu = CPUTemperature()
#temp=str(cpu.temperature)
temp=cpu.temperature
decimal.getcontext().rounding = decimal.ROUND_DOWN
temp2=decimal.Decimal(temp)
temp3=round(temp2,1)
temp4=str(temp3)
degree_sign= "°"
print("},{\"temp\": \"" + temp4 + degree_sign + "\"")
#get uptime load
response_uptime = os.popen("uptime").read()
uptime=response_uptime.split(" ")[-3:]
uptime2=str(uptime).replace("[","")
uptime3=str(uptime2).replace("]","")
uptime4=str(uptime3).replace("'","")
uptime5=str(uptime4).replace("\\n","")
uptime6=str(uptime5).replace(",","")
print("},{\"uptime\": \"" + str(uptime6) + "\"}]")
