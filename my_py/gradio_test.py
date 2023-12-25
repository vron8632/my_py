# -*- coding:utf-8 -*-
# Peoject：004_MyScripts
# File：gradio_test
# User：csu.pan-||
# Time：2023/4/4 9:28
# IDE: PyCharm
# Func: 用户自定义

import gradio as gr
import numpy as np

# 创建一个函数实现功能
def hello(greeting, name):
    return greeting + ", " + name + "!"

# 创建输入和输出
inputs = [
    gr.inputs.Textbox(label="Greeting"),
    gr.inputs.Textbox(label="Name")
]

outputs = gr.outputs.Textbox(label="Output")

# 创建 Gradio 接口
title = "My Example Interface"
description = "This is an example of the Gradio interface."

gr.Interface(
    fn=hello,
    inputs=inputs,
    outputs=outputs,
    title=title,
    description=description,
    ).launch(share=True)