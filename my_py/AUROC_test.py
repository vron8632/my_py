# -*- coding:utf-8 -*-
# Peoject：004_MyScripts
# File：AUROC_test
# User：csu.pan-||
# Time：2023/6/15 10:46
# IDE: PyCharm
# Func: AUROC的测试

# 导入sklearn算法库中的包
from sklearn.metrics import roc_curve, auc

def AUC(label, pre):
    # 计算正样本和负样本的索引，以便索引出之后的概率值
    pos = [i for i in range(len(label)) if label[i] == 1]   #正样本索引
    neg = [i for i in range(len(label)) if label[i] == 0]   #负样本索引
    auc = 0
    for i in pos:
        for j in neg:
            if pre[i] > pre[j]:
                auc += 1
            elif pre[i] == pre[j]:
                auc += 0.5

    return auc / (len(pos) * len(neg))


if __name__ == '__main__':
    label = [1, 0, 0, 0, 1, 0, 1, 0]
    pre = [0.55, 0.8, 0.3, 0.1, 0.4, 0.9, 0.66, 0.7]
    print('func: ', AUC(label, pre))

    '''
    label是列表形式，对应方法1中的label形式
    pre是列表形式，对应方法1中的pre形式
    '''
    fpr, tpr, th = roc_curve(label, pre, pos_label=1)
    print('sklearn: ', auc(fpr, tpr))


