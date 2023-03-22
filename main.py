"""
Vidur Modgil and Griffin Kiewit
Dr. Sweigart
Yr 4 Engineering
3/22/23
"""

import cv2

cam = cv2.VideoCapture(0)
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector()) 

while (True):
    ret, frame = cam.read()
    if (ret):
        humans, _ = hog.detectMultiScale(frame,  
                        winStride=(5, 5), 
                        padding=(3, 3), 
                        scale=1.21)
        for (x, y, w, h) in humans: 
            cv2.rectangle(frame, (x, y),  
                        (x + w, y + h),  
                        (0, 0, 255), 2) 
        
        cv2.imshow("out", frame)