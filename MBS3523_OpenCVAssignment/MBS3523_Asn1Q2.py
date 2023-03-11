import cv2

print(cv2.__version__)

cam = cv2.VideoCapture(0)
while True:
    ret, image = cam.read()
    # Color Conversion
    imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Show both windows
    cv2.imshow('Frame', image)
    cv2.imshow('Gray Image', imgGray)

    if cv2.waitKey(1) & 0xff == 27:
        break

cam.release()
cv2.destroyAllWindows()
