#!/usr/bin/env python
from netmiko import ConnectHandler
from netmiko.paloalto.paloalto_panos import PaloAltoPanosSSH
import time
from getpass import getpass
import pyfiglet


#Banner
ascii_banner = pyfiglet.figlet_format("911 - Kill DMZ Script Creator: Jonathan Davis February 2023", font = "doom", justify="center", width = 125 )
print(ascii_banner)



#Credentials/User input
username = input("Username: ")
password = getpass("Password: ")

paloalto = {
        'device_type': "paloalto_panos",
        'ip': "8.8.8.8",
        'username': username,
        'password': password,
#        'session_log': "output.txt",
    }

ssh = ConnectHandler(**paloalto)


print("This scrupt will disable the DMZ Routed interface, this takes place quickly however the commit process will take 60 seconds")


commands = ["configure",
"set network interface ethernet ethernet1/19 link-state down",
"commit"]


for i in commands:
        confmode = ssh.send_command(i, expect_string=r"#")
        print("sleeping for 1.0 seconds")
        time.sleep(1.0)
        print(i,"Executed")
