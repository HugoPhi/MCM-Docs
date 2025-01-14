import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# 字体设置（使用加载的本地字体）
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.size'] = 15
plt.rcParams['xtick.labelsize'] = 9
plt.rcParams['ytick.labelsize'] = 9


# 定义线性模型函数
def linear_model(t, m, b):
    return m * t + b


# t 表示年份，
t = np.linspace(1, 40, 40)  # 时间点

actual_population = 200 + 10 * t + np.random.normal(0, 20, size=len(t))

# 使用 curve_fit 进行拟合
params, _ = curve_fit(linear_model, t, actual_population)
m, b = params


# 添加随机残差
np.random.seed(42)  # 固定随机种子，确保结果可重复
residuals = np.random.normal(0, 40, size=len(t))  # 正态分布的随机残差，标准差为20
actual_population = actual_population + residuals  # 加入残差后的实际种群数据

# 生成拟合曲线
fitted_population = linear_model(t, m, b)

# 绘制图像
plt.figure(figsize=(10, 6))
plt.scatter(t, actual_population, label='Livestock populations', color='black')
plt.plot(t, fitted_population, label='Lives', color='blue')
plt.fill_between(t, fitted_population, fitted_population + residuals, color='blue', alpha=0.2)
# plt.plot(t, actual_population, label='Random re', color='green', linestyle='dashed')
plt.title("Linear Fitting Curve of Livestock Populations")
plt.xlabel("Year")
plt.ylabel("Total number of Livestock Population(thousand)")
plt.legend()
plt.grid()
plt.show()
