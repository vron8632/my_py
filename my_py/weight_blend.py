# -*- coding:utf-8 -*-
# 开发人员 : csu·pan-_-||
# 开发时间 : 2023/9/5 8:37
# 文件名称 : weight_blend.py
# 开发工具 : PyCharm
# 功能描述 : 自己修改

import cv2
import numpy as np
def calWeight(d, k):
    '''
    :param d: 融合重叠部分直径
    :param k: 融合计算权重参数
    :return:
    '''

    x = np.arange(-d / 2, d / 2)
    y = 1 / (1 + np.exp(-k * x))
    return y


def imgFusion(img1, img2, overlap, left_right=True):
    '''
    图像加权融合
    :param img1:
    :param img2:
    :param overlap: 重合长度
    :param left_right: 是否是左右融合
    :return:
    '''
    # 这里先暂时考虑平行向融合
    w = calWeight(overlap, 0.05)  # k=0.05 这里是超参

    if left_right:  # 左右融合
        H, W = img1.shape
        img_new = np.zeros((H, 2 * W - overlap))
        img_new[:, :W] = img1
        w_expand = np.tile(w, (H, 1))  # 权重扩增
        img_new[:, W - overlap:W] = (1 - w_expand) * img1[:, W - overlap:W] + w_expand * img2[:, :overlap]
        img_new[:, W:] = img2[:, overlap:]
    else:  # 上下融合
        row, col = img1.shape
        img_new = np.zeros((2 * row - overlap, col))
        img_new[:row, :] = img1
        w = np.reshape(w, (overlap, 1))
        w_expand = np.tile(w, (1, col))
        img_new[row - overlap:row, :] = (1 - w_expand) * img1[row - overlap:row, :] + w_expand * img2[:overlap, :]
        img_new[row:, :] = img2[overlap:, :]
    return img_new

if __name__ =="__main__":
    img1 = cv2.imread("left.png",cv2.IMREAD_UNCHANGED)
    img2 = cv2.imread("right.png",cv2.IMREAD_UNCHANGED)
    img1 = (img1 - img1.min())/img1.ptp()
    img2 = (img2 - img2.min())/img2.ptp()
    img_new = imgFusion(img1,img2,overlap=80,left_right=True)
    img_new = np.uint16(img_new*65535)
    cv2.imwrite('weight_blend.png',img_new)
