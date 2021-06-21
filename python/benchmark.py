import time
import torch
import torch.nn as nn
import torchvision.models as models
from torch.autograd import Variable

if torch.cuda.is_available():
    print('Cuda avilable',torch.cuda.get_device_name(0))
else:
    print('cuda is not avilable')
def tput(model, name):
    with torch.no_grad():
        try:
            batchsize=1
            print(f'batchsize: {batchsize}')
            input = torch.rand(batchsize,3,224,224)
            if torch.cuda.is_available():
                input=input.to('cuda')
                model=model.to('cuda')
            model.eval()
            model(input)
            T = 0
            for _ in range(5):
                t1 = time.time()
                model(input)
                t2 = time.time()
                T += (t2-t1)
            T /= 5
            print('Forward throughput: %10s : %6.2fms' % (name, T*100))
        except:
            print(f'Forward throughput: {name} is not available')

if __name__ == '__main__':
    print('Torchvision Object Detection, Instance Segmentation and Person Keypoint Detection test')
    tput(models.detection.fasterrcnn_resnet50_fpn(), 'fasterrcnn_resnet50_fpn')
    tput(models.detection.fasterrcnn_mobilenet_v3_large_fpn(), 'fasterrcnn_mobilenet_v3_large_fpn')
    tput(models.detection.fasterrcnn_mobilenet_v3_large_320_fpn(), 'fasterrcnn_mobilenet_v3_large_320_fpn')
    tput(models.detection.retinanet_resnet50_fpn(), 'retinanet_resnet50_fpn')
    tput(models.detection.maskrcnn_resnet50_fpn(), 'maskrcnn_resnet50_fpn')
