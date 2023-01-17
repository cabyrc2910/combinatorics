# Смоделируем ситуацию, когда бросают 2 игральные кости одновременно 360 раз. Посчитаем относительную частоту события, когда на олдной кости выпадает 1, а на другой 2

import array
import numpy as np
np.random.seed(1)
n = 360
c = np.random.randint (1, 7,size = n)
d = np.random.randint (1, 7,size = n)
print(f'c = array ({c})')
print(f'd = array ({d})')
a = c [(c == 1) & (d == 2)]
print(f'a = array ({a})')
m = len (a) # 12
print(f'm = {m}') 
W = m/n  # 0.03
print(f'W = {round(W,2)}') 