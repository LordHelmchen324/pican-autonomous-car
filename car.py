import RPi.GPIO as GPIO

class Car:

    PIN_LEFT, PIN_RIGHT, PIN_FORWARD, PIN_BACKWARD = 31, 33, 35, 37

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.PIN_LEFT, GPIO.OUT)
        GPIO.setup(self.PIN_RIGHT, GPIO.OUT)
        GPIO.setup(self.PIN_FORWARD, GPIO.OUT)
        GPIO.setup(self.PIN_BACKWARD, GPIO.OUT)

    def __del__(self):
        GPIO.cleanup()

    def stop(self):
        GPIO.output(self.PIN_FORWARD, GPIO.LOW)
        GPIO.output(self.PIN_BACKWARD, GPIO.LOW)

    def forwards(self):
        GPIO.output(self.PIN_FORWARD, GPIO.HIGH)
        GPIO.output(self.PIN_BACKWARD, GPIO.LOW)

    def backwards(self):
        GPIO.output(self.PIN_FORWARD, GPIO.LOW)
        GPIO.output(self.PIN_BACKWARD, GPIO.HIGH)

    def straight(self):
        GPIO.output(self.PIN_LEFT, GPIO.LOW)
        GPIO.output(self.PIN_RIGHT, GPIO.LOW)

    def left(self):
        GPIO.output(self.PIN_LEFT, GPIO.HIGH)
        GPIO.output(self.PIN_RIGHT, GPIO.LOW)

    def right(self):
        GPIO.output(self.PIN_LEFT, GPIO.LOW)
        GPIO.output(self.PIN_RIGHT, GPIO.HIGH)
