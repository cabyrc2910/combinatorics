# Проведите тест гипотезы. Продавец утверждает, что средний вес пачки печенья составляет 200 г.
# Из партии извлечена выборка из 10 пачек. Вес каждой пачки составляет:
# 202, 203, 199, 197, 195, 201, 200, 204, 194, 190.
# Известно, что их веса распределены нормально.
# Верно ли утверждение продавца, если учитывать, что доверительная вероятность равна 99%? (Провести двусторонний тест.)

#  Составим гипотезы:
#  H0 : М = 200 
#  H1 : М ≠ 200

import numpy as np

weights = np.array([202, 203, 199, 197, 195, 201, 200, 204, 194, 190])
n = 10

mean = weights.mean()   
std = weights.std(ddof=1)   
print(mean) #  среднее арифметическое = 198.5
print(std)  #  стандартное отклонение σ = 4.453463071962462

#  Поскольку мы проверяем гипотезу относительно математического ожидания нормально распределённой случайной величины с неизвестной дисперсией, будем использовать статистику:
#  t = (x-μ)/(σ/sqrt(n)) = (198.5-200.0)/(4.45/(10**0.5)) = -1.0659362899443976 = - 1.065

t = (mean-200)/(std/np.sqrt(n))  # (-1.0651074037450896)
print(t)     

# доверительная вероятность = 0.99
# Число степеней свободы  n - 1 = 9

# по таблице Стьюдента находим критическое
print('t1= 3.25') 
print('t2= −3.25')
# Ωα=(−∞,−3.25)∪(3.25,∞).

print('Вывод: значение  t  не попадает в критическую область, гипотеза верна')