import numpy as np
import matplotlib.pyplot as plt

s = np.array([27, 37, 42, 48, 57, 56, 77, 80])
print(s)

p = np.array([1.2, 1.6, 1.8, 1.8, 2.5, 2.6, 3, 3.3])
print(p)

plt.scatter(s, p)
print(plt.show)
print(np.corrcoef(p,s))   # [[1.         0.97857682]    коэф. корреляции
                           # [0.97857682 1.        ]]
                           
                           