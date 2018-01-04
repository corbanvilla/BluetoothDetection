#!/usr/bin/python3

#author - Animcogn
#purpose - connect to database, send query, then nest results in lists.
#created - 1/4/2018
#last edit - 1/4/2018

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
