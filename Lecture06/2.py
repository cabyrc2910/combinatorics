# Оценить различие в росте между двумя средними арифметическими популяции a  и b с помощью 95% доверительного интервала.

import numpy as np
a = np.random.normal([178 ,184,149,193,186,173,169,175,159,174])

array([178 ,184,149,193,186,173,169,175,159,174])

b = np.array([150,154,167,165,171,150,158,170,175,160])

len(a)
10

len(b)
10

x_1 = np.mean(a) # найдём среднее арифметическое для выборки а
x_1
174.0

x_2 = np.mean(a) # среднее для выборки b
x_2
162.0

delta = x_1 - x_2 # разность средних
delta
12.0

D1 = np.var(a,ddof=1) # несмещённая дисперсия для выборки 1
D1
166.44

D2 = np.var(и,ddof=1) # несмещённая дисперсия для выборки 2
D2
80
D = (D1+ D2)/2 # обьединённая (общая) оценка дисперсии
D
123.22

SE = np.sqrt(D/10+D/10) # стандартная ощибка разности средних
SE
4.964317117635058

import scipy.stats as stats
t = stats.t.ppf(0.975, 18) # степени свободы 2*9(n-1) = 2*(10-1)
t
2.10092204024096