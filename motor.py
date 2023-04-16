import RPi.GPIO as GPIO

class Motor:
    def __init__(self, r_en: int, l_en: int, rpwm:int, lpwm: int, polarity: bool):
        self.polarity = polarity

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(r_en,GPIO.OUT)
        GPIO.setup(l_en,GPIO.OUT)

        GPIO.output(r_en, True)
        GPIO.output(l_en, True)

        self.rpwm=GPIO.PWM(rpwm,100)
        self.lpwm = GPIO.PWM(lpwm, 100)
        self.rpwm.start(0)
        self.lpwm.start(0)
    
    def forward(self, power: float):
        adjPower = power * 100
        if (not polarity):
            self.rpwm.ChangeDutyCycle(adjPower)
            self.lpwm.ChangeDutyCycle(0)
        else:
            self.backward(power)

    def backward(self, power: float):
        adjPower = power * 100
        if (not polarity):
            self.lpwm.ChangeDutyCycle(adjPower)
            self.rpwm.ChangeDutyCycle(0)
        else:
            self.forward(power)