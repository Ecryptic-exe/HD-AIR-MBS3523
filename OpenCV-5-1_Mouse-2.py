import cv2
import numpy as np

EVT = 0

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)


def drawShape(event, x, y, flags, params):
    global EVT
    global PNT

    if event == cv2.EVENT_LBUTTONDOWN:
        #cv2.circle(frame, (x, y), 30, (255, 0, 0), -1)
        EVT = event
        PNT = (x, y)
        print(event)
        print(x, y)

    if event == cv2.EVENT_RBUTTONDOWN:
        EVT = event
        print(event)

cv2.namedWindow("Image")
cv2.setMouseCallback("Image", drawShape)

while True:
    ret, frame = cam.read()
    # print(frame.shape)
    if EVT == 1:
        # cv2.circle(frame, PNT, 30, (255, 0, 0), -1)
        ROI = np.zeros([300, 300, 3], np.uint8)

        # row, col (y,x)
        ROI[:, :] = frame[PNT[1], PNT[0]]
        cv2.imshow('ROI', ROI)

    if EVT == 2:
        frame[:, :] = frame

    cv2.imshow('Image', frame)
    if cv2.waitKey(2) & 0xff == 27:
        break

cam.release()
cv2.destroyAllWindows()
