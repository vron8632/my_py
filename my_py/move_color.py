# -*- coding:utf-8 -*-
# Peoject：004_MyScripts
# File：move_color
# User：csu.pan-||
# Time：2023/7/13 10:29
# IDE: PyCharm
# Func: 将cityscapes里所有的gt_color文件移动到一个文件夹里

import os
import shutil

s_path = r'E:\Projects\000_datasets\cityscapes\gtFine\val'
d_path = r'E:\Projects\000_datasets\cityscapes\gtFine\color'

def move_color(path):
    files = os.listdir(path)
    for i, file in enumerate(files):
        if os.path.isdir(os.path.join(path, file)) :
            move_color(os.path.join(path, file))
        else:
            print('第 %d / 共 %d' % (i + 1, len(files)))
            if 'color' in file:
                shutil.copy(os.path.join(path, file), os.path.join(d_path, file))

if __name__ == '__main__':
    move_color(s_path)