from motor import Motor
from wheelspeeds import WheelSpeeds

class Drivetrain:
    def __init__(self, lMotor: Motor, rMotor: Motor):
        self.lMotor = lMotor
        self.rMotor = rMotor
    
    def drive(speed: WheelSpeeds):
        self.lMotor.forward(speed.left)
        self.rMotor.forward(speed.right)