import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 2)
plt.figure()
plt.plot(x, 2*x)
plt.savefig('myplot2.png')
plt.show()

#plt.cla() clear an axis
#plt.clf() clear the entire figure
#plt.close() close a window