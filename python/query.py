#!/usr/bin/python3

#author - Animcogn
#purpose - connect to blue_hydra database, send query, then return results.
#created - 1/3/2018
#last edit - 1/8/2018

#database interfacing
import sqlite3

#Defininitions
databasePath = '/home/animcogn/blue_hydra.db'
sqlCommand = "SELECT uuid, name, vendor, created_at, updated_at \
              FROM blue_hydra_devices WHERE status = 'online';" #Query for data from blue_hydra

#Main function to be called elsewhere
def queryDatabase():
    #Connect to database
    try:
        conn = sqlite3.connect(databasePath)
        c = conn.cursor()

        #Query for data, then store in list
        try:
            c.execute(sqlCommand)
            results = c.fetchall()
            return results
            conn.close() #Close connection with database
        except Exception as e:
            print("Unable to query database: " + str(e))
    except Exception as e:
        print("Unable to connect to database: " + str(e))
