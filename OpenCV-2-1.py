#Webcam Distortion

import cv2
import numpy as np
print(cv2.__version__)

kernel = np.ones((5,5), np.uint8)

cam = cv2.VideoCapture(0)
while True:
 ret, image = cam.read()
 #Color Convertion
 imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 0)
 imgEdge = cv2.Canny(imgBlur, 100, 100)
 imgErode = cv2.erode(image, kernel, iterations=1)
 imgDil = cv2.dilate(imgEdge, kernel, iterations=1)

 cv2.imshow('Frame', image)
 #Show Variations
 cv2.imshow('Gray Image', imgGray)
 cv2.imshow('Blur Image', imgBlur)
 cv2.imshow('Canny Image', imgEdge)
 cv2.imshow('Erosion', imgErode)
 cv2.imshow('Dilation', imgDil)

 if cv2.waitKey(1) & 0xff == ord('q'):
     break

cam.release()
cv2.destroyAllWindows()