# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 21:56:49 2018

@author: pc
"""
import cv2

cam_input =cv2.VideoCapture(1) 
while True:
    ret, frame = cam_input.read()
    cv2.imshow("Imsthage", frame) 
    if cv2.waitKey(1) & 0xFF == ord('1'):
        cv2.imwrite("/opt/code/image/fangjian2.jpeg", frame)
        break
cam_input.release()
cv2.destroyAllWindows()  