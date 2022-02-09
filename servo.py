# Use Raspberry Pi to control Servo Motor motion
# Tutorial URL: http://osoyoo.com/?p=937

import RPi.GPIO as GPIO
import time
import os

GPIO.setwarnings(False)
# Set the layout for the pin declaration
GPIO.setmode(GPIO.BOARD)
# The Raspberry Pi pin 11(GPIO 18) connect to servo signal line(yellow wire)
# Pin 11 send PWM signal to control servo motion
GPIO.setup(11, GPIO.OUT)

# menu info
print("s: move one step")
position = 2.5
direction = 1
Servo = GPIO.PWM(11, 50)
Servo.start(position)
while True:
	# Now we will start with a PWM signal at 50Hz at pin 18. 
	# 50Hz should work for many servos very will. If not you can play with the frequency if you like.
	#Servo = GPIO.PWM(11, 50)						

	# Now the program asks for the direction the servo should turn.
	letter = input("Selection: ") 

	# You can play with the values.
	# 7.5 is in most cases the middle position
	# 12.5 is the value for a 180 degree move to the right
	# 2.5 is the value for a -90 degree move to the left
	if(letter == "s"):
		if (direction == 1 and position < 12.5):
			position = position + 2.5
			Servo.ChangeDutyCycle(position)
			if (position == 12.5):
				direction = 0

		elif (direction == 0 and position > 2.5):
			position = position - 2.5
			Servo.ChangeDutyCycle(position)
			if (position == 2.5):
				direction = 1
