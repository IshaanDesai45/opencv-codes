import cv2
import numpy as np
cap=cv2.VideoCapture(0)

while True :
    _,frame= cap.read()
    hsv= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow('frame',frame)
    cv2.imshow('hsv',hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()
cap.release()

