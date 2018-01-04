#!/usr/bin/python3

#author - Animcogn
#purpose - connect to database, send query, then nest results in lists.
#created - 1/3/2018
#last edit - 1/4/2018

#database interfacing
import sqlite3
#pytables
from tables import *
from numpy import *
#timestamps
import subprocess
import datetime
#regular expressions
import re

def fetchDate():
    current_date = subprocess.check_output("date +'%Y-%m-%d'", shell=True).decode().strip()
    current_time = subprocess.check_output("date +'%H-%M-%S'", shell=True).decode().strip()
    return current_date, current_time;




#Main function to be called elsewhere
def queryDatabase(databasePath, sqlCommand):
    #Connect to database
    try:

        conn = sqlite3.connect(databasePath)
        c = conn.cursor()
    except Exception as e:
        print("Unable to connect to database: " + str(e))

    #Query for data, then store in list
    try:
        c.execute(sqlCommand)
        results = c.fetchall()
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

    except Exception as e:
        print("Unable to query database: " + str(e))
    conn.close()

#def
