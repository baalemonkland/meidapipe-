import matplotlib.pyplot as plt
import numpy as np

import matplotlib.path as mpath

def ifInHand(x_0,y_0,x_1,y_1,x_2,y_2,x_3,y_3,x_4,y_4,x_5,y_5,x,y):
    """函数返回一个布尔类型"""
    # 确定手掌路径(掌心为0，大拇指到小指分别为12345）,xy为目标点
    path = mpath.Path([(x_0,y_0), (x_1,y_1), (x_2,y_2), (x_3,y_3),(x_4,y_4), (x_5,y_5)])
    return (path.contains_point((x,y)))





# def ray_tracing(x_0, y_0, x_1, y_1):
#     # 计算射线的角度
#     angle = np.arctan2(y_1 - y_0, x_1 - x_0)
#     # 计算射线的长度
#     length = np.sqrt((y_1 - y_0) ** 2 + (x_1 - x_0) ** 2)
#     # 生成射线
#     x = np.linspace(x_0, x_0 + length * np.cos(angle), 100)
#     y = np.linspace(y_0, y_0 + length * np.sin(angle), 100)
#     return x, y
#
# # 起点坐标
# x_0, y_0 = 0, 0
# # 终点坐标
# x_1, y_1 = 10, 10
#
# # 计算射线
# x, y = ray_tracing(x_0, y_0, x_1, y_1)
#
# # 绘制图像
# plt.plot(x, y)
# plt.xlim(-10, 20)
# plt.ylim(-10, 20)
# plt.show()