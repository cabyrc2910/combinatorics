# Определить сочетания, размещения или перестановки используются для решения этой задачи. Сколькими способами можно выбрать из колоды, состоящей из 36 карт, 4 карты ?

from math import factorial
import numpy as np

def combinations (n, k):
    return np.math.factorial (n) // (np.math.factorial(k) * np.math.factorial(n - k))
P = combinations (36, 4)   # 58905
print(f'P = (Из колоды, состоящей из 36 карт, 4 карты можно выбрать) = {(P)} раз')