import matplotlib.pyplot as plt
import numpy as np


x = [1, 2, 3, 4, 5]
y = [0.99, 0.49, 0.33, 0.7, 0.15]
plt.errorbar(x, y, xerr=0.05, yerr=0.1)
plt.grid()
p = np.polyfit(x, y, 2)
print(p)
f_x = np.poly1d(p)
print(f_x)
t = np.arange(1, 5.01, 0.01)
y_p = np.polyval(p, t)
plt.plot(t, f_x(t))
plt.show()