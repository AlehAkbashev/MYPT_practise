import matplotlib.pyplot as plt
import numpy as np


x = np.arange(-10, 10.02, 0.2)
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.plot(x, x**2 - x - 6)
plt.plot(x, 0*x)
plt.grid(True)
plt.show()
