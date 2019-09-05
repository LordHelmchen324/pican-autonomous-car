import RPi.GPIO as GPIO
from time import sleep

lftPin, rgtPin, fwdPin, bwdPin = 31, 33, 35, 37

GPIO.setmode(GPIO.BOARD)
GPIO.setup(lftPin, GPIO.OUT)
GPIO.setup(rgtPin, GPIO.OUT)
GPIO.setup(fwdPin, GPIO.OUT)
GPIO.setup(bwdPin, GPIO.OUT)

def stop():
    GPIO.output(fwdPin, GPIO.LOW)
    GPIO.output(bwdPin, GPIO.LOW)

def goForwards():
    GPIO.output(fwdPin, GPIO.HIGH)
    GPIO.output(bwdPin, GPIO.LOW)

def goBackwards():
    GPIO.output(fwdPin, GPIO.LOW)
    GPIO.output(bwdPin, GPIO.HIGH)

def steerStraight():
    GPIO.output(lftPin, GPIO.LOW)
    GPIO.output(rgtPin, GPIO.LOW)

def steerLeft():
    GPIO.output(lftPin, GPIO.HIGH)
    GPIO.output(rgtPin, GPIO.LOW)

def steerRight():
    GPIO.output(lftPin, GPIO.LOW)
    GPIO.output(rgtPin, GPIO.HIGH)

# ------------------------

stop()
steerStraight()

sleep(3)

goForwards()
sleep(1.5)
stop()
sleep(0.5)
steerLeft()
goBackwards()
sleep(1.5)
stop()
sleep(0.5)
steerRight()
goForwards()
sleep(1.5)
stop()
steerStraight()

# ------------------------

GPIO.cleanup()
