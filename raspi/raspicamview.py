import cv2 as cv
from picamera import Picamera

cap = cv.VideoCapture(-1)
writer = cv.VideoWriter('appsrc ! videoconvert ! x264enc tune=zerolatency ! rtph264pay ! gdppay ! udpsink host=127.0.0.1 port=5000', 0, 30, (224,  224)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
 


while true:
    frame = cap.read()
    cv.imshow('image', frame)
    writer.write(frame)
    if cv.waitKey(1) == ord('q'):
        break
                        
