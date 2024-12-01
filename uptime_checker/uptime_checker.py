#!/usr/bin/env python3

# All pre-installed besides Netmiko.
from csv import reader
from netmiko import ConnectHandler
from ping3 import ping, verbose_ping 
import getpass
import os
from datetime import datetime
import time
from datetime import date

# Checks if the folder exists, if not, it creates it.
if not os.path.exists('/automater/uptime_checker/uptime/cisco'):
    os.makedirs('/automater/uptime_checker/uptime/cisco')

# Current time and formats it to the North American time of Month, Day, and Year.
now = datetime.now()
dt_string = now.strftime("%m-%d-%Y")


# Log File.
file_path = "/automater/uptime_checker/uptime/cisco/" + dt_string + ".conf"
log = open(file_path, "a")


# Gives us the information we need to connect.





def uptime_checker(host, username, password):
    time.sleep(5)
    cisco_ios = {
        'device_type': 'cisco_ios',
        'host': host,
        'username': username,
        'password': password,
#        'secret': enable_secret,
    }
    # Creates the connection to the device.
    try:
        net_connect = ConnectHandler(**cisco_ios)
        net_connect.enable()

        # Sends Command.
        uptime = net_connect.send_command("show ver | i uptime")

        # Log File.
#        file_path = open("/automater/uptime_checker/cisco/" + dt_string + ".conf", "a")
        log.write(uptime)
        log.write("\n")
#        log.close()

    except:
        pass


# Gets the CSV file name, and grabs the information from it.
with open('/automater/uptime_checker/ios_devices.csv') as csvfile:
    csv_reader = reader(csvfile)
    list_of_rows = list(csv_reader)
    rows = len(list_of_rows)
    while rows >= 2:
        rows = rows - 1
        ip = list_of_rows[rows][0]
        ip_ping = ping(ip)
        if ip_ping == None:
            filename = "DOWN-DEVICES-IOS" + ".conf"
            downDeviceOutput = open("/automater/uptime_checker/uptime/cisco/" + filename, "w")
            downDeviceOutput.write(str(ip) + "\n")
            print(str(ip) + " is down!")
        else:
            uptime_checker(list_of_rows[rows][0], list_of_rows[rows][1], list_of_rows[rows][2])




while True:
        date = date.today()
        time.sleep(5)
        time_long  = datetime.now()
        time_short = str(time_long.strftime("%H:%M"))
        if time_short == "00:30":
                uptime_checker(list_of_rows[rows][0], list_of_rows[rows][1], list_of_rows[rows][2])
                print("Sleeping for 60 Seconds")
                time.sleep(60)
        else:
                pass
