import RPi.GPIO as GPIO
import time
import random

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

GPIO.setup(8, GPIO.OUT, initial=GPIO.HIGH)
n = 0.1

def letter():
    GPIO.output(8, GPIO.LOW)
    t = float(random.sample((1, 3), 1)[0])
    time.sleep(t*n)
    GPIO.output(8, GPIO.HIGH)
    time.sleep(n)

for x in range(120):
    for y in range(random.randint(3, 10)):
        for z in range(random.randint(3, 10)):
            letter()
        time.sleep(0.3)
    time.sleep(0.7)
GPIO.cleanup()
