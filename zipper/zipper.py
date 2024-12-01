#!/usr/bin/env python3

#Import Modules needed to run our functions successfully
import zipfile
import os
from datetime import date, timedelta



def compress():

    #Get yesterdays date.
    today = date.today() - timedelta(days=0)
    tdate = today.strftime('%Y-%m-%d')

    #Specify the path to where our files to be compressed are located.
    path = '/automater/backup/backups/cisco'

    fullpath = os.path.join(path,tdate)

    file = zipfile.ZipFile(fullpath + '.zip','w')

    #Change the working directory to where the files are.
    os.chdir('/automater/backup/backups/cisco')

    for x in os.listdir():
        if x.endswith('.conf',):
            file.write(x, compress_type = zipfile.ZIP_DEFLATED)
    file.close()

from datetime import datetime
import time

x = 0


while True:
        time.sleep(5)
        time_long  = datetime.now()
        time_short = str(time_long.strftime("%H:%M"))
        if time_short == "00:10":
                compress()
                print("Sleeping for 60 Seconds")
                time.sleep(60)
        else:
                pass
