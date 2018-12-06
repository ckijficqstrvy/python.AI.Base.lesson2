import matplotlib.pyplot as plt
import numpy as np

'''
x = np.linspace(-1, 1, 50)
y = x**2
plt.figure()
plt.plot(x, y)
plt.show()
'''
'''
# 圖中圖
fig = plt.figure()
# [left, bottom, width, height]
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax2 = fig.add_axes([0.2, 0.2, 0.2, 0.4])
plt.show()
'''
'''
# sub圖
fig = plt.figure()
# (row, col<=?row*?col的網格, 第幾個位置number)
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)
plt.show()
'''
fig, ax = plt.subplots(nrows=2, ncols=1)
plt.show()