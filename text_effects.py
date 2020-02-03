import sys
import time

def scrolling_text(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.025)

def scrolling_text_slow(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.2)

def scrolling_text_fast(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.01)

def scrolling_text_super_fast(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.001)
        time.sleep(.001)