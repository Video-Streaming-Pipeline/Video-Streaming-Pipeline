import time
import torch
import torch.nn as nn
import torchvision.models as models
from torch.autograd import Variable
import cv2 as cv
import numpy as np

#get pretrained model
model = models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
#set device
if torch.cuda.is_available():
    print('Cuda avilable',torch.cuda.get_device_name(0))
    model=model.to('cuda')
else:
    print('cuda is not avilable')
#set inference
model.eval()

def get_bbox(frame,model):
    #preprocess frame
    frame=frame.reshape(1,frame.shape[2],frame.shape[0],frame.shape[1])
    frame=frame/255
    #set device
    if torch.cuda.is_available():
        frame=torch.cuda.FloatTensor(frame)
    else:
        frame=torch.FloatTensor(frame)
    return model(frame)

#cap = cv.VideoCapture('udpsrc port=9777 ! application/x-rtp ! rtph264depay ! h264parse ! avdec_h264 ! videoconvert ! appsink', cv.CAP_GSTREAMER)
cap = cv.VideoCapture('https://www.freedesktop.org/software/gstreamer-sdk/data/media/sintel_trailer-480p.webm')

if not cap.isOpened():
    print("VideoCapture not opened")
    exit(-1)

while True:
    ret, frame = cap.read()
    if not ret:
        print("empty frame")
        break
    t1 = time.time()
    predictions = get_bbox(frame,model)
    t2 = time.time()
    print('Inference time: %6.2fms' % ( (t2-t1)*100))
    scores=predictions[0]['scores']
    boxes=predictions[0]['boxes']
    img=frame
    for i in range(len(scores)):
        if scores[i] > 0.5:
            img=cv.rectangle(frame,(boxes[i][0],boxes[i][1]),
            (boxes[i][2],boxes[i][3]),3)
    cv.imshow("Result", img)
    if cv.waitKey(1) == 'r':
        break


cap.release()
cv.destroyWindow("Receiver")
