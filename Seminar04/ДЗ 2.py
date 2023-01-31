# О случайной непрерывной равномерно распределенной величине B известно, что ее дисперсия равна 0.2.
# Можно ли найти правую границу величины B и ее среднее значение зная, что левая граница равна 0.5?
# Если да, найдите ее.

a = 0.5
d = 0.2
b = a+(d*12)**(1/2)
print(f'Правая граница распределения величины В = {b: .3f}\n'   # В =  2.049
      f'Среднее значение В на промежутке ({a}; {b: .3f}) M(B) = {(b+0.5)/2: .3f}')  # M(B) =  1.275