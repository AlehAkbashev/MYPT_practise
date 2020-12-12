import numpy as np

y = [1, 10, 1000]
for x in y:
    print(np.log(np.e**(1/(np.sin(x)+1))/(5/4+1/x**15))/np.log(1+x**2))
