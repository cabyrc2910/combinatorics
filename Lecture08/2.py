import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, -1, 1, -2, 2, -3, 3, -4, 4])
print(x)   # [ 0 -1  1 -2  2 -3  3 -4  4]

y = x**2
print(y)   # [ 0  1  1  4  4  9  9 16 16]

print(np.corrcoef(x, y)) #[[1. 0.]
                         # [0. 1.]]

print(plt.scatter(x, y))
print(plt.show())