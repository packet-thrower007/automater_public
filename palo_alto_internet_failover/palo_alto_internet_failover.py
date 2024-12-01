#!/usr/bin/env python

from netmiko import ConnectHandler
from netmiko.paloalto.paloalto_panos import PaloAltoPanosSSH
import time
from getpass import getpass
import pyfiglet
import re
from datetime import date
import logging
from datetime import datetime

file_object = open(r"log.txt")

# YY/mm/dd
############to test change today to the date of the last failover and comment out the real today##
#today = "2023/08/15"


today = date.today().strftime("%Y/%m/%d")
now = datetime.now()
current_time = now.strftime("%H:%M:%S")


# Log File
file1 = open('/automater/internet_failover/log.txt', 'a')

L = today
evaluation_false = "Stable" + "   " + (L) + " " + (current_time) + "\n"


# Writing a string to file
file1.write(evaluation_false)


# Closing file
file1.close()

#Banner
ascii_banner = pyfiglet.figlet_format("Internet Failover Detect/Fix Script Creator: Me myself and i 2023", font = "doom", justify="center", width = 125 )
print(ascii_banner)



#Credintal/Userinput
username = "test"
password = "test"

paloalto = {
        'device_type': "paloalto_panos",
        'ip': "1.1.1.1",
        'username': username,
        'password': password,
#        'session_log': "output.txt",
    }

ssh = ConnectHandler(**paloalto)

command = ["show log system opaque contains 'Path monitoring failed for static route destination 0.0.0.0/0 with'"]


for i in command:
        confmode = ssh.send_command(i, expect_string=r">")

        #The regex pattern that we created
        pattern = "\d{4}[/-]\d{2}[/-]\d{2}"

        #Will return all the strings that are matched
        dates = re.findall(pattern, confmode)

        print(today)
        for j in dates:
             if today == j:
                   file1 = open('/automater/palo_alto_internet_failover/log.txt', 'a')

                   L = today
                   evaluation_true = "Failover" + " " + (L) + " " + (current_time) + "\n"

                   # Writing a string to file
                   file1.write(evaluation_true)

                   # Closing file
                   file1.close()

                   ike_sa = ["test vpn ike-sa gateway test-1", 
                   "test vpn ike-sa gateway test-2"]

                   ipsec_sa = ["test vpn ipsec-sa tunnel test-1",  
                   "test vpn ipsec-sa tunnel test-2"]

                   udp_sessions = ["clear session all filter source 192.168.1.1",
                   "clear session all filter source 192.168.1.2"]

                   show_sessions = ["show session all filter source 192.168.1.1",
                   "show session all filter source 192.168.1.2"]

                   for i in ike_sa:
                       confmode = ssh.send_command(i, expect_string=r">")
                       print(confmode)
#                      print("sleeping for 1.0 seconds")
                       time.sleep(1.0)
                       print(i[24:],"Bounced")

                   for i in ipsec_sa:
                       confmode = ssh.send_command(i, expect_string=r">")
                       print(confmode)
#                      print("sleeping for 1.0 seconds")
                       time.sleep(1.0)
                       print(i[25:], "Bounced")

                   for i in udp_sessions:
                       confmode = ssh.send_command(i, expect_string=r">")
                       print(confmode)
                   for j in show_sessions:
                       show = ssh.send_command(j, expect_string=r">")
                       print(show)
                   ssh.disconnect()


ssh.disconnect()
