#code will be improved as time goes on. 
#NOTE: THIS IS A PROTOTYPEM IT DOESNT WORK FOR ANYTHING AND IT A PROOF OF CONCEPT

import time

def leg_count():    #Connect 2 or 4 legs and input the number of legs you have connected
    legs = int(input("How many legs have you connected: "))
    if legs == 4:
        main_4()
    elif legs == 6:
        main_6()
    else:
        print("please connect 4 or 6 legs")
        leg_count()

def main_4():   #Calabrates the legs to make sure theyre connected for 4 legs
    print("checking leg connections...")
    time.sleep(2)
    move_4_()

def main_6():   #Calabrates the legs to make sure theyre connected for 6 legs
    print("checking leg connections...")
    time.sleep(2)
    print("Valid Leg connections")
    move_6_()

def move_6_():  #Intro Movement script for 6 legs
    movement_direction_6 = input("Which direction would you like to go: W = forward, A = turn left, S = backwards, D = turn right: ")
    time.sleep(2)
    if movement_direction_6 == "W":
        print("Moved forwards")
    elif movement_direction_6 == "S":
        print("Moved backwards")
    elif movement_direction_6 == "A":
        print("Turned left")
    elif movement_direction_6 == "D":
        print("Turned Right")
    else:
        print("Invalid input, Try again")
    move_6()

def move_6():   #Main movement script for 6 legs
    movement_direction_6 = input("Direction: ")
    time.sleep(2)
    if movement_direction_6 == "W":
        print("Moved forwards")
    elif movement_direction_6 == "S":
        print("Moved backwards")
    elif movement_direction_6 == "A":
        print("Turned left")
    elif movement_direction_6 == "D":
        print("Turned Right")
    elif movement_direction_6 == "STOP":
        quit()
    elif movement_direction_6 == "RECALABRATE":
        leg_count()
    else:
        print("Invalid input, Try again")
    move_6()

def move_4_():  #into movement script for 4 legs
    movement_direction_4 = input("Which direction would you like to go: W = forward, A = turn left, S = backwards, D = turn right: ")
    time.sleep(2)
    if movement_direction_4 == "W":
        print("Moved forwards")
    elif movement_direction_4 == "S":
        print("Moved backwards")
    elif movement_direction_4 == "A":
        print("Turned left")
    elif movement_direction_4 == "D":
        print("Turned Right")
    else:
        print("Invalid input, Try again")
    move_4()

def move_4():   #Main movement script for 4 legs
    movement_direction_4 = input("Direction: ")
    time.sleep(2)
    if movement_direction_4 == "W":
        print("Moved forwards")
    elif movement_direction_4 == "S":
        print("Moved backwards")
    elif movement_direction_4 == "A":
        print("Turned left")
    elif movement_direction_4 == "D":
        print("Turned Right")
    elif movement_direction_4 == "STOP":
        quit()
    elif movement_direction_4 == "RECALABRATE":
        leg_count()
    else:
        print("Invalid input, Try again")
    move_4()

leg_count()
