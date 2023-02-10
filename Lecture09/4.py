#  Расчет коэффициентов методом градиентного спуска
import numpy as np
import scipy.stats as stats

x = np.array([27, 37, 42, 48, 57, 56, 77, 80])   # площадь
y = np.array([1.2, 1.6, 1.8, 1.8, 2.5, 2.6, 3, 3.3]) #  прайс (Цена)
 
def mse_(B1, y = y, x = x,n = 8):
    return np.sum((B1*x - y)**2)/n #  средняя квадратичной ошибки

alpha = 1e-6  # скорость обучения
# mse = 1/n *np.su,((B1*x - y)**2)
# mse = (2/n) *np.sum((B1*X - y)* X)

B1 = 0.1
n = 8 
for i in range(10):
    B1 -= alpha *(2/n) * np.sum ((B1*x-y)*x)
    print('B1 = {}'.format(B1))
    B1 = 0.09963717500000001
# B1 = 0.0992766067715
# B1 = 0.09891828127738128
# B1 = 0.09856218456783597
# B1 = 0.09820830277982404
# B1 = 0.09785662213653352
# B1 = 0.09750712894684428
# B1 = 0.09715980960479491
# B1 = 0.09681465058905309
# B1 = 0.09647163846238918
for i in range(3000):
    B1 -= alpha *(2/n) * np.sum ((B1*x-y)*x)
    if i % 500 == 0:
        print('Iteranion = {i}, B1 = {B1}, mse = {mse}'.format(i=i, B1=B1, mse=mse_(B1)))
# Iteranion = 0, B1 = 0.0992766067715, mse = 10.344162307912544
# Iteranion = 500, B1 = 0.044212570822721, mse = 0.04298386934659896
# Iteranion = 1000, B1 = 0.041780399509436315, mse = 0.022886502794653547
# Iteranion = 1500, B1 = 0.041672970818545076, mse = 0.022847293286272385
# Iteranion = 2000, B1 = 0.041668225707226836, mse = 0.022847216789406787
# Iteranion = 2500, B1 = 0.04166801611627644, mse = 0.022847216640163145

# а теп5ерь посчитаем mse через записанную ранее функцию и убедимся, что они одинаковы
print(mse_(0.041668))  # 0.022847216640000008  mse - функция потерь (мера измерения ошибок)
    
