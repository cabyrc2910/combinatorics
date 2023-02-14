# # Постройте графики для приведенных наборов данных. Найдите коэффициенты для линии
# регрессии и коэффициенты детерминации. Что вы замечаете? Нанесите на график модель
# линейной регрессии.
# X1= np.array([30,30,40, 40])
# Y1= np.array([37, 47, 50, 60])
# x2= np.array([30,30,40, 40, 20, 20, 50, 50])
# y2= np.array([37, 47, 50, 60, 25, 35, 62, 72])
# X3 = np.array([30,30,40, 40, 20, 20, 50, 50, 10, 10, 60, 60])
# Y3 = np.array([37, 47, 50, 60, 25, 35, 62, 72, 13, 23, 74, 84])

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


X3 = np.array([30,30,40, 40, 20, 20, 50, 50, 10, 10, 60, 60])
Y3 = np.array([37, 47, 50, 60, 25, 35, 62, 72, 13, 23, 74, 84])

print(np.corrcoef(X3,Y3)) # [[1.        0.9725791]
                          #  [0.9725791 1.       ]]
                          
b1 = (np.mean(X3*Y3) - np.mean(X3)* np.mean(Y3))/(np.mean(X3**2) - np.mean(X3)**2)
print(b1)                   # 1.2257142857142853

b0 = np.mean(Y3) - b1*np.mean(X3)
print(b0)                   # 5.600000000000016 

plt.scatter(X3,Y3)
print(plt.plot(X3, b0 + b1 * X3))
plt.title('My grapf')
plt.xlabel('Площадь квартиры')
plt.ylabel('Цена квартиры')
print(plt.show())

model = LinearRegression()
X3 = X3.reshape(-1,1)
print(X3)   # [[30]
            #  [30]
            #  [40]
            #  [40]
            #  [20]
            #  [20]
            #  [50]
            #  [50]
            #  [10]
            #  [10]
            #  [60]
            #  [60]]
regres = model.fit(X3,Y3)
print(regres.intercept_)  # 5.600000000000016
print(regres.coef_)       # [1.22571429]


