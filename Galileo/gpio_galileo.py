# This code writes and reads from the GPIO pins available on the BeagleBone Blue
# BeagleBone Blue Pinout https://github.com/beagleboard/beaglebone-blue/wiki/Pinouts
# Uses Adafruit library
# Created by NexTec Capstone Team at Texas A&M, Fall 2019

# Import external librarires
import Adafruit_BBIO
from Adafruit_BBIO.GPIO import *
import time

#DEFINE I/O NAMES FROM BBIO LIBRARY (referenced from pinout diagram above)
#-------------------------------------------------------------------------
#LEDs
USR_LED0 = "USR0"
USR_LED1 = "USR1"
USR_LED2 = "USR2"
USR_LED3 = "USR3"
LED_RED = "RED_LED"
LED_GREEN = "GREEN_LED"
#OUTPUTS
GPIO1_25 = "GP0_3"
GPIO1_17 = "GP0_4"
GPIO3_20 = "GP0_5"
GPIO3_17 = "GP0_6"
GPIO3_2 = "GP1_3"
GPIO3_1 = "GP1_4"
#INPUTS
GPIO1_17 = "GP0_4"
GPIO3_17 = "GP0_6"

#MODES
OUTPUT = 1
INPUT = 0

#STATES
HIGH = 1
LOW = 0

# DEFINE RELEVANT FUNCTIONS
def init(Pin, Mode): # Initialize GPIO pin as either Output or Input
    setup(Pin, Mode)
def write(Pin, State): # Write to Output GPIO pin as either High or Low
    output(Pin, State)
def read(Pin): # Read State (High or Low) of Input GPIO pin 
    State = input(Pin)
    return(State)
def vac_on():
    init(GPIO1_25, OUTPUT)
    write(GPIO1_25, HIGH)
def vac_off():
    init(GPIO1_25, OUTPUT)
    write(GPIO1_25, LOW)
# # UNCOMMENT THE SECTION BELOW TO RUN AS STANDALONE CODE

# while 1:
#     write(GPIO1_25, HIGH)
#     time.sleep(2)
#     write(GPIO1_25, LOW)
#     time.sleep(2)
   