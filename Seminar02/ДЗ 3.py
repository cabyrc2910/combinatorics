# Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?

from math import factorial

def bernulli(n, k, p): # вычисляем по формуле Бернулли 
    comb=factorial(n)/(factorial(k)*factorial(n-k))
    return comb*(p**k)*(1-p)**(n-k)

print(f'Вероятность что орёл выпадет ровно 70 раз: P = {bernulli(144,70,0.5):.3f}') # n=144, k=70, p=0.5
#  P = 0.063