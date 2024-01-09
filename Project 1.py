import datetime
import pyfiglet
from colorama import *

init()
blue = Fore.BLUE
red = Fore.RED
green = Fore.GREEN
reset = Fore.RESET
bold = Style.BRIGHT
r = Style.RESET_ALL
bold
head = pyfiglet.figlet_format("TODO List")
print(head)
r
time = str(datetime.datetime.now())
print(bold ,blue , time  , reset ,r)


while True:
    works = input(f"{bold}Enter your work: ")
    
    with open('TODO.lst' , 'a') as f:
        f.write(time)
        f.write(" : ")
        f.write(works)
        f.write("\n")
        f.close()
    restart = input("Are you want to continue(Yes or No): ")

    if restart.lower() == "no":

        print(f"{green}[+]Work Stored succesfully, Your work is: ")
        with open('TODO.lst' , 'r') as f:
            print(f.read())
            f.close()
            reset
            break
    # elif restart.lower()=="no": break
    else: continue