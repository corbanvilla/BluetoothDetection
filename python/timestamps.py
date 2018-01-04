#!/usr/bin/python3

#author - Animcogn
#purpose - connect to database, send query, then nest results in lists.
#created - 1/4/2018
#last edit - 1/4/2018

#pytables
from tables import *
from numpy import *
#timestamps
import subprocess
import datetime
#regular expressions
import re

#Ask bash for exact times
def fetchDate():
    current_date = subprocess.check_output("date +'%Y-%m-%d'", shell=True).decode().strip()
    current_time = subprocess.check_output("date +'%H-%M-%S'", shell=True).decode().strip()
    return current_date, current_time;

#Pytables to store information for easy access
#class NearbyDevices(IsDescription):
#    name        = StringCol(16)
#    first_seen  = StringCol(16)
#    last_seen   = StringCol(16)

#h5file = open_file("nearby_devices", mode="w", title="storage of devices found")
#group = h5file.create_group("/", "devices", "Device information")
#table = h5file.create_table(group, 'readout', NearbyDevices, "Bluetooth Devices")
#print(h5file)

#Smartwatch = table.row

#Grab query, filter times, and print
def fetchTimes(results):
    for row in results:
        name = row[0]
        firstSeen = row[1]
        lastSeen = row[2]
        print ("name=%s, first seen=%s, last seen=%s" \
        % (name, firstSeen, lastSeen))

        device_date = re.match('.+?(?=T)', lastSeen)
        print(str(device_date.group(0)))

        re1='.*?'
        re2='((?:(?:[0-1][0-9])|(?:[2][0-3])|(?:[0-9])):(?:[0-5][0-9])(?::[0-5][0-9])?(?:\\s?(?:am|AM|pm|PM))?)'
        rg = re.compile(re1+re2,re.IGNORECASE|re.DOTALL)
        m = rg.search(lastSeen)
        print(m.group(1))
