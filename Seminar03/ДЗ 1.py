# Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150. 
# Посчитать (желательно без использования статистических методов наподобие std, var, mean) 
# среднее арифметическое, 
# среднее квадратичное отклонение, 
# смещенную и несмещенную оценки дисперсий для данной выборки.

import numpy as np

arr=np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])

# среднее арифметическое
def mean_value(array):
    return sum(array)/len(array)

print(f'Среднее арифметическое М(Х) = {mean_value(arr):.2f}')   # 65.30

# среднее квадратичное отклонение выборки
def mean_square_deviation(array):
    square_dev=(array-mean_value(array))**2
    return (sum(square_dev)/len(square_dev))**(1/2)

print(f'Среднее квадратичное отклонение SD = {mean_square_deviation(arr):.3f}')   # 30.823

# смещенную и несмещённую оценку дисперсии 
def dispers(array, no_off=False):
#аргумент no_off отвечает за расчет смещенной, или несмещенной оценки дисперсии. По умолчанио расчитывается смещенная.
    square_dev=(array-mean_value(array))**2
    return sum(square_dev)/(len(square_dev)-1) if no_off else sum(square_dev)/len(square_dev)

print(f'Смещенная оценка дисперсии D = {dispers(arr):.3f}\n'         # 950.110
      f'Несмещенная оценка дисперсии D = {dispers(arr, True):.3f}')  # 1000.116