from math import e

desiredPercentage = 50

class WheelSpeeds:
    def __init__(self, left, right):
        self.right = right
        self.left = left

    @staticmethod
    def convertImgToTurnSpeed(xVal, width):
        magnitude = xVal/width

        if xVal > 0:
            return WheelSpeeds(magnitude, -magnitude)
        elif (xVal < 0):
            return WheelSpeeds(-magnitude, magnitude)
        return (0, 0)

    @staticmethod
    def convertImgToDriveSpeed(xA, xB, yA, yB, width, height):
        area = abs(xB - xA) * abs(yB-yA)
        totArea = width * height

        percentage = area/totArea
        err = desiredPercentage - percentage

        return WheelSpeeds(e ** (-err), e ** (-err))