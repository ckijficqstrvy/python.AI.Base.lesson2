import numpy as np
import matplotlib.pyplot as plt
'''
# 直線圖
x = np.linspace(0, 1, 50)
y = np.sin(2*np.pi*x)
fig = plt.figure()

ax = fig.add_subplot(121)
ax.plot(x, y, 'r--')
# plt.show()


# 散點圖
ax2 = fig.add_subplot(122)
ax2.scatter(x, y, s=5, c='g')
plt.show()
'''
'''
# 長條圖
x = ['apple', 'banana', 'cherry', 'orange', 'pear']
y = [3, 5, 7, 9, 10]
fig = plt.figure()
ax = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
ax.barh(x, y, height=0.5)
ax2.bar(x, y, width=0.5)
plt.show()
'''
'''
# 直方圖
mydata = np.random.randint(1, 50, 200)
plt.hist(mydata, bins=100, facecolor='orange')
plt.show()
'''
'''
# 圓餅圖
labels = ['apple', 'banana', 'cherry', 'orange', 'pear']
values = [3, 5, 2, 6, 7]
ex = [0, 0.2, 0, 0, 0]
plt.axes(aspect=1)
plt.pie(values, labels=labels, shadow=1, autopct='%3.1f%%', explode=ex)
plt.show()
'''
'''
# 填充圖
x = np.arange(0., 2, 0.01)
y = np.sin(2*np.pi*x)
fig, ax = plt.subplots()
ax.fill_between(x, y, facecolors='yellow')
plt.show()
'''
# 混合子圖
x = ['apple', 'banana', 'cherry', 'orange', 'pear']
y = [3, 5, 2, 6, 7]
fig, axs = plt.subplots(2, 1, figsize=(5, 5))
axs[1].scatter(x, y)
axs[1].plot(x, y, 'r', alpha=0.3)  #這方法可以點跟現不同顏色
#axs[1].plot(x, y, 'r-o')  #這方法點跟線一樣顏色
plt.show()
