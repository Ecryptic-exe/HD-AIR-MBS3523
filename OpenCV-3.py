import cv2
import numpy as np
print(cv2.__version__)

frame = np.zeros([500,500],dtype=np.uint8)
print(frame.shape)

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    #print(frame.shape)

    #frame[100:200, 200:300] = 135
    # From range 1(row,colomn) to range 2 replacing with colour

    frameCrop = frame[100:300, 200:400] #Region of Interest (ROI)
    cv2.imshow('Cropped Frame', frameCrop)

    frameROIGray = cv2.cvtColor(frameCrop, cv2.COLOR_BGR2GRAY) #BGR to Gray
    frameROIGray = cv2.cvtColor(frameROIGray,cv2.COLOR_GRAY2BGR) #Gray to BGR (Convert)

    #print(frameROIGray.shape)
    newFrame = frame
    frame[100:300, 200:400] = frameROIGray

    cv2.imshow('Frame', frame)
    cv2.imshow('Cropped ROI Frame', frameROIGray)

    if cv2.waitKey (2) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()