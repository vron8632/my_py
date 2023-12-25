# -*- coding:utf-8 -*-
# Peoject：004_MyScripts
# File：crop_color
# User：csu.pan-||
# Time：2023/7/13 10:46
# IDE: PyCharm
# Func: 将cityscapes的color图像裁剪成1365*1024

import os
import cv2

s_path = r'E:\Projects\000_datasets\cityscapes\gtFine\color'
d_path = r'E:\Projects\000_datasets\cityscapes\gtFine\color_crop'

def crop_color(path):
    files = os.listdir(path)
    for i, file in enumerate(files):
        print('第 %d / 共 %d' % (i + 1, len(files)))
        img = cv2.imread(os.path.join(path,file))
        img_new = img[0:840,250:250+1120]
        cv2.imwrite(os.path.join(d_path,file),img_new)

if __name__ == '__main__':
    crop_color(s_path)

