import smtplib
from email.message import EmailMessage
from datetime import date,datetime
import subprocess
import time
import calendar
import os
import datetime as dt

#Add/remove from this value as devices get added or removed, total devices + 1 for the zip "program looks at dates.
#Take special care to the date files are created, the logic is to count files with todays date, if you create new files with todays date that count changes.
expected = 51

index = 0

today = dt.datetime.now().date()

check_backups = "05:00"

date = date.today()
time.sleep(5)
time_long  = datetime.now()
time_short = str(time_long.strftime("%H:%M"))


for file in os.listdir('/automater/backup/backups/cisco/'):
    filetime = dt.datetime.fromtimestamp(
        os.path.getctime('/automater/backup/backups/cisco/' + file))
    if filetime.date() == today:
        index += 1


def e_mail():
    msg = EmailMessage()
    msg.set_content("Taking into account the expected value of backup file quanity on XXXX-AUTOMATER-1 and comparing to the file count currently in /automater/back>
    msg['Subject'] = "Cisco Backups Failed"
    msg['From'] = "xxxx-automater-1@test.local"
    msg['To'] = "123@aol.com"
    #msg['Bcc'] = "", "", ""
    server = smtplib.SMTP("8.8.8.8")
    server.send_message(msg)
    server.quit()


def e_mail_good():
    msg = EmailMessage()
    msg.set_content("Successfully backed up:" + " " + str(expected) + " devices")
    msg['Subject'] = "Cisco Backups Success"
    msg['From'] = "xxxx-automater-1@test.local"
    msg['To'] = "123@aol.com"
    #msg['Bcc'] = "", "", ""
    server = smtplib.SMTP("8.8.8.8")
    server.send_message(msg)
    server.quit()


while True:
        date = date.today()
        time.sleep(5)
        time_long  = datetime.now()
        time_short = str(time_long.strftime("%H:%M"))
        if time_short == check_backups:
             time.sleep(60)
             if index == expected:
                  print("Backups Match")
                  e_mail_good()
             elif index != expected:
                  print("Backups ! Match")
                  e_mail()

else:
     pass
