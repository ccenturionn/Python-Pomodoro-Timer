import time

def startTimer(timeLeft):
    while timeLeft:
        mins, secs = divmod(timeLeft, 60)
        timeFormat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeFormat, end='\r')
        time.sleep(1)
        timeLeft -= 1
    print("done\n")

def setBreak():
    print("Break")

def mainMenu():
    print("1. Start a new timer")
    print("2. Set break length")
    userInput = int(input("What option would you like to pick? "))
    if userInput == 1:
        startTimer(120)
    elif userInput == 2:
        setBreak()
    else:
        print("Invalid Option")
        return(mainMenu())

def main():
    mainMenu()
    print("Hello World")

main()
