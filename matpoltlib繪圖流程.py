import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 50)
y = np.sin(2*np.pi*x)
fig = plt.figure()
sp = fig.add_subplot(111)
sp.plot(x, y, 'b--')
plt.savefig('myplot.png')
plt.show()
# b=>藍色 --=>虛線

