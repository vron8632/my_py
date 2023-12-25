# -*- coding:utf-8 -*-
# 开发人员 : csu·pan-_-||
# 开发时间 : 2023/8/31 9:09
# 文件名称 : ronghe.py
# 开发工具 : PyCharm
# 功能描述 : 使用opencv-python编程，对left图片的右边80个像素实施透明度渐变，并与right拼接

from PIL import Image
import numpy as np

# 读取左边的图片
left_image = Image.open('left.jpg').convert('RGBA')

# 读取右边的图片
right_image = Image.open('right.jpg').convert('RGBA')

# 读取右边的图片
right_image1 = Image.open('right_image1.png').convert('RGBA')

# 获取左边图片的尺寸
width, height = left_image.size

for y in range(height):
    for x in range(width-80, width):
        # 对左边图片的右边80个像素实施透明度渐变
        pixel_l = left_image.getpixel((x, y))
        alpha_l = int((1 - (x - (width - 80)) / 80) * 255)
        # alpha_l = alpha_values[x - (width-80)]
        new_pixel_l = (pixel_l[0], pixel_l[1], pixel_l[2], alpha_l)
        left_image.putpixel((x, y), new_pixel_l)

        # # 对右边图片的左边80个像素实施透明度渐变
        # pixel_r = right_image.getpixel((x - (width-80), y))
        # alpha_r = 255 - alpha_l
        # new_pixel_r = (pixel_r[0], pixel_r[1], pixel_r[2], alpha_r)
        # right_image.putpixel((x - (width-80), y), new_pixel_r)

# 创建一个空白的结果图像
result_width = width + right_image.width - 80
result_height = max(height, right_image.height)
result_image = Image.new('RGBA', (result_width, result_height))

# 创建一张全透明的背景图像，与待放置的图像尺寸相同
background = Image.new("RGBA", result_image.size, (0, 0, 0, 0))

# 将图像粘贴到背景图像上
background.paste(left_image, (0, 0), mask=left_image)

# 将左边图片与右边图片拼接
result_image.paste(right_image, (width - 80, 0))
# result_image.paste(left_image, (0, 0),mask=left_image)
# 使用 alpha_composite() 方法将前景图像叠加到目标图像上
composite_image = Image.alpha_composite(result_image, background)

result_image.save('right_image.png')
background.save('background.png')

# 保存叠加后的图像
composite_image.save('result.png')