import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-10, 10.01, 0.01)
t = np.arange(-10, 11, 1)

#subplot 1
sp = plt.subplot(221)
plt.plot(x, np.sin(x))
plt.title(r'$\ y =sin(x)$', verticalalignment='bottom')
plt.grid(True)

#subplot 2
sp = plt.subplot(222)
plt.plot(x, np.cos(x), 'g')
plt.grid(True)
plt.axis('equal')
plt.title(r'$\ y=cos(x)$')

#subplot 3
sp = plt.subplot(223)
plt.plot(x, x**2, t, t**2, 'v')
plt.title(r'$\ y=x^2$', loc='center', y=-0.3)

#subplot 4
sp = plt.subplot(224)
plt.plot(x, x)
sp.spines['left'].set_position('center')
sp.spines['bottom'].set_position('center')
plt.text(12, 0,'text')
sp.set_title('$y=x$', verticalalignment='top')

plt.show()