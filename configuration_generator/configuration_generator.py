from colorama import init
from termcolor import colored
import csv
import sys
import pyfiglet

def main():
   menu()

def menu():
    clear_screen()
    title = pyfiglet.figlet_format("Configuration Generator", font = "digital", justify="center")
    print(title)

    choice = input("""
                      A: FUTURE        (        )
                      B: FUTURE        (        )
                      C: FUTURE        (        )
                      D: FUTURE        (        )
                      E: FUTURE        (        )
                      F: FUTURE        (        )
                      G: FUTURE        (        )
                      H: FUTURE        (        )
                      I: FUTURE        (        )
                      J: FUTURE        (        )
                      K: FUTURE        (        )
                      L: FUTURE        (        )
                      M: FUTURE        (        )
                      N: FUTURE        (        )
                      O: FUTURE        (        )
                      P: FUTURE        (        )
                      Q: FUTURE        (        )
                      R: FUTURE        (        )
                      S: FUTURE        (        )
                      T: FUTURE        (        )
                      U: FUTURE        (        )
                      v: FUTURE        (        )
                      W: FUTURE        (        )


                      Z: Logout
                      Please enter your choice: """)

    if choice == "A" or choice =="a":
        future()
    elif choice == "B" or choice =="b":
        future()
    elif choice == "C" or choice =="c":
        future()
    elif choice == "D" or choice =="d":
        future()
    elif choice == "E" or choice =="e":
        future()
    elif choice == "F" or choice =="f":
        future()
    elif choice == "G" or choice =="g":
        future()
    elif choice == "H" or choice =="h":
        future()
    elif choice == "I" or choice =="i":
        future()
    elif choice == "J" or choice =="j":
        future()
    elif choice == "K" or choice =="k":
        future()
    elif choice == "L" or choice =="l":
        future()
    elif choice == "M" or choice =="m":
        future()
    elif choice == "N" or choice =="n":
        future()
    elif choice == "O" or choice =="o":
        future()
    elif choice == "P" or choice =="p":
        future()
    elif choice == "Q" or choice =="q":
        future()
    elif choice == "R" or choice =="r":
        future()
    elif choice == "S" or choice =="s":
        future()
    elif choice == "T" or choice =="t":
        future()
    elif choice == "U" or choice =="u":
        future()
    elif choice == "V" or choice =="v":
        future()
    elif choice == "W" or choice =="w":
        future()
    elif choice=="Z" or choice=="z":
        sys.exit
    else:
        print("You must only select either A or B")
        print("Please try again")
        menu()


def future():
    file_path = 'future.txt'
    try:
        with open(file_path, 'r') as file:
            # Read the content of the file
            file_content = file.read()

            # Print the content
            print(file_content)

    except FileNotFoundError:
        pass
    except Exception as e:
        pass


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
