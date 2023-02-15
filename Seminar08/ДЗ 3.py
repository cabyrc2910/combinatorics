# Известно, что рост футболистов в сборной распределен нормальнос дисперсией генеральной совокупности,
# равной 25 кв.см. Объем выборки равен 27, среднее выборочное составляет 174.2. 
# Найдите доверительный интервал для математического ожидания с надежностью 0.95.

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# Для расчета доверительного интервала при извесной СКО будем использовать t-критерий и формулу для среднего арифмитического

var = 25
n = 27
mean = 174.2
std = (var)**0.5
alpha = 0.05
# z = stats.t.ppf(1-alpha/2,n-1)
z = stats.norm.ppf(1-alpha/2)  # известна дисперсия, значит известна сигма генеральной совокупности
d = z*std/(n)**0.5
min = mean - d          #  172.31
max = mean + d          #  176.09
print(f'Доверительный интервал для математического ожидания с надежностью 95% составляет:\n'f'min ={min: .2f}\n'f'max ={max: .2f}')