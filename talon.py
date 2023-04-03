import RPi.GPIO as gpio

MAX_DUTY_CYClE = 1000

class Talon:
    def __init__(self, pwmId, controlId):
        gpio.setmode(gpio.BOARD)
        self.controlId = controlId

        gpio.setup(pwmId, gpio.OUT)
        gpio.setup(controlId, gpio.OUT)

        self.pwm = gpio.PWM(pwmId, MAX_DUTY_CYClE)
        self.pwm.start(0)

    def set(power):
        self.pwm.ChangeDutyCycle(power*MAX_DUTY_CYClE)