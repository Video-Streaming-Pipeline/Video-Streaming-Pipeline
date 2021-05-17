import time
import torch
import torch.nn as nn
import torchvision.models as models
from torch.autograd import Variable
import cv2 as cv
import numpy as np
from multiprocessing import Process

def receive_CNN():
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

    #cap = cv.VideoCapture('udpsrc port=9777 ! application/x-rtp ! rtph264depay ! h264parse ! avdec_h264 ! videoconvert ! appsink', cv.CAP_GSTREAMER) # with raspberry pi
    cap = cv.VideoCapture('https://www.freedesktop.org/software/gstreamer-sdk/data/media/sintel_trailer-480p.webm') #example

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
                img=cv.rectangle(frame,(int(boxes[i][0]),int(boxes[i][1])),
                (int(boxes[i][2]),int(boxes[i][3])),(0,255,0),3)
        cv.imshow("Result", img)
        if cv.waitKey(1) == 27:
            break
    cap.release()
    cv.destroyWindow("Receiver")

def sender():
    cap = cv.VideoCapture("appsrc ! videoconvert ! appsink", cv.CAP_GSTREAMER) # CNN 처리결과 받아와서
    out = cv.VideoWriter('appsrc ! videoconvert ! x264enc tune=zerolatency ! rtph264pay ! udpsink host=221.164.144.187 port=9777', 0, 30, (224, 224))

    while True:
        res, frame = cap.read()
        if res:
            re_frame = cv.resize(frame, (224, 224), 0, 0, cv.INTER_LINEAR)
            out.write(re_frame)
            cv.imshow("image", re_frame)
            if cv.waitKey(20) == 27:
                break
    cap.release()
    out.release()

if __name__ == '__main__':
    s = Process(target=sender)
    r = Process(target=receive_CNN)
    s.start()
    r.start()
    s.join()
    r.join()

    cv.destroyAllWindows()