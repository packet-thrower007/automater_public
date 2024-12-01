# All pre-installed besides Netmiko.
from csv import reader
from datetime import date, datetime
from netmiko import ConnectHandler
from ping3 import ping, verbose_ping 
import getpass
import os
import time
from datetime import date



def get_mac_address(host, username, password):
    cisco_ios = {
    'device_type': 'cisco_ios',
    'host': host,
    'username': username,
    'password': password,
    }



    # Creates the connection to the device.
    net_connect = ConnectHandler(**cisco_ios)
    net_connect.enable()

    # Gets the running configuration.
    output = net_connect.send_command("show run")

    hostname = net_connect.send_command("show ver | i uptime")
    hostname = hostname.split()
    hostname = hostname[0]

    # Gets and splits the hostname for the output file name.
    ip_sla_hunt = net_connect.send_command("show ip sla summary | s i 8.8.8.8")

    print(ip_sla_hunt + "     " + hostname)
    net_connect.disconnect()

with open('/automater/backup/backup_ios.csv') as csvfile:
    csv_reader = reader(csvfile)
    list_of_rows = list(csv_reader)
    rows = len(list_of_rows)
    while rows >= 2:
        rows = rows - 1
        ip = list_of_rows[rows][0]
        ip_ping = ping(ip)
        if ip_ping == None:
            fileName = "DOWN_IOS_DEVICES" + ".txt"
            downDeviceOutput = open("/automater/ip_sla_hunt/" + fileName, "a")
            downDeviceOutput.write(str(ip) + " " + "is down! on " + str(date) + "\n")
            print(str(ip) + " is down!")
        else:
            try:
                get_mac_address(list_of_rows[rows][0], list_of_rows[rows][1], list_of_rows[rows][2])
            except:
                pass
    else:
        pass

