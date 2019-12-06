import cv2
import numpy as np
cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    #laplacian = cv2.Laplacian(frame,cv2.CV_64F)
    edges= cv2.Canny(frame,100,200)
    cv2.imshow('original',frame)
    cv2.imshow('edges',edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.release()
