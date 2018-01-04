#!/usr/bin/python3

#author - Animcogn
#purpose - call all other modules
#created - 1/3/2018
#last edit - 1/3/2018

#query database
from query import queryDatabase
#import timestamps

#Defininitions
databasePath = '/home/animcogn/blue_hydra.db'
sqlCommand = "SELECT name, created_at, updated_at FROM \
              blue_hydra_devices WHERE status = 'online';"

def main():
    queryDatabase(databasePath, sqlCommand)

main()
