import serial
import cv2
import time
print(serial.__version__)

ser = serial.Serial(port='COM4', baudrate=115200, timeout=1)

time.sleep(2)

def nil(x):
    pass

cv2.namedWindow('Trackbars')
cv2.createTrackbar('ServoPos', 'Trackbars', 90, 180, nil)

while True:
    servoPos1 = str(cv2.getTrackbarPos('ServoPos', 'Trackbars'))
    servoPos1 = servoPos1 + '\r'
    ser.write(servoPos1.encode('UTF-8'))
    print(servoPos1)
    time.sleep(0.1)

    if cv2.waitKey(1) & 0xff == 27:
        break

ser.close()
cv2.destroyAllWindows()
