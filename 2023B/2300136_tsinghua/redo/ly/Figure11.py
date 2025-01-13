import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(18, 10))

for i in range(1, 7):
    ax = fig.add_subplot(2, 3, i, projection='3d')
    _x = np.arange(4)
    _y = np.arange(3)
    _xx, _yy = np.meshgrid(_x, _y)
    x, y = _xx.ravel(), _yy.ravel()

    top = np.random.randint(1, 10, size=len(x))
    bottom = np.zeros_like(top)
    width = depth = 1

    ax.bar3d(x, y, bottom, width, depth, top, shade=True, alpha=0.5)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.set_title(f'Graph {chr(96 + i)}')

plt.tight_layout()
plt.show()
