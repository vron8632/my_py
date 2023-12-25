# -*- coding:utf-8 -*-
# 开发人员 : csu·pan-_-||
# 开发时间 : 2023/9/1 10:19
# 文件名称 : blend_01.py
# 开发工具 : PyCharm
# 功能描述 : photoshop里的一个功能， 左边图像的最右边80个像素使用渐变笔刷透明度逐渐增大，
           # 右边的图像和左边图像有80个像素的叠加区域，两个图像最终实现了无接缝拼接。

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# 打开图像并转换为 RGBA 模式
image = Image.open('right_image1.png').convert('RGBA')

# 将图像转换为 NumPy 数组
image_array = np.array(image)

# 获取图像的宽度和高度
width, height = image.size

# 获取右边80个像素的透明度值
alpha_values = image_array[0, 920:1000, 3]
# 读取文本文件并将值存入列表
data_list = []
with open('data.txt', 'r') as file:
    for line in file:
        value = float(line.strip())  # 假设文本文件每行包含一个浮点数
        data_list.append(value)

# 将列表转换为NumPy数组
data_array = np.array(data_list)

# 打印NumPy数组
print(data_array)
# 输出透明度值
print(alpha_values)

# 生成x轴坐标
x = np.arange(70)

# 绘制曲线
plt.plot(x, data_array)

# 显示网格线
plt.grid(True)

# 添加标题和坐标轴标签
plt.title('Curve Plot')
plt.xlabel('X')
plt.ylabel('Y')

# 显示图形
plt.show()


