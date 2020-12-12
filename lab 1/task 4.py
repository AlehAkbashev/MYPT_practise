import matplotlib.pyplot as plt
import numpy as np


x = np.arange(-10, 10.01, 0.01)
print('Введите функцию: ')
y = eval(input())

with plt.xkcd():
    plt.plot(x, y, label=r'$y = $')
    plt.legend(loc='best', fontsize=10)

plt.show()
