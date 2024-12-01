#!/usr/bin/env python
from netmiko import ConnectHandler
from netmiko.paloalto.paloalto_panos import PaloAltoPanosSSH
import time
from getpass import getpass
import pyfiglet




#Banner
ascii_banner = pyfiglet.figlet_format("Palo Alto network Bounce Problematic Tunnels Script Creator: Jonathan Davis January 2023", font = "doom", justify="center", width = 125 )
print(ascii_banner)



#Credintal/Userinput
username = input("Enter Username: ")
password = getpass("Enter Password: ")

paloalto = {
        'device_type': "paloalto_panos",
        'ip': "8.8.8.8",
        'username': username,
        'password': password,
#        'session_log': "output.txt",
    }

ssh = ConnectHandler(**paloalto)

ike_sa = ["test vpn ike-sa gateway TEST-0",
"test vpn ike-sa gateway TEST-1", 
"test vpn ike-sa gateway TEST-2"]


ipsec_sa = ["test vpn ipsec-sa tunnel TEST-0",
"test vpn ipsec-sa tunnel TEST-1",
"test vpn ipsec-sa tunnel TEST-2"]

for i in ike_sa:
        confmode = ssh.send_command(i, expect_string=r">")
        print(confmode)
#       print("sleeping for 1.0 seconds")
        time.sleep(1.0)
        print(i[24:],"Bounced")

for i in ipsec_sa:
        confmode = ssh.send_command(i, expect_string=r">")
        print(confmode)
#       print("sleeping for 1.0 seconds")
        time.sleep(1.0)
        print(i[25:], "Bounced")
