#!/usr/bin/env python3
from netmiko import ConnectHandler
from datetime import datetime
import time
import csv

while True:
    time.sleep(3600)

    with open('/automater/clear_ip_arp/devices.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:

                device = {row[0]}
                next_hop = row[1]

                print(device,next_hop)
                line_count += 1



    for ip in device:
         device = {
         "host": ip,
         "device_type": "cisco_xe",
         "username": "test",
         "password": "test",
         "secret": "",  # Enable password (If applicable)
    }

    # Connect to the device
    conn = ConnectHandler(**device)
    # Check if connected in user mode and enter enable mode
    # Make sure you have the "secret": "xxxx" is set in device var
    if not conn.check_enable_mode():
         conn.enable()

    # Notice send_command_timing method here


    clear_process = conn.send_command_timing("clear ip arp " +  str(next_hop))
    # Disconnect to clear the vty line
    conn.disconnect()
