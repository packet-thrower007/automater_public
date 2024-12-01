#!/usr/bin/python3
import difflib
import os
from zipfile import ZipFile
import datetime as dt
from datetime import datetime, timedelta
import time
from colorama import Fore
import time
from datetime import date

##Time to do a diff_check on files.
diff_checker = "01:00"

##Define date for log.
today_date = str(dt.datetime.now().date())

##Define dates for diff comparison.
yesterday_date = dt.datetime.now().date() - timedelta(days=1)
ereyesterday_date = dt.datetime.now().date() - timedelta(days=2)


##Define Path for zip_file() as a global varable.
today = "/automater/diff_checker/today/"
yesterday = "/automater/diff_checker/yesterday/"
ereyesterday = "/automater/diff_checker/ereyesterday/"


##Create Directory's for diff_comparision.
def create_dirs():
   print(f"{Fore.YELLOW}Step 1: Creating Directorys and Workspace for Diff_Checker{Fore.WHITE}")
   time.sleep(3)
   today = "/automater/diff_checker/today/"
   yesterday = "/automater/diff_checker/yesterday/"
   ereyesterday = "/automater/diff_checker/ereyesterday/"
   list = [today, yesterday, ereyesterday]

   for index in range(len(list)):
      if not os.path.exists(today):
         os.makedirs(today)
         print(" \n")
         print("-----  " + "Creating: " + today)
         time.sleep(3)

      if not os.path.exists(yesterday):
         os.makedirs(yesterday)
         print("-----  " + "Creating: " + yesterday)
         time.sleep(3)

      if not os.path.exists(ereyesterday):
         os.makedirs(ereyesterday)
         print("-----  " + "Creating: " + ereyesterday)
         time.sleep(3)

def zip_file():
   print(f"{Fore.YELLOW}Step 2: Zip File Extraction Process{Fore.WHITE}")
   time.sleep(3)
   with ZipFile("/automater/backup/backups/cisco/" + str(yesterday_date) + ".zip", 'r') as ZipObject:
      ZipObject.extractall(path=str(yesterday))
      print(" \n")
      print("-----  " + "Extracted /automater/backup/backups/cisco/"  + str(yesterday_date) + ".zip" + " " + ">" + " " + "/automater/diff_checker/yesterday/")
      time.sleep(3)
   with ZipFile("/automater/backup/backups/cisco/" + str(ereyesterday_date) + ".zip", 'r') as ZipObject:
      ZipObject.extractall(path=str(ereyesterday))
      print("-----  " + "Extracted /automater/backup/backups/cisco/" + str(ereyesterday_date) + ".zip" + " " +  ">" + " " + "/automater/diff_checker/ereyesterday/")
      time.sleep(3)

def open_files():
   for i in os.listdir(yesterday):
      if i.endswith('.conf'):
         with open(yesterday + "/" + i) as file_2:
            file_2_text = file_2.readlines()
            for j in os.listdir(ereyesterday):
               if j == i:
                  with open(ereyesterday + "/" + j) as file_3:
                     file_3_text = file_3.readlines()
                     for line in difflib.unified_diff(
                        file_3_text, file_2_text, fromfile='file2.txt',
                        tofile='file3.txt', lineterm=''):
                        changes = str(j + ":" + " " + line)
                        print(changes)
                        log = open("/automater/diff_checker/log.txt", "a")
                        log.write(today_date + ":" + " " + changes)
                        log.close()
while True:
        date = date.today()
        time.sleep(5)
        time_long  = datetime.now()
        time_short = str(time_long.strftime("%H:%M"))
        if time_short == diff_checker:
            time.sleep(60)
            create_dirs()
            zip_file()
            open_files()
