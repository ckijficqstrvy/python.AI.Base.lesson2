import numpy as np
import matplotlib.pyplot as plt

'''
# 顏色、深淺
x = np.linspace(-1, 1, 2)
plt.figure()
# color r=紅色 g=綠色 b=藍色 k=黑色 alpha=深淺(1以內)
plt.plot(x, 2*x, alpha=0.5, color='r')
plt.show()
'''
'''
# 散點圖
x = np.linspace(-1, 1, 5)
fig = plt.figure()
ax1 = fig.add_subplot(121) # <=產生一兩列的圖，位在位置1的子圖
ax2 = fig.add_subplot(122) # <=產生一兩列的圖，位在位置2的子圖
ax1.scatter(x, 2*x)
ax2.scatter(x, 2*x, marker='D')
plt.show()
'''
'''
# 直線圖
x = np.linspace(-1, 1, 5)
fig = plt.figure()
ax1 = fig.add_subplot(121) # <=產生一兩列的圖，位在位置1的子圖
ax2 = fig.add_subplot(122) # <=產生一兩列的圖，位在位置2的子圖
ax1.plot(x, 2*x)
ax2.plot(x, 2*x, linewidth='5', linestyle='--')
plt.show()
'''
'''
# 加圖例
x = np.linspace(-1, 1, 5)
fig = plt.figure()
plt.plot(x, 2*x, x, 2**x)
plt.legend(['First Line', 'Second Line'])
plt.show()
'''
# 加圖例2 不懂?
x = np.linspace(-1, 1, 5)
fig, ax = plt.subplots()
line, = ax.plot(x, x, lable='Inline Lable')
line.set_lable('First Line')
ax.legend()
plt.show()
