# Сравнить значение ковариации одних и тех же случайных величин

import numpy as np

p = np.array([1.2, 1.6, 1.8, 1.8, 2.5, 2.6, 3. , 3.3])
print(p) 

s = np.array([27, 37, 42, 48, 57, 56, 77, 88])
print(s)

cov = np.mean(p*s) - np.mean(p) * np.mean(s)
print(cov)   # 11.662500000000023

print(np.cov(p,s)) # ([[0.53928571,  13.32857143],        ковариация
                    # [13.32857143, 344.      ]])
                    
print(np.corrcoef(p,s))   # ([[1.          0.97857682]     корреляция Пирсона
                         #   [0.97857682, 1.        ]])

