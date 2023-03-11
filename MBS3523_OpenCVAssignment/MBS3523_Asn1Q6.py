import cv2
import numpy as np

print(cv2.__version__)
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

Output = 0


def drawROI(event, x, y, flags, params):
    global x1
    global y1
    global x2
    global y2
    global Output

    if event == cv2.EVENT_LBUTTONDOWN:
        x1 = x
        y1 = y
        Output = 0

    if event == cv2.EVENT_LBUTTONUP:
        x2 = x
        y2 = y
        Output = 1

    if event == cv2.EVENT_RBUTTONUP:
        Output = 2


cv2.namedWindow("Image")
cv2.setMouseCallback("Image", drawROI)

while True:

    ret, frame = cam.read()

    if Output == 1:

        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0))  # Draw boundary rectangle
        # Detect if x or y range selected is equal to zero so to prevent crashes
        if x1 == x2:
            pass
        elif y1 == y2:
            pass
        # Show cropped ROI region
        else:
            croppedROI = frame[y1:y2, x1:x2]
            cv2.imshow('ROI', croppedROI)

    if Output == 2:  # Right Click
        frame[:, :] = frame  # Clear Selection
        # Detect ROI window, if there is no then skip destroy windows
        if cv2.getWindowProperty('ROI', cv2.WND_PROP_VISIBLE) >= 1:
            cv2.destroyWindow('ROI')

    # Add Text to the top middle of the window
    text = 'MBS3523 Assignment 1 - Q6    Name: Yu Hoi Lam'
    font = cv2.FONT_HERSHEY_SIMPLEX

    cv2.putText(frame, text, (120, 20), font, 0.5, (255, 255, 0), 2)

    cv2.imshow('Image', frame)
    if cv2.waitKey(2) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
