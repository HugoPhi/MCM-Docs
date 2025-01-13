import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 定义指数模型函数
def exponential_model(t, A, B, C):
    return A * np.exp(-B * t + C)

# 模拟数据
# t 表示年份，actual_population 表示野生动物总数
t = np.linspace(1, 40, 40)  # 时间点
# 肉眼看的数据，不太准，用真实数据替换
actual_population = [212,415,349,265,165,135,264,210,202,225,237,389,150,215,210,173,112,198,124,146,148,140,105,70,136,130,75,72,69,64,60,56,53,50,48,47,46,45,44,42]

print(len(actual_population))
# 使用 scipy 的 curve_fit 函数进行拟合
params, _ = curve_fit(exponential_model, t, actual_population)
A, B, C = params

# 生成拟合曲线
fitted_population = exponential_model(t, A, B, C)
print(f'A = {A:.2f}, B = {B:.2f}, C = {C:.2f}')

# 计算总平方和（SST）
sst = np.sum((actual_population - np.mean(actual_population)) ** 2)

# 计算残差平方和（SSR）
ssr = np.sum((actual_population - fitted_population) ** 2)

# 计算R平方
r_squared = 1 - (ssr / sst)
print(f'R² = {r_squared:.4f}')

# 绘制图像
plt.figure(figsize=(10, 6))
plt.scatter(t, actual_population, label='Wildlife populations', color='black', alpha=0.6)
plt.plot(t, fitted_population, label='Exponential fit for wildlife populations', color='blue')
plt.title("Exponential Fitting Curve of Wildlife Populations")
plt.xlabel("Year")
plt.ylabel("Total Wildlife Populations(thousand)")
plt.text(30, 250, rf'$y={A:.2f}e^{{{B:.2f}(t+{C:.2f})}}$', fontdict=None)
plt.text(30, 230, rf'$R^2={r_squared:.4f}$', fontdict=None)
plt.legend()
plt.grid()
plt.show()