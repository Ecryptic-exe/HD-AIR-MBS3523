import cv2

print(cv2.__version__)

cam = cv2.VideoCapture(0)

dispW = 640
dispH = 480

#  Box Properties
BoxWidth = 80
BoxHeight = 80
tlC = 50  # Top Left Column
tlR = 75  # Top Left Row
lrC = tlC + BoxHeight
lrR = tlR + BoxHeight
deltaC = 2
deltaR = 2

while True:

    ret, frame = cam.read()

    #  Rectangle Bounce
    if tlC + deltaC < 0 or lrC + deltaC > dispW - 1:
        deltaC = deltaC * (-1)
    if tlR + deltaR < 0 or lrR + deltaR > dispH - 1:
        deltaR = deltaR * (-1)
    tlC = tlC + deltaC
    tlR = tlR + deltaR
    lrC = lrC + deltaC
    lrR = lrR + deltaR
    cv2.rectangle(frame,(tlC, tlR),(lrC, lrR),(0,0,255),3)

    # Add Text to the top middle of the window
    text = 'MBS3523 Assignment 1 - Q3    Name: Yu Hoi Lam'
    font = cv2.FONT_HERSHEY_SIMPLEX

    cv2.putText(frame, text, (120, 20), font, 0.5, (255, 255, 0), 2)

    cv2.imshow('Webcam', frame)

    if cv2.waitKey(2) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
