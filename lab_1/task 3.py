import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10.01, 0.01)
y = np.log((x**2+1)*np.exp(-np.abs(x)/10))/np.log(1+np.tan(1/(1+(np.sin(x))**2)))
plt.plot(x, y)
plt.xlabel(r'$XXX$')
plt.ylabel(r'$YYY$')
plt.grid(True)
plt.axis('equal')
plt.legend(['logo'])
plt.show()