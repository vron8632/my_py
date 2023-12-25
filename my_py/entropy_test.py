# coding:utf-8
# 当前的项目名称：004_MyScripts
# 编辑的文件名称：entropy_test
# 创建文件的用户：csu.pan-||
# 系统日期和时间：2023/3/219:03
# 创建IDE的名称: PyCharm

import torch
from torch.distributions import Categorical

tensor1 = torch.tensor([0.1,0.1,0.5,0.3])        # 1.1683    0.3109
tensor2 = torch.tensor([0.2,0.2,0.4,0.2])        # 1.3322    0.2639
tensor3 = torch.tensor([0.1,0.7,0.1,0.1])        # 0.9404    0.3905
tensor4 = torch.tensor([0.005,0.005,0.005,0.1,0.005,0.005,0.005,0.005,0.005,0.1,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.9])    # 0.5044  0.5044
tensor5 = torch.tensor([0.1,0.105,0.665,0.13])   # 1.0034    0.3366

dist = Categorical(probs=tensor4)                #
entropy = dist.entropy()                         #
print('entropy: ',entropy)

# entropy = torch.tensor(0.1)
entropy_exp = (entropy).exp()
print('entropy_exp: ',entropy_exp)

tensor6 = torch.randn((2,2,2))
tensor7 = torch.ones((2,2,2))

tensor8 = (tensor6 - 1) * (tensor6 - 1)

tensor9 =  torch.tensor([0.1,0.1,0.3,0.3])
tensor9 = torch.softmax(20*tensor9,dim=0)   # 1.3813 -> 1.2754 -> 1.0585 -> 0.7832  (1->5->10->20)
dist = Categorical(probs= tensor9)
entropy = dist.entropy()
print('entropy9: ',entropy)
