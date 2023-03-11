import cv2

print(cv2.__version__)

cam = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')

while True:

    ret, frame = cam.read()
    faces = faceCascade.detectMultiScale(frame, 1.1, 5)  # Detect different scale

    for (x, y, w, h) in faces:
        faces = frame[y:y + h, x:x + w]  # Extract Faces

        imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert Face to Gray
        faceCLR = cv2.cvtColor(imgGray, cv2.COLOR_GRAY2BGR)  # Convert Format to BGR

        faceCLR[y:y + h, x:x + w] = faces  # Replace Frame

        cv2.rectangle(faceCLR, (x, y), (x + w, y + h), (0, 0, 255), 3)  # Draw Boundary Box

        # Add Text to the top middle of the window
        text = 'MBS3523 Assignment 1 - Q4    Name: Yu Hoi Lam'
        font = cv2.FONT_HERSHEY_SIMPLEX

        cv2.putText(faceCLR, text, (120, 20), font, 0.5, (255, 255, 0), 2)

    cv2.imshow('Webcam2', faceCLR)

    if cv2.waitKey(2) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
