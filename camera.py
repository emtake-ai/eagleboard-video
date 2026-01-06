import cv2
import numpy as np 

cap = cv2.VideoCapture("/dev/video0")

while True:
    ret, frame = cap.read()
    cv2.imshow("d", frame)
    if cv2.waitKey(1) == 27:
        break

    