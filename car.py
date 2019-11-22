import RPi.GPIO as GPIO

class Car:

    PIN_LEFT, PIN_RIGHT, PIN_FORWARDS, PIN_BACKWARDS = 31, 33, 35, 37

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.PIN_LEFT, GPIO.OUT)
        GPIO.setup(self.PIN_RIGHT, GPIO.OUT)
        GPIO.setup(self.PIN_FORWARDS, GPIO.OUT)
        GPIO.setup(self.PIN_BACKWARDS, GPIO.OUT)

    def __del__(self):
        GPIO.cleanup()

    def stop(self):
        GPIO.output(self.PIN_FORWARDS, GPIO.LOW)
        GPIO.output(self.PIN_BACKWARDS, GPIO.LOW)

    def forwards(self):
        GPIO.output(self.PIN_FORWARDS, GPIO.HIGH)
        GPIO.output(self.PIN_BACKWARDS, GPIO.LOW)

    def backwards(self):
        GPIO.output(self.PIN_FORWARDS, GPIO.LOW)
        GPIO.output(self.PIN_BACKWARDS, GPIO.HIGH)

    def straight(self):
        GPIO.output(self.PIN_LEFT, GPIO.LOW)
        GPIO.output(self.PIN_RIGHT, GPIO.LOW)

    def left(self):
        GPIO.output(self.PIN_LEFT, GPIO.HIGH)
        GPIO.output(self.PIN_RIGHT, GPIO.LOW)

    def right(self):
        GPIO.output(self.PIN_LEFT, GPIO.LOW)
        GPIO.output(self.PIN_RIGHT, GPIO.HIGH)
