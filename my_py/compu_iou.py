# -*- coding:utf-8 -*-
# 开发人员 : csu·pan-_-||
# 开发时间 : 2023/8/23 6:40
# 文件名称 : compu_iou.py
# 开发工具 : PyCharm
# 功能描述 : 自己修改

iou = '98.7 88.4 89.9 66.3 65.2 62.7 59.1 79.6 92.2 72.4 92.3 80.0 66.0 94.6 79.9 85.9 78.8 64.0 80.6'
iou_list = iou.split(' ')
list_int = [float(i) for i in iou_list]
print(sum(list_int)/len(list_int))

# 定义一个字符串
string = 'Entropy balance strategy for domain adaptive semantic segmentation'
print('源字符串为：', string)

# 将字符串转换为大写形式
uppercase_string = string.upper()
print('字符串转换为大写：')
print(uppercase_string)
