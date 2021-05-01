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
        print('batchsize: 32')
        input = torch.rand(32,3,224,224).to('cuda')
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

if __name__ == '__main__':
    alexnet = models.alexnet()
    resnet18 = models.resnet18()
    resnet50 = models.resnet50()
    mobilenet_v2 = models.mobilenet_v2()
    vgg16 = models.vgg16()
    squeezenet = models.squeezenet1_0()
    tput(alexnet, 'alexnet')
    tput(resnet18, 'resnet18')
    tput(mobilenet_v2, 'mobilenet_v2')
    tput(resnet18, 'resnet50')
    tput(vgg16, 'vgg16')
    tput(squeezenet, 'squeezenet')