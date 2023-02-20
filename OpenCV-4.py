import cv2
print(cv2.__version__)

cam = cv2.VideoCapture(0)

def nil(x):
    pass

cv2.namedWindow('Frame')
cv2.createTrackbar('x', 'Frame', 0, 540, nil)
cv2.createTrackbar('y', 'Frame', 0, 380, nil)

while True:
    ret, frame = cam.read()

    x = cv2.getTrackbarPos('x', 'Frame')
    y = cv2.getTrackbarPos('y', 'Frame')

    cv2.rectangle(frame, (x, y), (x+100, y+100), (255, 0, 0), 5)

    cv2.imshow('Frame',frame)
    if cv2.waitKey (2) & 0xff == 27:
        break

cam.release()
cv2.destroyAllWindows()
