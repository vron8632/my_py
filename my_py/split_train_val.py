# -*- coding:utf-8 -*-
# Peoject：004_MyScripts
# File：split_train_val
# User：csu.pan-||
# Time：2023/7/13 11:11
# IDE: PyCharm
# Func: 将红外图像划分按比例划分到train和val中

import os
import random
import shutil

s_path = r'E:\Projects\000_datasets\remote_senseing\air-ground\sample'
train_path = r'E:\Projects\000_datasets\huipu\train\Infrared'
val_path = r'E:\Projects\000_datasets\huipu\val\Infrared'

def move_color(path):
    files = os.listdir(path)
    for i, file in enumerate(files):
        print('第 %d / 共 %d' % (i + 1, len(files)))
        prob = random.randint(1,100)
        if prob < 90:
            shutil.copy(os.path.join(path, file), os.path.join(train_path, file))
        else:
            shutil.copy(os.path.join(path, file), os.path.join(val_path, file))


if __name__ == '__main__':
    move_color(s_path)
