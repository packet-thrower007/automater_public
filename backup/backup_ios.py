# All pre-installed besides Netmiko.
from csv import reader
from datetime import date, datetime
from netmiko import ConnectHandler
from ping3 import ping, verbose_ping 
import getpass
import os
import time
from datetime import date



# Change this value to the time cisco_ios devices should be backed up.
backup_time = "00:00"

def get_saved_config(host, username, password):
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

    # Gets and splits the hostname for the output file name.
    hostname = net_connect.send_command("show ver | i uptime")
    hostname = hostname.split()
    hostname = hostname[0]

    # Creates the file name, which is the hostname, and the date and time.
    fileName = hostname + ".conf"

    # Creates the text file in the backup-config folder with the special name, and writes to it.
    backupFile = open("/automater/backup/backups/cisco/" + fileName, "w+")
    backupFile.write(output)
    print("Outputted to " + fileName)
    net_connect.disconnect()


while True:
        date = date.today()
        time.sleep(5)
        time_long  = datetime.now()
        time_short = str(time_long.strftime("%H:%M"))
        if time_short == backup_time:
#           Sleep for 60 seconds, this prevent backups running multiple times in the 60 second time
#            time.sleep(60)
            with open('/automater/backup/backup_ios.csv') as csvfile:
                csv_reader = reader(csvfile)
                list_of_rows = list(csv_reader)
                rows = len(list_of_rows)
                while rows >= 2:
                    rows = rows - 1
                    ip = list_of_rows[rows][0]
                    ip_ping = ping(ip)
                    if ip_ping == None:
                        fileName = "DOWN-DEVICES-IOS" + ".conf"
                        downDeviceOutput = open("/automater/backup/backups/cisco/" + fileName, "a")
                        downDeviceOutput.write(str(ip) + " " + "is down! on " + str(date) + "\n")
                        print(str(ip) + " is down!")
                    else:
                        try:
                           get_saved_config(list_of_rows[rows][0], list_of_rows[rows][1], list_of_rows[rows][2])
                        except:
                           pass
else:
    pass
