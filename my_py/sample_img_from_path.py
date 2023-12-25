# -*- coding:utf-8 -*-
# 开发人员 : csu·pan-_-||
# 开发时间 : 2023/9/14 9:04
# 文件名称 : sample_img_from_path.py
# 开发工具 : PyCharm
# 功能描述 : 采样图片

"""有个文件夹里有87个子文件夹，每个子文件夹里有250张图片，
从中采样出5张图片，包括第1张和最后一张，以及中间的均匀分布。
将这些采样的图片复制进另外一个文件夹。"""

import os
import shutil
import random

source_folder = r"E:\Projects\000_datasets\remote_senseing\air-ground\Images"  # 源文件夹路径
destination_folder = r"E:\Projects\000_datasets\remote_senseing\air-ground\sample"  # 目标文件夹路径
output_name_prefix = "sampled_image_"  # 新文件名前缀

subfolders = os.listdir(source_folder)

image_counter = 1  # 用于生成新文件名的计数器

for subfolder in subfolders:
    subfolder_path = os.path.join(source_folder, subfolder)
    if os.path.isdir(subfolder_path):
        image_files = os.listdir(subfolder_path)
        if len(image_files) > 2:
            sampled_images = [image_files[0], image_files[-1]]
            interval = len(image_files) // 3
            for i in range(1, 3):
                sample_index = i * interval
                sampled_images.append(image_files[sample_index])
            for image in sampled_images:
                source_path = os.path.join(subfolder_path, image)
                new_filename = output_name_prefix + str(image_counter) + '.jpg'  # 生成新的文件名
                image_counter += 1  # 更新计数器
                destination_path = os.path.join(destination_folder, new_filename)
                shutil.copy2(source_path, destination_path)