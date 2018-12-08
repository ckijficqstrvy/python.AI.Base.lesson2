import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 13)
y = np.random.randint(10, 100, 12)
fig, ax = plt.subplots(2, 2)
ax[0, 0].plot(x, y, 'r-o')
ax[0, 1].scatter(x, y, color='pink')
ax[1, 0].bar(x, y, color='k')
ax[1, 1].hist(y, facecolor='orange')
plt.show()
