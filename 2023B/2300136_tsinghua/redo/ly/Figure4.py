import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib.colors as mcolors


# 字体设置（使用加载的本地字体）
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.size'] = 15
plt.rcParams['xtick.labelsize'] = 9
plt.rcParams['ytick.labelsize'] = 9


# 创建数据
data = {
    'Type': 12 * ['a'] + 12 * ['b'] + 12 * ['c'] + 12 * ['d'],
    'Month': list(range(1, 13)) * 4,
    'Level': [3, 3, 1, 0, 0, 0, 3, 3, 3, 3, 3, 3,
              3, 3, 3, 3, 0, 0, 3, 0, 3, 3, 3, 3,
              0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3,
              3, 0, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3,]
}

# 转换为DataFrame
df = pd.DataFrame(data)

# 创建透视表
pivot_table = df.pivot_table(values='Level', index='Month', columns='Type')
bounds = [0, 1, 2, 3, 4]
norm = mcolors.BoundaryNorm(bounds, ncolors=256)
# 绘制热图
plt.figure(figsize=(8, 6))
sns.heatmap(pivot_table, annot=True, cmap='Blues', norm=norm, cbar_kws={'label': 'level', 'ticks': [0, 1, 2, 3]})
plt.show()
