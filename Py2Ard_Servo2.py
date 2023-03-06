import serial
import cv2
import time

print(serial.__version__)

ser = serial.Serial(port='COM4', baudrate=115200, timeout=1)
time.sleep(2)
faceCascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
dispW = 640
dispH = 480
angle = 90

while True:
    ret, img = cam.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)

        faceXcenter = x + w / 2
        faceYcenter = y + h / 2
        errorPan = faceXcenter - dispW / 2
        print(errorPan)

        if abs(errorPan) > 20:
            angle = angle - errorPan / 10  # proportional const
        if angle > 180:
            angle = 180
        if angle < 0:
            angle = 0
        print(angle)
        angle = int(angle)

    cv2.imshow('Image', img)

    ser.write([angle])

    time.sleep(0.1)

    if cv2.waitKey(1) & 0xff == 27:
        break

# ser.close()
cv2.destroyAllWindows()
