import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-10, 10.01, 0.01)
plt.figure(figsize=(10, 5))
first_line, = plt.plot(x, np.sin(x))
print(first_line)
second_line = plt.plot(x, np.cos(x))
print(second_line)
print(type(second_line))
plt.xlabel(r'$x$', fontsize=14)
plt.ylabel(r'$f(x)$', fontsize=25)
plt.axis('equal')
plt.grid(True)
print(type(first_line))
plt.legend((first_line, *second_line), ['lin1', 'lin2'])
plt.savefig('figure_with_legend.png')
plt.show()

