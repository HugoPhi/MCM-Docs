import matplotlib.pyplot as plt
import numpy as np


# 字体设置（使用加载的本地字体）
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.size'] = 15
plt.rcParams['xtick.labelsize'] = 9
plt.rcParams['ytick.labelsize'] = 9


# 数据
categories = ['Wildlife', 'Human', 'Livestock']
wildlife_protection = [0.510774, 0.136791, 0.157609]
natural_resources_conservation = [0.247575, 0.100906, 0.28744]
local_financial_interest = [0.0631765, 0.351931, 0.118961]
animal_tourism_interactions = [0.178475, 0.410373, 0.43599]

data = [wildlife_protection, natural_resources_conservation, local_financial_interest, animal_tourism_interactions]
labels = ['Wildlife Protection', 'Natural Resources Conservation', 'Local Financial Interest', 'Animal Tourism Interactions']
sums = np.sum(data, axis=0)

# 初始化左侧位置
left_x = np.zeros(len(categories))

plt.figure(figsize=(10, 6))
# 绘制百分比横向柱状图
for section, label in zip(data, labels):
    x = section / sums
    plt.barh(categories, x, left=left_x, label=label)
    for i, (value, left) in enumerate(zip(x, left_x)):
        plt.text(left + value / 2, i, f'{value:.0%}', ha='center', va='center')
    left_x += x

# 设置标题和显示图形

plt.title('The weight of the four sections in different land types')
plt.xlabel('Weight')
plt.ylabel('Land type')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))  # 添加图例
plt.tight_layout()  # 自动调整子图参数，使之填充整个图像区域
plt.show()
