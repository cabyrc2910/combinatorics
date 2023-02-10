import array
import numpy as np

np.random.seed(1)
n = 60
b = np.random.randint (1, 7, n)
print(f'b = array ({b})')
a = b [b == 3]
print(f'a = array ({a})') 
m = len (a)
print(f'm = {m}') # 6
# Теперь можем вычислить относительную частоту события А
W = m/n
print(f'W = {W}') # 0,1