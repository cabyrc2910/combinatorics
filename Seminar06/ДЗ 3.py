# Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170
# Рост матерей 178, 165, 165, 173, 168, 155, 160, 164, 178, 175
# Используя эти данные построить 95% доверительный интервал для разности среднего роста родителей и детей.
# Интервальная оценка для разности средних арифметических расчитывается по формуле: 
# x1-x2 +- t(a/2)*(sqrt(s1**2/n1)+sqrt(s2**2/n2))
# x1 - среднее арифметическое в группе 1,   x2 - среднее арифметическое в группе 2
# s1**2 - дисперсия в группе 1,             s2**2 - дисперсия в группе 2
# n1 - число элементов в группе 1,          n2 - число элементов в группе 2

import numpy as np
import scipy.stats as stats

daughters = np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])
mothers = np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])

mean_difference = np.mean(mothers) - np.mean(daughters)  # среднее значение
std = np.sqrt((np.std(mothers) ** 2 / len(mothers)) + (np.std(daughters) ** 2 / len(daughters)))  #  стандартное отклонение
a = 1.96 * std
confidence_interval = (mean_difference - a, mean_difference + a)  # (-5.329451431471127, 9.12945143147114)

print("95% доверительный интервал разности среднего роста родителей и детей:", confidence_interval) 
