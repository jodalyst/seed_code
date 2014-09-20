from __future__ import print_function
from time import sleep
import time
import subprocess
import random
unload_spi = subprocess.Popen('sudo rmmod spi_bcm2708', shell=True, stdout=subprocess.PIPE)
start_spi = subprocess.Popen('sudo modprobe spi_bcm2708', shell=True, stdout=subprocess.PIPE)
sleep(3)
import smtplib

import RPi.GPIO as GPIO
import spidev
import sys
import math
import random
board_type = sys.argv[-1]
GPIO.setmode(GPIO.BCM)

GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(22, GPIO.OUT)


def get_adc(channel):                                   
    if ((channel > 1) or (channel < 0)):                
        return -1
    r = spi.xfer2([1,(2+channel)<<6,0])  
    ret = ((r[1]&31) << 6) + (r[2] >> 2)
    return ret

spi = spidev.SpiDev()
spi.open(0,0)    

def readAnalogInput():
    return get_adc(1)

def writeDigitalOutput(pin,value):
    if pin == 4:
        thing = 22
    else:
        return "Error: pin not correct!"
    if value in [1,True]:
        GPIO.output(thing,1)
    elif value in [0,False]:
        GPIO.output(thing,0)
    else:
        return "ERROR: input value not correct"

def readDigitalInput(x):
    if x not in [1,2,3]:
        return "Error: pin not correct!"
    if x ==1:
        pin=25
    elif x==2:
        pin = 24
    else:
        pin = 23
        
    return GPIO.input(pin)

def delay(ms):
    sleep(ms*1.0/1000.)

def randomTime(upToSeconds):
    return random.random()*upToSeconds
    
def roundUpDown(value):
    if value>=0.5:
        return 1
    else:
        return 0

def randomChoice():
    return roundUpDown(random.random())

fromAddress = 'seedtemp14@gmail.com'
username = 'seedtemp14'
password = 'seedseed'
    
