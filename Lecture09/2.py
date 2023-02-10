# Расчет коэффициентов по формулам

import numpy as np
import scipy.stats as stats

s = np.array([27, 37, 42, 48, 57, 56, 77, 80])   # площадь
p = np.array([1.2, 1.6, 1.8, 1.8, 2.5, 2.6, 3, 3.3]) #  прайс (Цена)
n = 8  

b1 = (n*np.sum(p*s)- np.sum(s)* np.sum(p))/(n*np.sum(s**2)- np.sum(s)**2)
print(b1)  # 0.03874584717607981

#  2 способ
b1 = (np.mean(s*p)- np.mean(s)* np.mean(p))/(np.mean(s**2)- np.mean(s)**2)
print(b1)  # 0.03874584717607981

b0 = np.mean(p) - b1*np.mean(s)
print(b0)  # 0.17147009966776983

y_pred = 0.17147009 + 0.03874585 * s    # предсказуемое прогнозируемое значение
print(y_pred)  # [1.21760804 1.60506654 1.79879579 2.03127089 2.37998354 2.34123769 3.15490054 3.27113809]