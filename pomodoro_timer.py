import time
import os

#Runs the timer and outputs it to the terminal
def startTimer(timeLeft, breakLength):
    os.system('clear')
    print("Starting a timer with a working time of {0} mins and a break time of {1} mins".format(timeLeft / 60, breakLength / 60))
    timeLeftBack = timeLeft
    breakLengthBack = breakLength
    while True:
        timeLeft = timeLeftBack
        breakLength = breakLengthBack
        #Loop for work section of timer
        while timeLeft:
            mins, secs = divmod(timeLeft, 60)
            timeFormat = '{:02d}:{:02d}'.format(mins, secs)
            print("        WORKING                                                        ", end='\r')
            print(timeFormat, end='\r')
            time.sleep(1)
            timeLeft -= 1
        #Loop for break section of timer
        while breakLength:
            mins, secs = divmod(breakLength, 60)
            timeFormat = '{:02d}:{:02d}'.format(mins, secs)
            print("        BREAK                                                        ", end='\r')
            print(timeFormat, end='\r')
            time.sleep(1)
            breakLength -= 1

def setTime():
    os.system('clear')
    try:
        timeLength = 60 * int(input("How long would you like the timer to be? (mins): "))
    except ValueError:
        print("Invalid Input")
        return(setTime())
    return(timeLength)
    print("Length of timer set to", timeLength)

#Allows user to define the length of the break period
def setBreak():
    os.system('clear')
    try:
        breakLength = 60 * int(input("How long would you like your breaks to be? (mins): "))
    except ValueError:
        print("Invalid Input")
        return(setBreak())
    return(breakLength)
    print("Length of break set to", breakLength)

#Main menu presents the options to the user
def mainMenu():
    defaultTime = True
    defaultBreak = True
    while 1:
        os.system('clear')
        print("1. Start the timer")
        print("2. Set work length")
        print("3. Set break length")
        #Checks to ensure user input if valid
        try:
            userInput = int(input("What option would you like to pick? "))
        except ValueError:
            print("Invalid Input")
            return(mainMenu())
        if userInput == 1:
            if defaultTime == True:
                timeLength = 1500
            if defaultBreak == True:
                breakLength = 300
            startTimer(timeLength, breakLength)
        elif userInput == 2:
            timeLength = setTime()
            defaultTime = False
        elif userInput == 3:
            breakLength = setBreak()
            defaultBreak = False
        else:
            print("Invalid Option")
            return(mainMenu())


mainMenu()
