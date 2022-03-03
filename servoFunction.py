# Use Raspberry Pi to control Servo Motor motion
# Tutorial URL: http://osoyoo.com/?p=937

import RPi.GPIO as GPIO
import time
import os

class servoFunction:
	def __init__(self):	
		GPIO.setwarnings(False)
		# Set the layout for the pin declaration
		GPIO.setmode(GPIO.BOARD)
		# The Raspberry Pi pin 11(GPIO 18) connect to servo signal line(yellow wire)
		# Pin 11 send PWM signal to control servo motion
		GPIO.setup(11, GPIO.OUT)
		self.position = 2.5
		self.direction = 1
		self.Servo = GPIO.PWM(11, 50)
		self.Servo.start(self.position)

	def rotateMotor(self, rotate):
		if (rotate == 1):
			if (self.direction == 1 and self.position < 12.5):
				steps = 5
				stepSize = 2.5 / steps
				for i in range(0, 5):
					self.position = self.position + stepSize
					print(self.position, "/n")
					self.Servo.ChangeDutyCycle(self.position)
					time.sleep(0.5)
				if (self.position == 12.5):
					self.direction = 0

			elif (self.direction == 0 and self.position > 2.5):
				steps = 5
				stepSize = 2.5 / steps
				for i in range(0, 5):
					self.position = self.position - stepSize
					print(self.position, "/n")
					self.Servo.ChangeDutyCycle(self.position)
					time.sleep(0.5)
				if (self.position == 2.5):
					self.direction = 1
			time.sleep(1)
