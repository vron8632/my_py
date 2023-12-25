# ---------------------------------------------------------------
# Copyright (c) 2022 BIT-DA, Mingjia Li. All rights reserved.
# Licensed under the Apache License, Version 2.0
# ---------------------------------------------------------------

import warnings

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical

from ..builder import LOSSES
from .cross_entropy_loss import CrossEntropyLoss
from .utils import get_class_weight, weight_reduce_loss


@LOSSES.register_module()
class EntropyConstraintLoss(CrossEntropyLoss):
    """CrossEntropyLoss after Logit Norm.

    Args:
        use_sigmoid (bool, optional): Whether the prediction uses sigmoid
            of softmax. Defaults to False.
        use_mask (bool, optional): Whether to use mask cross entropy loss.
            Defaults to False.
        reduction (str, optional): . Defaults to 'mean'.
            Options are "none", "mean" and "sum".
        class_weight (list[float] | str, optional): Weight of each class. If in
            str format, read them from a file. Defaults to None.
        loss_weight (float, optional): Weight of the loss. Defaults to 1.0.
        loss_name (str, optional): Name of the loss item. If you want this loss
            item to be included into the backward graph, `loss_` must be the
            prefix of the name. Defaults to 'loss_ce'.
        avg_non_ignore (bool): The flag decides to whether the loss is
            only averaged over non-ignored targets. Default: False.
            `New in version 0.23.0.`
    """

    def __init__(self,
                 use_sigmoid=False,
                 use_mask=False,
                 reduction='mean',
                 class_weight=None,
                 loss_weight=1.0,
                 loss_name='loss_lc',
                 avg_non_ignore=False,
                 eps=1e-7):
        super(EntropyConstraintLoss, self).__init__(use_sigmoid,
                                                  use_mask,
                                                  reduction,
                                                  class_weight,
                                                  loss_weight,
                                                  loss_name,
                                                  avg_non_ignore)
        self.eps = eps

    def forward(self,
                cls_score,
                label,
                weight=None,
                avg_factor=None,
                reduction_override=None,
                ignore_index=-100,
                **kwargs):
        """Forward function."""  # 把某点的所有通道上平方和相加再开方，得到L2范数 (2,1,512,512)
        norms = torch.norm(cls_score, p=2, dim=1, keepdim=True) + self.eps
        normed_logit = torch.div(cls_score, norms)  # (2,19,512,512)对应公式(8),输出的概率都除以一个所有类的L2范数，起到控制输出的效果

        cls_softmax = torch.softmax(cls_score, dim=1)           # (2,19,512,512)
        matrix = cls_softmax.permute(0, 2, 3, 1)                # (2,512,512,19)
        matrix = matrix.contiguous().view(-1, matrix.size(3))   # (2*512*512,19)
        dist = Categorical(probs=matrix)                        # (2*512*512,19)
        entropy = dist.entropy()                                # (2*512*512,)
        entropy = entropy.contiguous().view(cls_score.size(0),cls_score.size(2),cls_score.size(3))
        entropy = (entropy - 1) * (entropy - 1)
        if weight is not None:
            weight = weight * (1 + 0.001 * entropy)
        loss_cls = super(EntropyConstraintLoss, self).forward(normed_logit,
                                                            label,
                                                            weight,
                                                            avg_factor,
                                                            reduction_override,
                                                            ignore_index,
                                                            **kwargs)
        return loss_cls
