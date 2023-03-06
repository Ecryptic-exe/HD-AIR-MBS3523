import cv2
import numpy as np

def drawShape(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x,y), 30, (255, 0, 0), -1)
        #print(event)
        #print(x, y)

    elif event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(img, (x, y), (x + 20, y + 30), (0, 0, 255), -1)

cv2.namedWindow("Image")
cv2.setMouseCallback("Image", drawShape)

#img = np.zeros((500, 500, 3), np.uint8)
img = cv2.imread("Resources/lena.png")

while True:
    cv2.imshow("Image", img)
    if cv2.waitKey(2) & 0xff == 27:
        break

cv2.destroyAllWindows()

#wtf bugged
