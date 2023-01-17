# Определить сочетания, размещения или перестановки используются для решения этой задачи. В магазине 20 покупателей. Сколькими способами 5 покупателей могут образовать очередь?
from math import factorial
import numpy as np
def arrangements (n, k):
    return np.math.factorial (n) // np.math.factorial (n - k)
P = arrangements (20, 5)  # n = 20, k = 5
print(f'P = (В магазине 20 покупателей, 5 покупателей могут образовать очередь) = {(P)} раз') # 1860480

def permutations (n):
    return np.math.factorial (n)
P = permutations ( 5 )  # находим как n!  или 5!
print(f'P = (В магазине 20 покупателей, 5 покупателей могут образовать очередь) = {(P)} раз') # 120
