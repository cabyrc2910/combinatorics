# Приведеныдиаметры коронарных артерий после приёма нтфедепина и плацебо. 
# Позволяют ли проводимые ниже данные утверждать , что нифедепин влияет на диаметр коронарных артерий ?
# Выполнить расчёты  в Python
# Сделать расчёт в ручную
# Сравнить критерий Стьюдента и p_value  со значениями, полученными в Python

import scipy.stats as stats
import numpy as np

x = [2.5, 2.2, 2.6, 2, 2.1, 1.8, 2.4, 2.3, 2.7, 2.7, 1.9]
y = [2.5, 1.7, 1.5, 2.5, 1.4, 1.9, 2.3, 2.0, 2.6, 2.3, 2.2]

#################################################################
print(stats.ttest_ind(x,y))  
# statistic=1.3283484757831463, pvalue=0.19902265798859645

print((np.mean(x) - np.mean(y)) / np.sqrt (np.var(x, ddof=1) / len(x) + np.var(y, ddof=1) / len(y))) # 1.3283484757831465

#################################################################

d1 = np.var(x, ddof=1)  #  var(несмещённый)ddof=1 
print(d1)     # 0.10090909090909095
d2 = np.var(y, ddof=1)
print(d2)    # 0.17163636363636364
m1 = np.mean(x)
print(m1)    # 2.2909090909090906
m2 = np.mean(y)
print(m2)   # 2.0818181818181816
D = 0.5*(d1+d2)
print(D)    #  0.1362727272727273
print((m1-m2)/np.sqrt(2*D/len(x)))  # 1.3283484757831465