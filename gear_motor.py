
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)
 
Motor1 = 16    # Input Pin
Motor2 = 18    # Input Pin
Motor3 = 22    # Enable Pin
 
GPIO.setup(Motor1,GPIO.OUT)
GPIO.setup(Motor2,GPIO.OUT)
GPIO.setup(Motor3,GPIO.OUT)
 
print "FORWARD MOTION"
GPIO.output(Motor1,GPIO.HIGH)
GPIO.output(Motor2,GPIO.LOW)
GPIO.output(Motor3,GPIO.HIGH)
 
sleep(3)
 
print "BACKWARD MOTION"
GPIO.output(Motor1,GPIO.LOW)
GPIO.output(Motor2,GPIO.HIGH)
GPIO.output(Motor3,GPIO.HIGH)
 
sleep(3)
 
print "STOP"
GPIO.output(Motor3,GPIO.LOW)
 
GPIO.cleanup()
