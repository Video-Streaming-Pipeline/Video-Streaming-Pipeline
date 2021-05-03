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
    print('Torchvision classification models test')
    tput(models.alexnet(), 'alexnet')
    tput(models.mobilenet_v2(), 'mobilenet_v2')
    tput(models.mobilenet_v3_large(), 'mobilenet_v3_large')
    tput(models.mobilenet_v3_small(), 'mobilenet_v3_small')
    tput(models.mobilenet_v3_small(), 'mobilenet_v3_small')
    tput(models.vgg11(), 'VGG11')
    tput(models.vgg13(), 'VGG13')
    tput(models.vgg16(), 'VGG16')
    tput(models.vgg19(), 'VGG19')
    tput(models.resnet18(), 'resnet18')
    tput(models.resnet50(), 'resnet50')
    tput(models.resnet101(), 'resnet101')
    tput(models.resnet152(), 'resnet152')
    tput(models.densenet121(), 'densenet121')
    tput(models.densenet201(), 'densenet201')
    print('Torchvision Object Detection, Instance Segmentation and Person Keypoint Detection test')
    tput(models.detection.fasterrcnn_resnet50_fpn(), 'fasterrcnn_resnet50_fpn')
    tput(models.detection.fasterrcnn_mobilenet_v3_large_fpn(), 'fasterrcnn_mobilenet_v3_large_fpn')
    tput(models.detection.fasterrcnn_mobilenet_v3_large_320_fpn(), 'fasterrcnn_mobilenet_v3_large_320_fpn')
    tput(models.detection.retinanet_resnet50_fpn(), 'retinanet_resnet50_fpn')
    tput(models.detection.maskrcnn_resnet50_fpn(), 'maskrcnn_resnet50_fpn')
    tput(models.detection.keypointrcnn_resnet50_fpn(), 'maskrcnn_resnet50_fpn')
    print('Torchvision semantic segmentation models test')
    tput(models.segmentation.fcn_resnet50(), 'fcn_resnet50')
    tput(models.segmentation.fcn_resnet101(), 'fcn_resnet101')
    tput(models.segmentation.deeplabv3_resnet50(), 'deeplabv3_resnet50')
    tput(models.segmentation.deeplabv3_mobilenet_v3_large(), 'deeplabv3_mobilenet_v3_large')
    tput(models.segmentation.lraspp_mobilenet_v3_large(), 'lraspp_mobilenet_v3_large')
