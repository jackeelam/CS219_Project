import sys
sys.path.append(".")
#import RPi.GPIO as GPIO
import time
import os
from servoFunction import servoFunction
servoClass = servoFunction()
while (1):
	letter = input("Selection: ") 
	if (letter == "s"):
		servoClass.rotateMotor(1)
		
