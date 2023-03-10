# На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9. 
# Код содержит три цифры, которые нужно нажать одновременно. 
# Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?
from math import factorial

def combinations(n, k):
    return (factorial(n)/(factorial(k)*factorial(n-k)))

# общее количество исходов n = 3 из 10 , 
# количество благоприятных исходов (попыток) m = 1 

P=1/combinations(10,3) # 1/120 = 0.1846
print(f'P(Вероятность открыть с первой попытки) = {round(P*100,2)}%') # 0.83%