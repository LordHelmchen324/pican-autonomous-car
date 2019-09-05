import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)

# Left
GPIO.output(31, GPIO.HIGH)
sleep(2)
GPIO.output(31, GPIO.LOW)

sleep(1)

# Right
GPIO.output(33, GPIO.HIGH)
sleep(2)
GPIO.output(33, GPIO.LOW)

sleep(1)

# Forwards
GPIO.output(35, GPIO.HIGH)
sleep(2)
GPIO.output(35, GPIO.LOW)

sleep(1)

# Backwards
GPIO.output(37, GPIO.HIGH)
sleep(2)
GPIO.output(37, GPIO.LOW)

GPIO.cleanup()
