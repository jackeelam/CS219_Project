import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)
 
Motor1 = 16    # Input Pin
Motor2 = 18    # Input Pin
Motor3 = 22    # Enable Pin

GPIO.setup(Motor1,GPIO.OUT)
GPIO.setup(Motor2,GPIO.OUT)
GPIO.setup(Motor3,GPIO.OUT)

p = GPIO.PWM(Motor3,100)          #GPIO19 as PWM output, with 100Hz frequency

p.start(10)
GPIO.output(Motor1,GPIO.HIGH)
GPIO.output(Motor2,GPIO.LOW)
sleep(5)

'''
p.start(0)

for x in range (50):                          #execute loop for 50 times, x being incremented from 0 to 49.
    GPIO.output(Motor1,GPIO.HIGH)
    GPIO.output(Motor2,GPIO.LOW)
    p.ChangeDutyCycle(x)               #change duty cycle for varying the brightness of LED.
    sleep(0.1)                           #sleep for 100m second 
'''

''' 
print("FORWARD MOTION")
GPIO.output(Motor1,GPIO.HIGH)
GPIO.output(Motor2,GPIO.LOW)
GPIO.output(Motor3,GPIO.HIGH)
 
sleep(5)
 
print("BACKWARD MOTION")
GPIO.output(Motor1,GPIO.LOW)
GPIO.output(Motor2,GPIO.HIGH)
GPIO.output(Motor3,GPIO.HIGH)
 
sleep(5)
''' 
print("STOP")
GPIO.output(Motor3,GPIO.LOW)
 
GPIO.cleanup()
