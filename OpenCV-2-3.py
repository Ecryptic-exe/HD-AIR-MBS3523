import cv2
print(cv2.__version__)

faceCascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')

img = cv2.imread('Resources/BTS.jpg')
img = cv2.resize(img, (int(img.shape[1]/1.1),int(img.shape[0]/1.1)))
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 5)
for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y),(x+w, y+h), (0,0,255),3)

cv2.imshow('BTS',img)
cv2.imshow('Gray Image', imgGray)

cv2.waitKey(0)