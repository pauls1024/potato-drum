#!/usr/bin/env python

"""beetbox_serial.py: Trigger script for the control panel- 3 serial reports to arduino to control LED sequences, 3 Joe voice samples, 6 drum samples. Plan to introduce Cron to stop sounds after bedtime"""

__author__ = "Shane Lester -based on code by Scott Garner"


import pygame

import RPi.GPIO as GPIO
import mpr121
import serial
#ser = serial.Serial('/dev/ttyUSB0',9600)

# Use GPIO Interrupt Pin

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)

# Use mpr121 class for everything else

mpr121.TOU_THRESH = 0x30
mpr121.REL_THRESH = 0x33
mpr121.setup(0x5a)

# User pygame for sounds

pygame.mixer.pre_init(44100, -16, 12, 512)
pygame.init()

kick = pygame.mixer.Sound('samples/kick.wav')
kick.set_volume(.65);
snare = pygame.mixer.Sound('samples/snare.wav')
snare.set_volume(.65);
openhh = pygame.mixer.Sound('samples/open.wav')
openhh.set_volume(.65);
closedhh = pygame.mixer.Sound('samples/closed.wav')
closedhh.set_volume(.65);
clap = pygame.mixer.Sound('samples/clap.wav')
clap.set_volume(.65);
cymbal = pygame.mixer.Sound('samples/cymbal.wav')
cymbal.set_volume(.65);
BongoHigh = pygame.mixer.Sound('samples/BongoHigh.wav')
BongoHigh.set_volume(.65);
ed1 = pygame.mixer.Sound('samples/ed1.wav')
ed1.set_volume(.65);
ed2 = pygame.mixer.Sound('samples/ed2.wav')
ed2.set_volume(.65);
ed3 = pygame.mixer.Sound('samples/ed3.wav')
ed3.set_volume(.65);
ed4 = pygame.mixer.Sound('samples/ed4.wav')
ed4.set_volume(.65);
ed1 = pygame.mixer.Sound('samples/ed1.wav')
ed1.set_volume(.65);
joe1 = pygame.mixer.Sound('samples/joe1.wav')
joe1.set_volume(.65);
joe2 = pygame.mixer.Sound('samples/joe2.wav')
joe2.set_volume(.65);
joe3 = pygame.mixer.Sound('samples/joe3.wav')
joe3.set_volume(.65);
# Track touches

touches = [0,0,0,0,0,0,0,0,0,0,0,0];


while True:

   if (GPIO.input(7)): # Interupt pin is high
     pass
   else: # Interupt pin is low
      print "LOW"
      touchData = mpr121.readData(0x5a)
      
      print touchData           

      for i in range(12):
         if (touchData & (1<<i)):

            if (touches[i] == 0):

               print( 'Pin ' + str(i) + ' was just touched')

               if (i == 0):
                  #ser.write('0')
                  print 1
               elif (i == 1):
                  #ser.write('1')
                  print 2
               elif (i == 2):                  
                  #ser.write('2')
                  print 3
               elif (i == 3):
                  closedhh.play()
               elif (i == 4):
                  openhh.play()
               elif (i == 5):
                  cymbal.play()
               elif (i == 6):
                  clap.play()
               elif (i == 7):
                  snare.play()
               elif (i == 8):
                  kick.play()
               elif (i == 9):
                  joe1.play()
               elif (i == 10):
                  joe2.play()
               elif (i == 11):
                  joe3.play()

            touches[i] = 1;
         else:
            if (touches[i] == 1):
               print( 'Pin ' + str(i) + ' was just released')
            touches[i] = 0;

