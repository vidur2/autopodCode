"""
Vidur Modgil and Griffin Kiewit
Dr. Sweigart
Yr 4 Engineering
3/22/23
"""

# import the necessary packages
import numpy as np
import cv2
from wheelspeeds import WheelSpeeds

def main():
    # initialize the HOG descriptor/person detector
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    cv2.startWindowThread()

    # open webcam video stream
    cap = cv2.VideoCapture(0)

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        scale_percent = 50 # percent of original size
        width = int(frame.shape[1] * scale_percent / 100)
        height = int(frame.shape[0] * scale_percent / 100)
        dim = (width, height)
        
        # resize image
        frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
        # using a greyscale picture, also for faster detection
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        # detect people in the image
        # returns the bounding boxes for the detected objects
        boxes, weights = hog.detectMultiScale(frame, winStride=(8,8) )

        boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

        biggestArea = 0
        largest = (0, 0, 0, 0)
        (lXA, lYA, lXB, lYB) = (0, 0, 0, 0)

        for (xA, yA, xB, yB) in boxes:
            # display the detected boxes in the colour picture 
            cv2.rectangle(frame, (xA, yA), (xB, yB),
                            (0, 255, 0), 2)
            area = (xB - xA) * (yB - yA)

            if (area > biggestArea):
                biggestArea = area
                lXA, lXB, lYA, lYB = xA, xB, yA, yB
        xCenter = (lXA + lXB)/2 - (width/2)
        turnSpeed = WheelSpeeds.convertImgToTurnSpeed(xCenter, width)
        driveSpeed = WheelSpeeds.convertImgToDriveSpeed(lXA, lXB, lYA, lYB, width, height)
        
        # Display the resulting frame
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    # and release the output
    out.release()
    # finally, close the window
    cv2.destroyAllWindows()
    cv2.waitKey(1)

if (__name__ == "__main__"):
    main()