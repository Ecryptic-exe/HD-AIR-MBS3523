import cv2
print(cv2.__version__)

cam = cv2.VideoCapture(0)

def nil(x):
    pass
cv2.namedWindow('Trackbar')
cv2.createTrackbar('hueLow', 'Trackbar', 0, 179, nil)
cv2.createTrackbar('hueHigh', 'Trackbar', 179, 179, nil)
cv2.createTrackbar('satLow', 'Trackbar', 0, 255, nil)
cv2.createTrackbar('satHigh', 'Trackbar', 255, 255, nil)
cv2.createTrackbar('valLow', 'Trackbar', 0, 255, nil)
cv2.createTrackbar('valHigh', 'Trackbar', 255, 255, nil)

while True:
    ret, frame = cam.read()

    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    hueLow = cv2.getTrackbarPos('hueLow', 'Trackbar')
    hueHigh = cv2.getTrackbarPos('hueHigh', 'Trackbar')
    satLow = cv2.getTrackbarPos('satLow', 'Trackbar')
    satHigh = cv2.getTrackbarPos('satHigh', 'Trackbar')
    valLow = cv2.getTrackbarPos('valLow', 'Trackbar')
    valHigh = cv2.getTrackbarPos('valHigh', 'Trackbar')

    FG_Mask = cv2.inRange(frameHSV, (hueLow, satLow, valLow), (hueHigh, satHigh, valHigh))

    cv2.imshow('FG_Mask', FG_Mask)

    #show masked layer color
    FG = cv2.bitwise_and(frame, frame, mask=FG_Mask)
    cv2.imshow('FG', FG)

    #find contours
    contours, hierachy = cv2.findContours(FG_Mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

    for contour in contours:
        cv2.drawContours(frame,[contour], 0,(255,0,0),5)
        area = cv2.contourArea(contour)
        if area > 100: # noise reduction
            (x,y,w,h) = cv2.boundingRect(contour)
            cv2.rectangle(frame,(x,y,),(x+y,w+h), (0,0,255), 5)

    cv2.imshow('img', frame)

    if cv2.waitKey(2) & 0xff == 27:
        break

cam.release()
cv2.destroyAllWindows()
