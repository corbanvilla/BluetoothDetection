#!/usr/bin/python3

#author - Animcogn
#purpose - call all other modules
#created - 1/3/2018
#last edit - 1/3/2018

#query database
import query
#extract timestamps from query
import timestamps
#initialize and insert to database
import database as db

def main():
    db.initiateDatabase()
    results = query.queryDatabase()
    timestamps.fetchTimes(results)
main()
