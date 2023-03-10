# При исследовании препарата для снижения кровяного давления у больных 3 раза измерялся
# сердечный выброс. Менялся ли сердечный выброс ?
# Найти критерий вручную, проверьте значение функцией и интерпретируйте результат с
# использованием p-value

import numpy as np
import scipy.stats as stats

A = np.array([3.5, 3.3, 4.9, 3.6])
B = np.array([8.6, 5.4, 8.8, 5.6])
C = np.array([5.1, 8.6, 7.7, 5.0])
print(stats.friedmanchisquare(A, B, C))   #FriedmanchisquareResult(statistic=6.5, pvalue=0.03877420783172202)

n = 4     # кол-во больных
k = 3      # кол-во измерений
R = (n*(k+1))/2   # 8.0
print(R)

#                Измерения
# Больной   1-е  ранг  2-е  ранг   3-е  ранг
# 1         3,5   1    8,6   3     5,1   2
# 2         3,3   1    5.4   2     8,6   3
# 3         4,9   1    8,8   2     6,7   2
# 4         3,6   1    5,6   3     5,0   2
# сумма рангов    4          11          9

Ri1 = 4    # Cумма рангов 1 измерения
Ri2 = 11   # Cумма рангов 2 измерения
Ri3 = 9    # Cумма рангов 3 измерения
Xr = (12/(n*k*(k+1)))*((Ri1-R)**2+(Ri2-R)**2+(Ri3-R)**2)
print(Xr)  # 6.5