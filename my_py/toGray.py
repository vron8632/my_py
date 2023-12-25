# -*- coding:utf-8 -*-
# 开发人员 : csu·pan-_-||
# 开发时间 : 2023/12/7 10:10
# 文件名称 : toGray.py
# 开发工具 : PyCharm
# 功能描述 : 自己修改

from PIL import Image
import os

# 设置输入和输出文件夹路径
input_folder = r"E:\Projects\000_datasets\flowers\val"
output_folder =r"E:\Projects\000_datasets\flowers\gray"

# 获取输入文件夹中所有文件的路径
image_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith(".jpg")]

# 遍历每个文件，将其转换为灰度图像并保存到输出文件夹中
for i, image_file in enumerate(image_files):
    print('第 %d / 共 %d'%(i+1,len(image_files)))
    with Image.open(image_file) as img:
        gray_img = img.convert("L")
        gray_img_path = os.path.join(output_folder, os.path.basename(image_file))
        gray_img.save(gray_img_path)
