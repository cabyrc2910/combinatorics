#Задание 1
# Из колоды в 52 карты извлекаются случайным образом 4 карты крести. 
# a) Найти вероятность того, что все карты – крести. 
from math import factorial
c4_13 = factorial(13)/(factorial(4)*factorial(13-4))
c0_39 = factorial(39)/(factorial(0)*factorial(39-0))
c4_52 = factorial(52)/(factorial(4)*factorial(52-4))
p = c4_13 * c0_39 / c4_52

print(f'c4_13={c4_13}')     # 715.0
print(f'c0_39={c0_39}')     # 1.0
print(f'c4_52={c4_52}')     # 270725.0
print(f'Вероятность вытащить 4 карты крести = {round(p*100,2)} %')   # 0.26 %

# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.
c4_48 = factorial(48)/(factorial(4)*factorial(48-4))
c4_52 = factorial(52)/(factorial(4)*factorial(52-4))
p = c4_48 / c4_52
p = 1 - p

print(f"c4_48={c4_48}")      # 194580.0
print(f"c4_52={c4_52}")      # 270725.0
print(f'Вероятность вытащить туза = {round(p*100,2)} %')   # 28.13 %