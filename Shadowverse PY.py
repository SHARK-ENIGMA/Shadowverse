import time # Used for telling the program to wait a few seconds.
import os # Used for the 'cls' command.

# This class describes the class "bcolors", in relation to coloring text.
# Usage example:    print(bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)
class bcolors:
    # violet
    HEADER = '\033[95m'
    # light-blue
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    # light-yellow
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
# End color definitions

# This is the script that defines what "cls" means. We must call upon a base Windows command called "cls" to use this defined command.
# The blue "cls" is our custom name for the command in this program.
def cls():
    os.system('cls')

cls()
# End CLS defining

# This is where we figure out how to find "quit" within a specific input. (DAY 3)
def DEBUG_MENU_input():
    MENU_input = [str(input(MENU_prompts[1]))]
    time.sleep(1)
    print(MENU_input)
    time.sleep(1)
    if ("1" in MENU_input):
        print(bcolors.OKBLUE + "1 has been typed." + bcolors.ENDC)
        DEBUG_MENU_input()
    elif ("2" in MENU_input):
        print(bcolors.OKBLUE + "2 has been typed." + bcolors.ENDC)
        DEBUG_MENU_input()
    elif ("3" in MENU_input):
        print(bcolors.OKBLUE + "3 has been typed." + bcolors.ENDC)
        DEBUG_MENU_input()
    elif ("4" in MENU_input):
        print(bcolors.OKBLUE + "4 has been typed.")
        DEBUG_MENU_input()
    # FOUND IT! --->
    elif ("Quit" in MENU_input or "quit" in MENU_input):
        print(bcolors.OKBLUE + "Quit has been typed." + bcolors.ENDC)
        DEBUG_MENU_input()
    else:
        print(ERR_codes[0])
        DEBUG_MENU_input()

def COUNTDOWN_3():
    COUNTER_3 = 0
    while True:
        COUNTER_3 += 1
        time.sleep(1)
        print(bcolors.OKCYAN + str(COUNTER_3) + bcolors.ENDC)
        if (COUNTER_3 == 3):
            break

def COUNTDOWN_5():
    COUNTER_5 = 0
    while True:
        COUNTER_5 += 1
        print(bcolors.OKCYAN + str(COUNTER_5) + bcolors.ENDC)
        time.sleep(1)
        if (COUNTER_5 == 5):
            break
    
# This is where we must begin defining the different variables later used for user input.
MENU_prompts = [
    bcolors.OKCYAN + "> " + bcolors.ENDC, # 0
    bcolors.OKBLUE + "Please input your response: " + bcolors.ENDC, # 1
    bcolors.FAIL + "Closing executable" + bcolors.ENDC, # 2
    bcolors.FAIL + "Are you sure?" + bcolors.ENDC, # 3
]
ERR_codes = [
    bcolors.FAIL + "ERR_INPUT: Please make sure there are no typos in your response." + bcolors.ENDC, # 0
    bcolors.FAIL + "ERR_SEQUENCE: Please make sure your command is structured correctly" + bcolors.ENDC, # 
]
SYS_QUIT = 0

# This is the pre-load screen that displays what the game is, who it was made by, and what version it's currently running at.
def PRE_LOAD_SCREEN():
    print(bcolors.UNDERLINE + bcolors.FAIL + "WE ARE OFFICIALLY OUT OF PRE-ALPHA AND IN ALPHA STAGE!" + bcolors.ENDC + bcolors.ENDC)
    time.sleep(0.2)
    print(bcolors.HEADER + "Author:" + bcolors.ENDC + bcolors.WARNING + " Kyle Scott" + bcolors.ENDC)
    time.sleep(2)
    print(bcolors.HEADER + "Version: " + bcolors.ENDC + bcolors.WARNING + "0.22" + bcolors.ENDC)
    time.sleep(0.2)
    print(bcolors.HEADER + "Project Began: " + bcolors.ENDC + bcolors.WARNING + "9-14-2024" + bcolors.ENDC)
    time.sleep(0.2)
    print(bcolors.HEADER + "Description:" + bcolors.ENDC)
    time.sleep(0.2)
    print(bcolors.HEADER + " - " + bcolors.ENDC + bcolors.WARNING + "This is a text-based RPG called Shadowverse." + bcolors.ENDC)
    time.sleep(0.2)
    print(bcolors.HEADER + " - " + bcolors.ENDC + bcolors.WARNING + "You make decisions based on intelligently generated rooms and areas that you enter upon your own volition." + bcolors.ENDC)
    time.sleep(0.2)
    print(bcolors.HEADER + " - " + bcolors.ENDC + bcolors.WARNING + "The intent is to have an options system, inventory system, save system, and a randomly generated rooms system" + bcolors.ENDC)
    time.sleep(0.2)
    print(bcolors.WARNING + "   based on sets of text in different arrays." + bcolors.ENDC)
    time.sleep(2)
    print(" ")
    print(" ")
    # Default update entry:
    # print(bcolors.HEADER + " - " + bcolors.ENDC + bcolors.WARNING + "" + bcolors.ENDC)
    print(bcolors.HEADER + "Recent Updates:" + bcolors.ENDC)
    time.sleep(0.2)
    print(bcolors.HEADER + " - " + bcolors.ENDC + bcolors.WARNING + "" + bcolors.ENDC)
    time.sleep(0.2)
    print(bcolors.HEADER + " - " + bcolors.ENDC + bcolors.WARNING + "Made a lot of updates for the 'MAIN_INPUT' loop." + bcolors.ENDC)
    time.sleep(0.2)
    print(bcolors.HEADER + " - " + bcolors.ENDC + bcolors.WARNING + "Wrote the 'OPTIONS' Screen." + bcolors.ENDC)
    time.sleep(0.2)
    print(bcolors.HEADER + " - " + bcolors.ENDC + bcolors.WARNING + "Made some functions for a quick countdown counter... 'COUNTDOWN_3' & 'COUNTDOWN_5'" + bcolors.ENDC)
    time.sleep(0.2)
    print(bcolors.HEADER + " - " + bcolors.ENDC + bcolors.WARNING + "Didn't get any kind of keypress functionality to work..." + bcolors.ENDC)
    time.sleep(0.2)
    print(bcolors.HEADER + " - " + bcolors.ENDC + bcolors.WARNING + "Made an update dev-log." + bcolors.ENDC)
    time.sleep(0.2)
    print(bcolors.HEADER + " - " + bcolors.ENDC + bcolors.WARNING + "Rewrote the menu screens into their own functions to be called later." + bcolors.ENDC)
    time.sleep(0.2)
    print(bcolors.HEADER + " - " + bcolors.ENDC + bcolors.WARNING + "FIXED the MENU_input input string response checker." + bcolors.ENDC)
    time.sleep(0.2)
    print(bcolors.HEADER + " - " + bcolors.ENDC + bcolors.WARNING + "Made the Pre-load screen." + bcolors.ENDC)
    time.sleep(0.2)
    print(bcolors.HEADER + " - " + bcolors.ENDC + bcolors.WARNING + "Made the Main-Menu." + bcolors.ENDC)
    print(" ")
    input("Input any key to continue... ")
    cls()
# End pre-load screen


# Right here is where the 'load-screen' will be displayed, loading and creating different files as needed.


# Begin MENU_OPTIONS() screen
def MENU_OPTIONS():
    print(bcolors.HEADER + " ██████  ██████  ████████ ██  ██████  ███    ██ ███████ " + bcolors.ENDC)
    print(bcolors.HEADER + "██    ██ ██   ██    ██    ██ ██    ██ ████   ██ ██      " + bcolors.ENDC)
    print(bcolors.HEADER + "██    ██ ██████     ██    ██ ██    ██ ██ ██  ██ ███████ " + bcolors.ENDC)
    print(bcolors.HEADER + "██    ██ ██         ██    ██ ██    ██ ██  ██ ██      ██ " + bcolors.ENDC)
    print(bcolors.HEADER + " ██████  ██         ██    ██  ██████  ██   ████ ███████ " + bcolors.ENDC)
    print(bcolors.HEADER + "                                                        " + bcolors.ENDC)
    print(bcolors.HEADER + "[Back]" + bcolors.ENDC)
    print(bcolors.HEADER + "[Help]" + bcolors.ENDC)
    print(bcolors.HEADER + "[DEBUG]" + bcolors.ENDC)
    print(bcolors.HEADER + "[3]" + bcolors.ENDC + bcolors.WARNING + "      Rename Save" + bcolors.ENDC)
    # https://stackoverflow.com/questions/2491222/how-to-rename-a-file-using-python
    print(bcolors.HEADER + "[4]" + bcolors.ENDC + bcolors.WARNING + "      Delete Save" + bcolors.ENDC)
    print(bcolors.HEADER + "[5]" + bcolors.ENDC + bcolors.WARNING + "      Author's Notes" + bcolors.ENDC)
    print(bcolors.HEADER + "[6]" + bcolors.ENDC + bcolors.WARNING + "      Check Stats" + bcolors.ENDC)
    print(bcolors.HEADER + "[...]" + bcolors.ENDC + bcolors.WARNING + "      " + bcolors.ENDC)
# End MENU_OPTIONS() screen


# This is the main menu. This pretty screen displays in different secitons of the text different colors. This is how we make it look nice.
def MAIN_MENU_SCREEN():
    print(bcolors.HEADER + "███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗██╗   ██╗███████╗██████╗ ███████╗███████╗" + bcolors.ENDC)
    print(bcolors.HEADER + "██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║██║   ██║██╔════╝██╔══██╗██╔════╝██╔════╝" + bcolors.ENDC)
    print(bcolors.OKBLUE + "███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║██║   ██║█████╗  ██████╔╝███████╗█████╗  " + bcolors.ENDC)
    print(bcolors.OKBLUE + "╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════██║██╔══╝  " + bcolors.ENDC)
    print("███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝ ╚████╔╝ ███████╗██║  ██║███████║███████╗")
    print("╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝")
    print("                              " + bcolors.HEADER + "Kyle Scott" + bcolors.ENDC + "                                                    ")
    print(bcolors.WARNING + "[1]" + bcolors.ENDC + "     Play")
    print(bcolors.WARNING + "[2]" + bcolors.ENDC + "     Options")
    print(bcolors.WARNING + "[3]" + bcolors.ENDC + "     New Game")
    print(bcolors.WARNING + "[4]" + bcolors.ENDC + "     Load Game")
    print(bcolors.WARNING + "[5]" + bcolors.ENDC + "     Tutorial")
    print(bcolors.WARNING + "[Quit]" + bcolors.ENDC)
# End main menu screen, and begin requiring input from the user.

# How to create, edit, and read txt files
# https://www.askpython.com/python/built-in-methods/modify-text-file-python
# https://www.geeksforgeeks.org/create-a-new-text-file-in-python/

PRE_LOAD_SCREEN()
time.sleep(1)
while SYS_QUIT == 0:
    # We begin writing our program here.
    MAIN_MENU_SCREEN()
    print(" ")
    MENU_input = input(MENU_prompts[0])
    if ("1" in MENU_input):
        # This is just placeholder code for when we actually start making the game.
        cls()
        print(bcolors.OKBLUE + "Play Game" + bcolors.ENDC)
        time.sleep(3)
    elif ("2" in MENU_input):
        cls()
        MENU_OPTIONS()
        MENU_input = input(MENU_prompts[0])
        if ("Back" in MENU_input or "BACK" in MENU_input or "back" in MENU_input):
            cls()
            continue
        elif ("Help" in MENU_input or "HELP" in MENU_input or "help" in MENU_input):
            cls()
            # Help menu here
            print("help")
        elif ("DEBUG" in MENU_input or "debug" in MENU_input or "Debug" in MENU_input):
            cls()
            # Debug menu here
            print("Debug")
        elif ("3" in MENU_input):
            cls()
            # Rename Save menu here
            print("Rename Save")
        elif ("4" in MENU_input):
            cls()
            # Delete Save menu here
            print("Delete Save")
        elif ("5" in MENU_input):
            cls()
            # Author's Notes here
            print("Author's Notes")
        elif ("6" in MENU_input):
            cls()
            # Check Stats menu here
            print("Check Stats")
        else:
            print(ERR_codes[0])
    elif ("3" in MENU_input):
        print(bcolors.OKBLUE + "3 has been typed." + bcolors.ENDC)
    elif ("4" in MENU_input):
        print(bcolors.OKBLUE + "4 has been typed.")
    elif ("Quit" in MENU_input or "quit" in MENU_input):
        # 'Are you sure?' screen
        print(MENU_prompts[3])
        input("Input any key to continue... ")
    else:
        print(ERR_codes[0])

cls()

print(MENU_prompts[2]) # Closing...
COUNTDOWN_3()
quit()
