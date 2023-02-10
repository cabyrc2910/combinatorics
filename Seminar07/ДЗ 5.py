# Заявляется, что партия изготавливается со средним арифметическим 2,5 см.
# Проверить данную гипотезу, если известно, что размеры изделий подчинены
# нормальному закону распределения. Объем выборки 10, уровень статистической
# значимости 5%
# 2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34

import numpy as np
import scipy.stats as stats


# Гипотеза 1:   H0 : M = 2,5
# Гипотеза 2:   H1 : M ≠ 2,5

alpha = 0.05 # 5%
a = np.array([2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34])
n = a.size # 10

mean = np.mean(a)  
print(mean)           # 2.5279999999999996

std = np.std(a, ddof=1)  
print(std )           # 0.1572542173961923

t_stat = (mean - 2.5) / (std / np.sqrt(n))  
print(t_stat)         # 0.5630613661802959

t_critical = stats.t.ppf(1 - alpha, n-1)
print(t_critical)     # 1.8331129326536333

# Если t-статистика меньше t-критического, то гипотеза не отвергается.  
# Если t-статистика больше t-критического, то гипотеза отвергается.

if t_stat < t_critical:
    print(f't_stat = {t_stat:.3f}',f't_critical = {t_critical:.3f}',f't_stat  < t_critical -> Гипотеза Н0 не отвергается',sep='\n')
else:
    print(f't_stat = {t_stat:.3f}',f't_critical = {t_critical:.3f}',f't_stat  > t_critical -> Гипотеза Н0 отвергается',sep='\n')