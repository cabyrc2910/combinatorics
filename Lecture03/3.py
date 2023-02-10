# Расчёт медианы в Python
import array
import numpy as np

z = np.array([100,80,75,77,89,33,45,25,65,17,30,24,57,55,70,75,65,84,90,150])
print(z) # array([100,80,75,77,89,33,45,25,65,17,30,24,57,55,70,75,65,84,90,150])

print(z.shape)  # (20,)

z.sort()
print(z) # array([17,24,25,30,33,45,55,57,65,70,75,75,77,80,84,89,90,100,150])

print((z[9] + z[10])/2)  # 67.5
