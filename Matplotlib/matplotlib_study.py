# 导入库
from time import sleep

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
import os


def show_plt():
    # 生成数据
    x = np.arange(0, 6.28, 0.01)  # 生成 [0,6] step = 0.1

    sin_y = np.sin(x)
    plt.plot(x, sin_y,label='sin(x)',linestyle = ":")

    cos_y = np.cos(x)
    plt.plot(x, cos_y,label='cos(x)')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('sin(x) & cos(x)')


    plt.legend() # 显示 label
    plt.show()


def show_image(path):
    # 检查文件是否存在
    if not os.path.exists(path):
        print(f"文件不存在: {path}")
        return

    # 检查文件是否可读
    if not os.access(path, os.R_OK):
        print(f"文件不可读: {path}")
        return

    try:
        img = imread(path)
    except SyntaxError as e:
        print(f"读取图像时出错 - 确保提供的路径指向一个有效的PNG文件: {e}")
        return

    plt.imshow(img)
    plt.show()


if __name__ == '__main__':
    current_directory = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_directory, 'image', 'test-image.png')
    show_image(image_path)
