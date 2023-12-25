# -*- coding:utf-8 -*-
# 开发人员 : csu·pan-_-||
# 开发时间 : 2023/8/3 8:11
# 文件名称 : diffusers_01.py
# 开发工具 : PyCharm
# 功能描述 : 使用dreambooth生成一张图片

import numpy as np
import torch
import torch.nn.functional as F
import torchvision.utils
from matplotlib import pyplot as plt
from PIL import Image
from diffusers import StableDiffusionPipeline
from diffusers import DDPMPipeline

# 第一个创建时需要访问令牌
# from huggingface_hub import login
# login('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')
# add_to_git_credential=True

def show_images(x):
    """给定一批图像，创建一个网格并将其转换为PIL"""
    x = x * 0.5 + 0.5     #将(-1,1)区间映射回(0,1)区间
    grid = torchvision.utils.make_grid(x)
    grid_im = grid.detach().cpu().permute(1, 2, 0).clip(0, 1) * 255
    grid_im = Image.fromarray(np.array(grid_im).astype(np.uint8))
    return grid_im


def make_grid(images, size=64):
    """给定一个PIL图像列表，将它们叠成一行以便查看"""
    output_im = Image.new('RGB', (size * len(images), size))
    for i, im in enumerate(images):
        output_im.paste(im.resize((size, size)), (i * size, 0))
    return output_im

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# # https://huggingface.co/sd-dreambooth-library  这里有来自社区的各种模型
# model_id = 'sd-dreambooth-library/toby'
#
# # 加载管线
# pipe = StableDiffusionPipeline.from_pretrained(model_id,torch_dtype=torch.float16).to(device)
#
# promt = 'Lying dog'
# # guidance_scale决定模型输出与prompt的匹配程度
# image = pipe(promt,num_inference_steps = 20, guidance_scale = 5.5)
# image1 = image.images[0]
# image1.save('output.jpg')

# 加载预设好的管线
butterfly_pipeline = DDPMPipeline.from_pretrained('johnowhitaker/ddpm-butterflies-32px').to(device)

# 生成8张图片
images = butterfly_pipeline(batch_size = 2).images

# 输出图片
new_im = make_grid(images)
new_im.save('output.jpg')
