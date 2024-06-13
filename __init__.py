# #!/usr/bin/env python3

import RPi.GPIO as GPIO
import schedule
import time
from datetime import datetime
from subprocess import call
import requests

#Personal Imports
import DownloadOwl
import image
import GetStoredImage
import GetTextRecord

#Directorys
workingDirectory = "/home/cam/ink"
externalConfig = "settings.txt"
backupConfig = "config.txt"
downloadedImage = "downloadedImage.jpg"


#User Settings
customSubreddit = "aww"
usbImageInterval = 120


# Gpio pins for each button (from top to bottom)
#24 is hard coded to shut down
BUTTONS = [5, 6, 16]
LABELS = ['A', 'B', 'C', 'D']
MODES = ["OWL","CUSTOM","USB", "SHUTDOWN", "WEBPAGE"]
currentMode = MODES[0]

shutdownHoldTime = 5
pressedTime = 0
isPressed = False

#Setup the GPIO Buttons
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTONS, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# "handle_button" will be called every time a button is pressed
# It receives one argument: the associated input pin.
def handle_button(pin):
    currentMode = MODES[BUTTONS.index(pin)]
    DisplayFuncs[BUTTONS.index(pin)]()

# Loop through out buttons and attach the "handle_button" function to each
for pin in BUTTONS:
    GPIO.add_event_detect(pin, GPIO.FALLING, handle_button, bouncetime=250)

#Pin 1
def DisplayOwl():
    print("Displaying Owl from Reddit")
    DownloadOwl.DownloadLatestImage("Superbowl")
    image.ShowImage(''.join(["Superbowl", ".jpg"]))

#Pin 2
def DisplayCustom():
    print("Displaying Custom subreddit image")
    DownloadOwl.DownloadLatestImage(customSubreddit)
    image.ShowImage(''.join([customSubreddit, ".jpg"]))

#Pin 3
def DisplayUSB():
    print("Displaying random image from USB")
    img = GetStoredImage.GetRandomImage()
    print("Displaying " + img)
    image.ShowImage(img)

#Pin 4
def PowerDown():
    call("sudo shutdown -h now", shell=True)

def DisplayWeb(link):
    print("Displaying web page from Cam: ", link)
    
    #Download Image
    response = requests.get(link)
    if response.status_code == 200:
        with open(downloadedImage, 'wb') as f:
            f.write(response.content)

    #Show Image
    #image.ShowImage(downloadedImage)

    #Make sure it only runs once
    return schedule.CancelJob

DisplayFuncs = [DisplayOwl,DisplayCustom,DisplayUSB,PowerDown,DisplayWeb]
#DisplayFuncs[4]()

def CheckUSBConnection():
    print("Checking For USB")

def CheckWebCommand():
    #Get executable web commands
    currentWebCommands = GetTextRecord.GetOnlineCommands()

    #Print to logs
    print(datetime.today().time())

    #Add executables to schedule
    for command in currentWebCommands:
        print(command[0].time())
        schedule.every().day.at(str(command[0].time())).do(DisplayWeb, command[1]).tag(command[0])


#Background Processes:
#schedule.every(30).seconds.do(CheckUSBConnection)
#schedule.every(10).minutes.do(CheckWebCommand)

#CheckWebCommand()
#DisplayWeb("https://i.redd.it/dwk2baaqod791.jpg")

while True:
    #Main Loop
    schedule.run_pending()
    time.sleep(1)

    #Check for power Button
    if GPIO.input(24) == GPIO.LOW:
        #First Button press
        if isPressed == False:
            isPressed = True
            pressedTime = time.time()
            #Unmount USB
            call("sudo umount /home/cam/usb", shell=True)

        #Check timer
        elif isPressed and time.time() - pressedTime > shutdownHoldTime:
            print("Shutting Down Pi")
            PowerDown()
            break

    #reset timer check
    elif isPressed:
        isPressed = False


#todo list:
#Check online for text record, and show message/image if date matches.
    #Can't be a browser, will be a manual link to an existing image.


#Figure out how to go back to showing the web page after closing.
#USB text file options
    #Show new usb image every 30 mins, check reddit every 3 hours, etc.
#Auto run and restart