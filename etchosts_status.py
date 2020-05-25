#!/usr/bin/env python3
import os
import re
import json

# your hosts file or similarly-formatted file
# example
#10.0.0.1 router
hostsfile = '/etc/hosts'

# output file with optional path
filePath = 'Output.txt';
 
# As file at filePath is deleted now, so we should check if file exists or not not before deleting them
if os.path.exists(filePath):
    os.remove(filePath)

with open(hostsfile, 'r') as f:
    hosts = f.readlines()

# ignore commented or blank lines
hostlines = [host.strip() for host in hosts
    if not host.startswith('#') and host.strip() != '']

for i in hostlines:
    # parse
    splitted = re.split(' +|	+', i)
    # use IPv4 lines
    if re.match(r'^[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}$',splitted[0]):
        response = os.system("ping -c 1 -w2 " + splitted[0] + " > /dev/null 2>&1")
        if response == 0:
            splitted.append("UP")
        else:
            splitted.append("DOWN")
        d1 = {}
        t1 = {"ip": splitted[0], "host": splitted[1], "status": splitted[2]}
        d1.update(t1)
        d1 = json.dumps(t1, indent=4) + ","
        with open(filePath, "a+") as text_file:
            text_file.write(str(d1))
# Make clean parse-able json
print(os.system("sed -i '$ s/.$/]/' " + filePath))
print(os.system("sed -i '0,/{/s//[{/' " + filePath))

