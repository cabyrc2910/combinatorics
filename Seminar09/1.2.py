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


x2= np.array([30,30,40, 40, 20, 20, 50, 50])
y2= np.array([37, 47, 50, 60, 25, 35, 62, 72])

print(np.corrcoef(x2,y2)) # [[1.         0.94058229]
                          #  [0.94058229 1.        ]]
                          
b1 = (np.mean(x2*y2) - np.mean(x2)* np.mean(y2))/(np.mean(x2**2) - np.mean(x2)**2)
print(b1)                   # 1.24

b0 = np.mean(y2) - b1*np.mean(x2)
print(b0)                   # 5.100000000000001

plt.scatter(x2 ,y2)
print(plt.plot(x2 , b0 + b1 * x2))
plt.title('My grapf')
plt.xlabel('Площадь квартиры')
plt.ylabel('Цена квартиры')
print(plt.show())

model = LinearRegression()
x2 = x2 .reshape(-1,1)
print(x2 )  #  [[30]
            #  [30]
            #  [40]
            #  [40]
            #  [20]
            #  [20]
            #  [50]
            #  [50]]
            
regres = model.fit(x2 ,y2)
print(regres.intercept_)  # 5.1000000000000085
print(regres.coef_)       # [1.24]


