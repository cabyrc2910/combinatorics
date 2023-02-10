import numpy as np
from sklearn.linear_model import LinearRegression

s = np.array([27, 37, 42, 48, 57, 56, 77, 80])
p = np.array([1.2, 1.6, 1.8, 1.8, 2.5, 2.6, 3, 3.3])
n = 8

model = LinearRegression() #  зададим модель линейной ригрессии

# делаем массив s  двумерным атрибутом  reshape(-1,1)
s = s.reshape(-1,1)
print(s) #[[27]
        #  [37]
        #  [42]
        #  [48]
        #  [57]
        #  [56]
        #  [77]
        #  [80]]
regres = model.fit(s,p) #  подбираем коэффиценты  
print(regres.intercept_) #  выводим интерсептор  0.1714700996677747
print(regres.coef_)  #  выводим коэффицент  [0.03874585]

# Функция predict()
y_pred = model.predict(s) #  подставим площадь в модель и подсчитаем предиктовые значения цены квартиры
print(y_pred)
# [1.21760797 1.60506645 1.79879568 2.03127076 2.37998339 2.34123754 3.15490033 3.27113787]

import matplotlib.pyplot as plt
plt.scatter(s,p)
print(plt.show())

import pandas as pd
df = pd.DataFrame ({'реальные': p, 'предсказанные':y_pred})
print(df)
            #    реальные  предсказанные
            # 0       1.2       1.217608
            # 1       1.6       1.605066
            # 2       1.8       1.798796
            # 3       1.8       2.031271
            # 4       2.5       2.379983
            # 5       2.6       2.341238
            # 6       3.0       3.154900
            # 7       3.3       3.271138

# Коэффицент детерминации
# r = np.corrcoef(s,p)[1,0]
# r              # 0.9785768205829909
# print(r**2)    # 0.95761259937823151

# или получим из математической модели
print(regres.score(s,p))  # 0.957612593782315

### Критерий Фишера. F= MSF / MSO
# MSF - Фактическая сумма квадратнвых отклонений на одну степень свободы
# MSF= SSF/df2

# df1 - степень свободы числителя df1 = p - 1, где p число параметров
# df2 - степень свободы знаменателя df2 = n - p, где n - число парных измерений

# SSF - фактическая сумма квадратных отклонений
# SSO - остаточная сумма квадратных отклонений

df1 = 2-1
df2 = 8-2
SSf = sum((y_pred - np.mean(p))**2)  # 3.614987541528235
print(SSf)

SSo = np.sum((p - y_pred)**2)        # 0.16001245847176088
print(SSo)

Msf = SSf/df1   # 3.614987541528235
print(Msf)

Mso = SSo/df2   # 0.02666874307862681
print(Mso)

F = Msf/Mso     # 135.55147803067638
print(F)

import scipy.stats as stats
### Оценка значимости математической модели. Критерий Фишера.

a = 0.05
df = n-2
print(stats.f.ppf(1-0.05, 1, df))  # 5.987377607273699
print(stats.t.ppf(1-0.025, df))   # 2.4469118487916806


### Оценка значимости стдельных коэффицентовю. Критерий Стьюдента
b0 = 0.17147009966776983
b1 = 0.03874584717607981

# sb и s0 - стандартные ошибки коэхффицентов
s0 = np.sqrt((Mso * np.sum(s**2))/(n * sum((s - np.mean(s))**2)))  
print(s0)   # 0.18558943

sb = np.sqrt(Mso/np.sum((s - np.mean(s))**2))  
print(sb)   # 0.0033279211856704766

t0 = b0/s0 #   Критерий Стьюдента для коэффицента b0
print(t0)   # 0.92392171

tb = b1 /sb #  Критерий Стьюдента для коэффицента b1
print(tb)   # 11.642657687601963

 
