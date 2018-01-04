#!/usr/bin/python3

#author - Animcogn
#purpose - connect to database, send query, then nest results in lists.
#last edit - 1/3/2018

#database interfacing
import sqlite3
#pytables
import tables
import numpy

#Main function to be called elsewhere
def queryDatabase(databasePath, sqlCommand):
    #Connect to database
    try:

        conn = sqlite3.connect(databasePath)
        c = conn.cursor()
    except Exception as e:
        print("Unable to connect to database: " + str(e))

    #Pytables to store information for easy access
    class NearbyDevices(IsDescription):
        name        = String()
        first_seen  = String()
        last_seen   = String()

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



    except Exception as e:
        print("Unable to query database: " + str(e))
    #conn.close()

#def
