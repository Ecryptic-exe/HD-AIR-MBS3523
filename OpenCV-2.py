import cv2
import numpy as np
print(cv2.__version__)

kernel = np.ones((5,5), np.uint8)

img = cv2.imread('Resources/lena.png')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img = cv2.resize(img, (int(img.shape[1]/1.1),int(img.shape[0]/1.1)))

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (5,5),0)
imgEdge = cv2.Canny(imgBlur, 100, 100)
imgErode = cv2.erode(img, kernel, iterations=1)
imgDil = cv2.dilate(imgEdge, kernel, iterations=1)

cv2.imshow('Lena',img)
cv2.imshow('Gray Image', imgGray)
cv2.imshow('Blur Image', imgBlur)
cv2.imshow('Canny Image', imgEdge)
cv2.imshow('Erosion', imgErode)
cv2.imshow('Dilation', imgDil)

cv2.waitKey(0)