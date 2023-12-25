# -*- coding:utf-8 -*-
# 开发人员 : csu·pan-_-||
# 开发时间 : 2023/8/3 10:22
# 文件名称 : diffusers_02_butterfly.py
# 开发工具 : PyCharm
# 功能描述 : 从头训练扩散模型，生成美丽的蝴蝶图片

import torchvision
from datasets import load_dataset
from torchvision import transforms

dataset = load_dataset('huggan/smithsonian_butterflies_subset',split='train')
# 也可以从本地文件夹中加载图像
# dataset = load_dataset('imagefolder',data_dir='path/to/folder')

# 32*32尺寸训练，也可以尝试更大的
image_size = 32
batch_size = 16

# 定义数据增强过程
preprocess = transforms.Compose([
    transforms.Resize(image_size,image_size),
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
    transforms.Normalize([0.5],[0.5])
])

def transform(examples):
    images = [preprocess(image.convert('RGB')) for image in examples['images']]
    return {'images':images}

dataset
