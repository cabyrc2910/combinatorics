# На 8 уроке мы строили графики приведенных ниже данных.
# Для какого графика можно использовать модель линейной регрессии?

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = np.array([10,8, 13, 9,11,14, 6,4,12, 7,5])
y = np.array([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68 ])
x = np.array([ 10,8, 13, 9,11,14, 6,4,12, 7,5 ])
y2 = np.array([ 9.14, 8.14, 8.74,8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74])
x = np.array([ 10,8, 13, 9,11,14, 6,4,12, 7,5 ])
y3 = np.array([7.46,6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73])
x4 = np.array([8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8])
y4 = np.array([6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25,12.5, 5.56, 7.91, 6.89])
x0 = np.array([ 10, 8, 13, 9, 11, 14, 6, 4, 12, 7,5, 15, 16, 18 ])
y0 = np.array([ 9.14, 8.14, 8.74,8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74, 6.5, 5, 2.9])

plt.scatter(x,y)
print(plt.show())
print(np.corrcoef(x,y))  # [[1.         0.81642052]
                         #  [0.81642052 1.        ]]
plt.scatter(x,y2)
print(plt.show())
print(np.corrcoef(x,y2)) # [[1.         0.81623651]
                         #  [0.81623651 1.        ]]
plt.scatter(x,y3)
print(plt.show())
print(np.corrcoef(x,y3)) # [[1.         0.81628674]
                         #  [0.81628674 1.        ]]
                                         
plt.scatter(x4,y4)
print(plt.show())
print(np.corrcoef(x4,y4)) # [[1.         0.81652144]
                          #  [0.81652144 1.        ]]
                          
plt.scatter(x0,y0)
print(plt.show())
print(np.corrcoef(x0,y0)) # [[1.         0.02245218]
                          #  [0.02245218 1.        ]]

# Для 3 графика можно использовать модель линейной регрессии

b1 = (np.mean(x*y3) - np.mean(x)* np.mean(y3))/(np.mean(x**2) - np.mean(x)**2)
print(b1)                   # 0.4997272727272716

b0 = np.mean(y3) - b1*np.mean(x)
print(b0)                   # 3.0024545454545555

plt.scatter(x,y3)
print(plt.plot(x, b0 + b1 * x))
plt.title('My grapf')
plt.xlabel('Площадь квартиры')
plt.ylabel('Цена квартиры')
print(plt.show())


