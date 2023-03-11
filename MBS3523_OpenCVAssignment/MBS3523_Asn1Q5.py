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

    cv2.line(frame, (0, y), (1000, y), (255, 0, 0), 5)
    cv2.line(frame, (x, 0), (x, 1000), (255, 0, 0), 5)

    # Add Text to the top middle of the window
    text = 'MBS3523 Assignment 1 - Q5    Name: Yu Hoi Lam'
    font = cv2.FONT_HERSHEY_SIMPLEX

    cv2.putText(frame, text, (120, 20), font, 0.5, (255, 255, 0), 2)

    cv2.imshow('Frame', frame)

    if cv2.waitKey(2) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
