# -*- coding:utf-8 -*-
# Peoject：004_MyScripts
# File：GramTest
# User：csu.pan-||
# Time：2023/7/7 7:35
# IDE: PyCharm
# Func: 计算Gram矩阵

import numpy as np
from skimage import data, img_as_float

# 加载一张灰度图像
# image = data.camera()
image = np.array([[100,120],[130,140]])
image2 = np.array([[8,6],[3,4]])

# 将图像转换为浮点数类型
image = img_as_float(image)

# 计算图像的均值和标准差
mean = np.mean(image)
std = np.std(image)

# 对图像进行归一化处理
normalized_image = (image - mean) / std

# 计算Gram矩阵
gram1 = np.dot(normalized_image.T, normalized_image)
gram2 = np.dot(image2.T, image2)  #[10 14
                                  # 14 20]
print(gram2)
