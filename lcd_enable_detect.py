import sys
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.ADC as ADC
from Adafruit_CharLCD import Adafruit_CharLCD
from NokiaLCD import NokiaLCD
from collections import OrderedDict
import commands
import json
import time

#import game libraries
from gamelibs import config_manager
from gamelibs import lcd_manager

#Who am I? Get my ip address
ipaddress = commands.getoutput("/sbin/ifconfig").split("\n")[1].split()[1][5:]

#configuration. Load the config and get various dictionaries and arrays back
configFileName = 'game-' + ipaddress +'.config'
config, controlids, controldefs, sortedlist = config_manager.loadConfig(configFileName)

#initialise all of the LCDs and return a list of LCD objects
myLcdManager = lcd_manager.LcdManager(sortedlist, config)

myLcdManager.display(str(config['local']['controls']['0']['display']['pin']) + ' (top)', config['local']['controls']['0']['display']['width'], '0')
for ctrlid in controlids:
    myLcdManager.display(str(config['local']['controls'][ctrlid]['display']['pin']) + " (" + str(ctrlid) + ")", config['local']['controls'][ctrlid]['display']['width'], ctrlid)
    
#Main loop
while(True):
	pass
