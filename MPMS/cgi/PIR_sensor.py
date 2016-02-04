#!/usr/bin/python


#//-----------------------------
#//          lib
#//-----------------------------
import RPi.GPIO as GPIO
import time

#//-----------------------------
#//          Debug
#//-----------------------------


#//-----------------------------
#//          Variable
#//-----------------------------
GPIO14 = 8


#//-----------------------------
#//          function
#//-----------------------------


#//------------------------------
#//          main
#//------------------------------
#variable
prev_input = 0
people_coin = 0

#//1. init GPIO
# Use physical pin numbers
GPIO.setmode(GPIO.BOARD)
# Set up header pin 22 (GPIO25) as an input
RIP_Pin = GPIO14
print "Setup Detect RIP PIN"
GPIO.setup(RIP_Pin, GPIO.IN)

#//2. while, keep loop to detect RIP pin
while True:
  #take a reading
  input = GPIO.input(RIP_Pin)
  #if the last reading was low and this one high, print
  if ((not prev_input) and input):
    print("RIP high")
    people_coin += 1
  #update previous input
  prev_input = input
  #slight pause to debounce
  time.sleep(0.05)