import matplotlib.pyplot as plt
import numpy as np

# 放物線の方程式: y = ax^2 + bx + c
def parabola(x, a, b, c):
    return a * x**2 + b * x + c

# 放物線のパラメータ
a = -1  # 二次項の係数
b = 0  # 一次項の係数
c = 0  # 定数項

# xの範囲を指定
x_values = np.linspace(-10, 10, 100)

# 対応するy値を計算
y_values = parabola(x_values, a, b, c)

# プロット
plt.plot(x_values, y_values, label='Parabola')
plt.title('Parabolic Trajectory')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()