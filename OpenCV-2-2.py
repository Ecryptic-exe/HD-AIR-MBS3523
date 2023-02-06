import cv2
print(cv2.__version__)

cam = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')

while True:
    ret, frame = cam.read()
    imgGray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 5) #Detect different scale
    print(faces)
    # 1 set of numbers is contained in [x, y, w, h], 2 or more rectangles are presented by [[x1, y1, w1, h1][x2, y2, w2, h2]]
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y),(x+w, y+h), (0,0,255),3) #Frames, Point1: (x, y)//Point 2: (x+w, y+h), w and h are size of the rectangle

    cv2.imshow('Webcam',frame)
    cv2.imshow('Gray', imgGray)
    if cv2.waitKey (2) & 0xff == ord('q'):
        break;

cam.release()
cv2.destroyAllWindows()