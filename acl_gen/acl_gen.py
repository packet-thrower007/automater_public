#ACL Generator
from colorama import init
from termcolor import colored
import csv
import sys
import os
import pyfiglet

print("\n\n ")

print("The first question is to allow for template override, by default type 'any' for Source Network ID")
src_ip = input("What is the Source Network ID/Host & Wildcard: ")

print("\n\nThe second question allow for template override, by default leave 'blank' for Destination Network ID")
dst_ip = input("What is the Destination Network ID/Host & Wildcard: ")


def main():
   menu()


def menu():
    clear_screen()
    title = pyfiglet.figlet_format("Configuration Generator", font = "digital", justify="center")
    print(title)
    choice = input("""
                      01: DATA
                      02: VOIP
                      03: IOT
                      04: FUTURE
                      05: FUTURE
                      06: FUTURE
                      07: FUTURE
                      08: FUTURE
                      09: FUTURE
                      10: FUTURE
                      11: FUTURE
                      12: FUTURE
                      13: FUTURE
                      14: FUTURE
                      15: FUTURE
                      16: FUTURE
                      17: FUTURE
                      18: FUTURE
                      19: FUTURE
                      20: FUTURE
                      21: FUTURE
                      22: FUTURE
                      23: FUTURE
                      24: FUTURE
                      25: FUTURE

                      Z: Logout
                      Please enter your choice: """)

    if choice == "1" or choice =="01":
        data()
    elif choice == "2" or choice =="02":
        voip()
    elif choice == "3" or choice =="03":
        iot()
    elif choice == "4" or choice =="04":
        future()
    elif choice == "5" or choice =="05":
        future()
    elif choice == "6" or choice =="06":
        future()
    elif choice == "7" or choice =="07":
        future()
    elif choice == "8" or choice =="08":
        future()
    elif choice == "9" or choice =="09":
        future()
    elif choice == "10" or choice =="10":
        future()
    elif choice == "11" or choice =="11":
        future()
    elif choice == "12" or choice =="12":
        future()
    elif choice == "13" or choice =="13":
        future()
    elif choice == "14" or choice =="14":
        future()
    elif choice == "15" or choice =="15":
        future()
    elif choice == "16" or choice =="16":
        future()
    elif choice == "17" or choice =="17":
        future()
    elif choice == "18" or choice =="18":
        future()
    elif choice == "19" or choice =="19":
        future()
    elif choice == "20" or choice =="20":
        future()
    elif choice == "21" or choice =="21":
        future()
    elif choice == "22" or choice =="22":
        future()
    elif choice == "23" or choice =="23":
        future()
    elif choice == "24" or choice =="24":
        future()
    elif choice == "25" or choice =="25":
        future()



    elif choice=="Z" or choice=="z":
        sys.exit
    else:

        print("You must only select either A or B")
        print("Please try again")
        menu()

def data():
   base_acl = open("/automater/acl_gen/data.conf", "r")
   acl = "DATA-IN"
   print("ip access-list extended" + "", acl)
   for i in base_acl:
      values = i.split()
      index = values.index('[]')
      values[index] = src_ip
      while '[]' in values:
          index = values.index('[]')
          values.pop(index)
      print(' '.join(values))
   base_acl.close()
   pass


def voip():
   base_acl = open("/automater/acl_gen/voip.conf", "r")
   acl = "VOIP-IN"
   print("ip access-list extended" + "", acl)
   for i in base_acl:
      values = i.split()
      index = values.index('[]')
      values[index] = src_ip
      while '[]' in values:
          index = values.index('[]')
          values.pop(index)
      print(' '.join(values))
   base_acl.close()

   pass

def iot():
   base_acl = open("/automater/acl_gen/iot.conf", "r")
   acl = "IOT-IN"
   print("ip access-list extended" + "", acl)
   for i in base_acl:
      values = i.split()
      index = values.index('[]')
      values[index] = src_ip
      while '[]' in values:
          index = values.index('[]')
          values.pop(index)
      print(' '.join(values))
   base_acl.close()

   pass

def future():
   pass

def future():
   pass

def future():
   pass

def future():
   pass

def future():
   pass

def future():
   pass

def future():
   pass

def future():
   pass

def future():
   pass

def future():
   pass

def future():
   pass

def future():
   pass

def future():
   pass

def future():
   pass

def future():
   pass

def future():
   pass

def future():
   pass

def future():
   pass

def future():
   pass

def future():
   pass

def future():
   pass

def future():
   pass


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


##the program is initiated, so to speak, here
main()
