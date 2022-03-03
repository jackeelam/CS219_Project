import RPi.GPIO as GPIO
import os, sys

from rfidReader import rfidReader

reader = rfidReader()
text = input('New data:')
reader.writeTag(text)
id, text = reader.readTag()
print(id)
print(text)
GPIO.cleanup()