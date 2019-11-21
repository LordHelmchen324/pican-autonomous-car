import RPi.GPIO as GPIO

class Car:

    PIN_LEFT, PIN_RIGHT, PIN_FORWARD, PIN_BACKWARD = 31, 33, 35, 37

    def __init__():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(PIN_LEFT, GPIO.OUT)
        GPIO.setup(PIN_RIGHT, GPIO.OUT)
        GPIO.setup(PIN_FORWARD, GPIO.OUT)
        GPIO.setup(PIN_BACKWARD, GPIO.OUT)

    def __del__():
        GPIO.cleanup()

    def stop():
        GPIO.output(fwdPin, GPIO.LOW)
        GPIO.output(bwdPin, GPIO.LOW)

    def forwards():
        GPIO.output(fwdPin, GPIO.HIGH)
        GPIO.output(bwdPin, GPIO.LOW)

    def backwards():
        GPIO.output(fwdPin, GPIO.LOW)
        GPIO.output(bwdPin, GPIO.HIGH)

    def straight():
        GPIO.output(lftPin, GPIO.LOW)
        GPIO.output(rgtPin, GPIO.LOW)

    def left():
        GPIO.output(lftPin, GPIO.HIGH)
        GPIO.output(rgtPin, GPIO.LOW)

    def right():
        GPIO.output(lftPin, GPIO.LOW)
        GPIO.output(rgtPin, GPIO.HIGH)
