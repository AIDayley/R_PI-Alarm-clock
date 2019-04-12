#!/usr/bin/env python3
# get the GPIO time and datetime libraries
import RPi.GPIO as GPIO
import time
import datetime
'''# Most likely NOT needed anymore'''
'''# got this from https://stackoverflow.com/questions/4772830/how-do-you-play-ogg-files-in-python-in-linux
#you need to run the following lines in your shell before this method of playing files will work
# the dependencies
sudo apt-get install libsndfile-dev python-numpy cython python-setuptools
# also get http://github.com/cournape/audiolab
# install audiolab
cd audiolab-0.11 && python setup.py install --user
'''
#
#from scikits.audiolab.pysndfile.matapi import oggread
#import vlc
#from pygame import mixer
#
GPIO.setmode(GPIO.BCM) # Set numbering scheme to the one that is defined at a low level by the internal CPU
# This is due to the fact that there are multiple different boards with different numberings, and this can cause problems when working around DNU pins
# See https://learn.sparkfun.com/tutorials/raspberry-gpio/all#python-rpigpio-api
# Logical GPIO pin 4 is the Alarm Switch
GPIO.setup(4, GPIO.IN) # this is if you want no resistor
#GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Pull up resistor 
#GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Pull down resistor
'''# GPIO pin for light needs to be added'''
GPIO.setup(00, GPIO.OUT) # this is if you want no resistor
#GPIO.setup(00, GPIO.OUT, pull_up_down=GPIO.PUD_UP) #Pull up resistor 
#GPIO.setup(00, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN) #Pull down resistor 
# Logical GPIO pin 17 is the Horn Output Pin
GPIO.setup(18, GPIO.OUT) # this is if you want no resistor
#GPIO.setup(18, GPIO.OUT, pull_up_down=GPIO.PUD_UP) #Pull up resistor 
#GPIO.setup(18, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN) #Pull down resistor 

#
# This code should not be needed since the audio will be played by the script 
#If using pygame mixer
#mixer.init()
#mixer.music.load("alarm.mp3")
# or if using VLC
#p = vlc.MediaPlayer("alarm.mp3")
#


print("setup complete") # This line is used for toubleshooting
# Loop that allows for swapping modes
while (True):
  # "Alarm program"
  while(True):
    # Check I/O pin for alarm switch state
    print("first loop") # This line is used for toubleshooting
    if (GPIO.input(4)):
      print("alarm enabled") # This line is used for toubleshooting
      currentDT = datetime.datetime.now()
      if (currentDT.hour>=5 and currentDT.minute>=45):
        break; # leave the loop and go to the other loop if it is (or is past) 5:50
    else:
      GPIO.output(00, GPIO.LOW) '''# GPIO needs to be added for the light'''
      GPIO.output(18, GPIO.LOW) # quiet the horn
      time.sleep(5) # in seconds
  while(True):
    time.sleep(0.5) # This may need to be changed
    if(GPIO.input(4)):
      print("loop 2 io on") # This line is used for toubleshooting
      currentDT = datetime.datetime.now()
      print(currentDT) # This line is used for toubleshooting
      if(currentDT.hour>=19 and currentDT.minute>=0):
        '''# Insert your code here to call up the script to play audio'''
        #mixer.music.play()
        #p.play()
		#data, fs, enc = oggread("alarm.ogg")
        time.sleep(301)
        print("music after hit") # This line is used for toubleshooting
        if(currentDT.hour>=6 and currentDT.minute>=5): #Horn
          print("horn loop before hit") # This line is used for toubleshooting
          GPIO.output(18, GPIO.HIGH) # this does not turn off. For this reason, I've added code that will fix that.
          print("horn pin on") # This line is used for toubleshooting
    else:break # go back to the upper loop if the switch is off
GPIO.cleanup() # return pins to default value (might not even be executed, but if something breaks the outermost while loop, then it would be)
