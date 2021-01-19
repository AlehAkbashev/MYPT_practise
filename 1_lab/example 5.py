import numpy as np
import matplotlib.pyplot as plt


plt.subplot(111, polar=True)
phi = np.arange(0, 2*np.pi, 0.01)
rho = phi
plt.plot(phi, rho, lw=4)
plt.show()

t = np.arange(0, 2*np.pi, 0.01)
r = 4
plt.plot(r*np.sin(t), r*np.cos(t), lw=5)
plt.axis('equal')
plt.show()
