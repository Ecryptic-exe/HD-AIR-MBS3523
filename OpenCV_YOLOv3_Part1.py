import cv2
import numpy as np

print(cv2.__version__)

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

classes = []
with open('YOLO/coco80.names', 'r') as f:
    classes = f.read().splitlines()
    print(len(classes))

net = cv2.dnn.readNetFromDarknet('YOLO/yolov3-320.cfg', 'YOLO/yolov3-320.weights')
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

while True:
    ret, frame = cam.read()
    # img1 = np.concatenate((frame, frame), axis=1)  # Stack frame
    blob = cv2.dnn.blobFromImage(frame, 1/255., (320, 320), (0, 0, 0), swapRB=True, crop=False)
    net.setInput(blob)
    layerNames = net.getLayerNames()
    # print(len(layerNames))
    outputLayers = net.getUnconnectedOutLayersNames()
    # print(outputLayers)
    output = net.forward(outputLayers)

    bBox = []
    conf = []
    cid = []
    
    # print(len(output))
    # print(output[0].shape)  # Predict Large / (Region, Choice)
    # print(output[1].shape)  # Predict Medium
    # print(output[2].shape)  # Predict Small

    cv2.imshow('Webcam', frame)
    if cv2.waitKey(2) & 0xff == 27:
        break

cam.release()
cv2.destroyAllWindows()
