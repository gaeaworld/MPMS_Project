#!/usr/bin/python


#//-----------------------------
#//          lib
#//-----------------------------
#import RPi.GPIO as GPIO
import time


#//-----------------------------
#//          Debug
#//-----------------------------
TURN_ON = 1
TURN_OFF = 0
DEBUG = TURN_ON

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
prev_input    = 0
c_people_coin = 0
people_coin   = 0
current_time  = 0
pir_input     = 0
nrm_file      = "node_record_min.txt"
nrs_file      = "node_record_sum.txt"

if(DEBUG == TURN_ON):
    #//1. init GPIO
    #GPIO.setmode(GPIO.BOARD)
    RIP_Pin = GPIO14
    print "Setup Detect RIP PIN"
    #GPIO.setup(RIP_Pin, GPIO.IN)

    #//2. while loop to detect RIP pin
    while True:
        pir_input = 1
        if (1):
            #//2.1 show current time
            current_time = time.strftime("%Y/%b/%d %H:%M:%S")
            print current_time
            #//2.2 count plus 1
            print("RIP high")
            people_coin += 1
            print people_coin
            #//2.3 write into nrm file
            #//TO DO...

        #prev_input = pir_input           #update previous input
        time.sleep(0.5)
        #// 2.4 write into nrs file
        msg = str(people_coin)
        fd = open(nrs_file, 'w')
        fd.write(msg)
        fd.close()
else:
   #//1. init GPIO
    GPIO.setmode(GPIO.BOARD)
    RIP_Pin = GPIO14
    print "Setup Detect RIP PIN"
    GPIO.setup(RIP_Pin, GPIO.IN)

    #//2. while loop to detect RIP pin
    while True:
        pir_input = GPIO.input(RIP_Pin)
        if ((not prev_input) and pir_input):
            #//2.1 show current time
            current_time = time.strftime("%Y/%b/%d %H:%M:%S")
            print current_time
            #//2.2 count plus 1
            print("RIP high")
            people_coin += 1
            print people_coin
            #//2.3 write into nrm file
            #//TO DO...

        prev_input = pir_input           #update previous input
        time.sleep(0.5)
        #// 2.4 write into nrs file
        msg = str(people_coin)
        fd = open(nrs_file, 'w')
        fd.write(msg)
        fd.close()
