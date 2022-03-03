
#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import os, sys

class suppress_output:
    def __init__(self, suppress_stdout=False, suppress_stderr=False):
        self.suppress_stdout = suppress_stdout
        self.suppress_stderr = suppress_stderr
        self._stdout = None
        self._stderr = None

    def __enter__(self):
        devnull = open(os.devnull, "w")
        if self.suppress_stdout:
            self._stdout = sys.stdout
            sys.stdout = devnull

        if self.suppress_stderr:
            self._stderr = sys.stderr
            sys.stderr = devnull

    def __exit__(self, *args):
        if self.suppress_stdout:
            sys.stdout = self._stdout
        if self.suppress_stderr:
            sys.stderr = self._stderr

class rfidReader:
    def __init__(self):
        self.reader = SimpleMFRC522()

    def readTag(self):
        print("Reading")
        try:
            with suppress_output(suppress_stdout=True, suppress_stderr=True):
                id, text = self.reader.read()
        finally:
            return id, text
    def writeTag(self, data):
        print("Writing")
        try:
            with suppress_output(suppress_stdout=True, suppress_stderr=True):
                self.reader.write(data)
        finally:
            return

'''
reader = rfidReader()
text = input('New data:')
reader.writeTag(text)
GPIO.cleanup()
'''
# try:
#         text = input('New data:')
#         print("Now place your tag to write")
#         reader.write(text)
#         print("Written")
# finally:
#         GPIO.cleanup()
