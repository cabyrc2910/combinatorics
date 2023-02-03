# Приведены данные из исследования Фреба и Уайта, посвящённые исследованию состояния лёгких. 
# Возьмём данные для группы люлдей , которые работали в накуренном помещении и для людей , выкуривающих небольшле число сиьтарет в день.
# Обьёмы выборок  одинаковые - по 200 человек. Для людей работающих в накуренном помещении средняя скорость средины выдоха составляет 
# 2,72, std = 0,71, а выкуривших небольшое число сигарет 2,63, std = 0,723. 
# Можно ли считать среднюю скорость одинаковой средней скоростью середингы выдоха одинаковой в обеих группах ?
import scipy.stats as stats
import numpy as np
x1 = 2.72
x2 = 2.63
S1 = 0.71
S2 = 0.73
n1 = 200
n2 = 200
a = 0.05
t = (x1 - x2)/(np.sqrt(S1**2/n1 + S2**2/n2))
print(t)  # 1.2498794541681988 = 1.24 расчётное значение, критическое 1,96 (по табл. a = 0.05)