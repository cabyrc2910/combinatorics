# # Постройте графики для приведенных наборов данных. Найдите коэффициенты для линии
# регрессии и коэффициенты детерминации. Что вы замечаете? Нанесите на график модель
# линейной регрессии.
# X1= np.array([30,30,40, 40])
# Y1= np.array([37, 47, 50, 60])
# x2= np.array([30,30,40, 40, 20, 20, 50, 50])
# y2= np.array([37, 47, 50, 60, 25, 35, 62, 72])
# X3 = np.array([30,30,40, 40, 20, 20, 50, 50, 10, 10, 60, 60])
# Y3 = np.array([37, 47, 50, 60, 25, 35, 62, 72, 13, 23, 74, 84])

import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X1= np.array([30,30,40, 40])
Y1= np.array([37, 47, 50, 60])

plt.scatter(X1,Y1)
print(plt.show())

print(np.corrcoef(X1,Y1)) # [[1.         0.79262399]
                          #  [0.79262399 1.        ]]
                          
b1 = (np.mean(X1*Y1) - np.mean(X1)* np.mean(Y1))/(np.mean(X1**2) - np.mean(X1)**2)
print(b1)                   # 1.3

b0 = np.mean(Y1) - b1*np.mean(X1)
print(b0)                   # 3.0

plt.scatter(X1,Y1)
print(plt.plot(X1, b0 + b1 * X1))
plt.title('My grapf')
plt.xlabel('Площадь квартиры')
plt.ylabel('Цена квартиры')
print(plt.show())                          
                                                 
model = LinearRegression()
X1 = X1.reshape(-1,1)
print(X1) # [[30]
         #  [30]
         #  [40]
         #  [40]]
regres = model.fit(X1,Y1)
print(regres.intercept_)  # 3.0 
print(regres.coef_)       # [1.3]


