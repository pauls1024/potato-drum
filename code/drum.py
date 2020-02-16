#!/usr/bin/env python

# This is a python3 script
# bin() function and Sonic Pi OSC will not work from python2

"""beetbox based script : Trigger script for sonic pi using 12 channel mpr121 sensor"""

__author__ = "Paul Smith - based on code by Scott Garner and Shane Lester"

from gpiozero import Button 
import mpr121

from pythonosc import osc_message_builder
from pythonosc import udp_client

sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)

# Use GPIO Interrupt Pin
trigger = Button(14)

# Use mpr121 class for everything else
mpr121.TOU_THRESH = 0x30
mpr121.REL_THRESH = 0x33
mpr121.setup(0x5a)

# create a place to store the last state (touched  or not touched) of each switch
touches = [0,0,0,0,0,0,0,0,0,0,0,0]

while True:
    #check to see if the mpr121 has set the interrupt pin
    if (trigger.is_pressed):
      print( "Something was touched or released")
      #read the data to see which switches are currently pressed
      touchData = mpr121.readData(0x5a)
      
      print( "Current switch state :" + bin(touchData)[2:].zfill(12))           

      #send a message to Sonic Pi for each switch currently touched
      for i in range(12):
         if (touchData & (1<<i)):

            if (touches[i] == 0):

               print( 'Pin ' + str(i) + ' was just touched')
               sender.send_message('/play_drum', str(i))

            touches[i] = 1
         else:
            if (touches[i] == 1):
               print( 'Pin ' + str(i) + ' was just released')
            touches[i] = 0
    else:
        pass
