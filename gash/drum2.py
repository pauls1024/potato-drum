#!/usr/bin/env python

"""beetbox_serial.py: Trigger script for the control panel- 3 serial reports to arduino to control LED sequences, 3 Joe voice samples, 6 drum samples. Plan to introduce Cron to stop sounds after bedtime"""

__author__ = "Shane Lester -based on code by Scott Garner"


import pygame

import RPi.GPIO as GPIO
import mpr121
import serial

from pythonosc import osc_message_builder
from pythonosc import udp_client

sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)

# Use GPIO Interrupt Pin
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)

# Use mpr121 class for everything else
mpr121.TOU_THRESH = 0x30
mpr121.REL_THRESH = 0x33
mpr121.setup(0x5a)

touches = [0,0,0,0,0,0,0,0,0,0,0,0];

while True:

   if (GPIO.input(7)): # Interupt pin is high
     pass
   else: # Interupt pin is low
      print( "LOW")
      touchData = mpr121.readData(0x5a)
      
      print( touchData)           

      for i in range(12):
         if (touchData & (1<<i)):

            if (touches[i] == 0):

               print( 'Pin ' + str(i) + ' was just touched')
               sender.send_message('/play_drum', str(i))

            touches[i] = 1;
         else:
            if (touches[i] == 1):
               print( 'Pin ' + str(i) + ' was just released')
            touches[i] = 0;

