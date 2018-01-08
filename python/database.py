#!/usr/bin/python3

#author - Animcogn
#purpose - create database for storing suspicious devices to be used
#          later in project, this list will contain suspicion rating,
#          when it was first seen, and last seen.
#created - 1/5/2018
#last edit - 1/8/2018

#sqlite
import sqlite3
from pathlib import Path # <-- check if database does not exist,
                         #     if so, create tables, etc, etc

def initiateDatabase():
    debug = True
    db_path = Path("suspicious_devices.db")
    if not db_path.is_file(): #if does not exist, format / create tables
        if debug: print("database does not exist, creating / formatting")
        conn = sqlite3.connect("suspicious_devices.db")
        c = conn.cursor()
        c.execute('''CREATE TABLE devices (
                     uuid int NOT NULL,
                     name varchar(255),
                     vendor varchar(255),
                     first_seen,
                     last_seen,
                     threat_rating int NOT NULL,
                     PRIMARY KEY (uuid))''')
        conn.commit()
        conn.close()
def insertToDatabase(record): #one record at a time please :)
    conn = sqlite3.connect("suspicious_devices.db")
    c = conn.cursor()
    c.execute("REPLACE INTO devices VALUES (?,?,?,?,?,?)", record)
    conn.commit()
    conn.close
