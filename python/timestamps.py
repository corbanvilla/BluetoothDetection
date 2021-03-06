#!/usr/bin/python3

#author - Animcogn
#purpose - take database query, regex for timestamps, calculate time imbalances
#created - 1/4/2018
#last edit - 1/8/2018

#pytables
from tables import *
from numpy import *
#timestamps
import subprocess
from datetime import datetime
#regular expressions
import re
#database storing
import database as db

#Grab query, filter times, and print
def fetchTimes(results):
    for row in results:
        first_seen = row[3]
        last_seen = row[4]
        first_seen = regexStamp(first_seen)
        last_seen = regexStamp(last_seen)
        rating = algorithm(first_seen, last_seen, fetchDate())

        if rating >= 1: #filter out noise
            db.insertToDatabase([row[0], row[1], row[2], first_seen, last_seen, rating])

#Ask bash for exact times
def fetchDate():
    current_date = subprocess.check_output\
    ("date +'%Y-%m-%d'", shell=True).decode().strip()
    current_time = subprocess.check_output\
    ("date +'%H:%M:%S'", shell=True).decode().strip()
    return (current_date + " " + current_time)

#sort for exact parts in timestamp for comparing
def regexStamp(string):
    device_date = re.match('.+?(?=T)', string)
    device_date = (str(device_date.group(0)))

    re1='.*?'
    re2='((?:(?:[0-1][0-9])|(?:[2][0-3])|(?:[0-9])):(?:[0-5][0-9])(?::[0-5][0-9])?(?:\\s?(?:am|AM|pm|PM))?)'
    rg = re.compile(re1+re2,re.IGNORECASE|re.DOTALL)
    device_time = rg.search(string)
    device_time = (device_time.group(1))

    timestamp = (device_date + " " + device_time)
    return(timestamp)

#timestamp 1 - before | timestamp 2 - after
def timeDifference(timestamp1, timestamp2, humanReadable=True):
    t1 = datetime.strptime(timestamp1, "%Y-%m-%d %H:%M:%S")
    t2 = datetime.strptime(timestamp2, "%Y-%m-%d %H:%M:%S")

    #Subtrack times
    difference = (t2 - t1)
    #Convert to days, hours
    if humanReadable:
        hours = round(difference.seconds / 3600, 2)
        days = (difference.days)
        return(days, hours)
    else:
        #Convert to minutes and combine days and seconds
        minutes = round(((difference.days * 24 * 60) + difference.seconds / 60), 2)
        return(minutes)

#decide threat rating by timestamps
def algorithm(first_seen, last_seen, current_time): #need to tweak algorithm later in
    first_to_last = (timeDifference(first_seen, last_seen, False))
    last_to_current = (timeDifference(last_seen, current_time, False))

    if first_to_last > 144 and last_to_current < 60: # <--- change these values to adjust detection
        alert = 4
        return(alert)

    elif first_to_last > 180 and last_to_current < 60:
        alert = 3
        return(alert)

    elif first_to_last > 60 and last_to_current < 60:
        alert = 2
        return(alert)

    elif first_to_last > 15 and last_to_current < 60:
        alert = 1
        return(alert)

    else:
        alert = 0
        return(alert)
