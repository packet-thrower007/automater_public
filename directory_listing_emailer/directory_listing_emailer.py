#!/usr/bin/env python3
import smtplib
from email.message import EmailMessage
import subprocess
import time
import calendar
import os
import re

#rootdir = "/backups/cisco/"
#regex = re.complile('(.*zip$)|(.*conf$)')
#rx = '(.*zip$)|(.*conf$)'

#for root, dirs, files in os.walk(rootdir):
#       for file in files:
#               if re.match(rx,file):
#                       print(file)



####Construct Date in MMM format

for x in range (1,13):
        print(x, ":", calendar.month_abbr[x], time.strftime("%d"))

#print(x)


####ls -l on /backups/cisco/

output = subprocess.check_output("ls -l /backups/cisco/", shell=True)
output = output.decode("utf-8")

print(output)




def e_mail():
        msg = EmailMessage()
        msg.set_content("Test")
        msg['Subject'] = "E-Mail via "
        msg['From'] = test@aol.com
        msg['To'] = test@aol.com
        #msg['Bcc'] = "", "", ""
#        server = smtplib.SMTP(".outlook.com")
        server = smtplib.SMTP("8.8.8.8")
        server.send_message(msg)
        server.quit()

for i in range(1):
        e_mail()
