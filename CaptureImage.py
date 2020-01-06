import cv2
import os
import time
import matplotlib.pyplot as plt


cap = cv2.VideoCapture(0)
    
if cap.isOpened():
    ret, frame = cap.read()
    print(ret)
    print(frame)
else:
    ret = False

img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

directory = r"C:/Users/smarty/Desktop/"
os.chdir(directory)
print(os.listdir(directory)) 
filename = 'Intruder.jpg'
cv2.imwrite(filename, img1) 


cap.release()
