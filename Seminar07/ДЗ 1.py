# Даны две независимые выборки. Не соблюдается условие нормальности
# x1 380,420, 290
# y1 140,360,200,900
# Сделайте вывод по результатам, полученным с помощью функции


import numpy
from scipy import stats

x1 = numpy.array([380, 420, 290])
y1 = numpy.array([140, 360, 200, 900])
mannwhitneyu_py = stats.mannwhitneyu(x1, y1)

print('Критерий Манна-Уитни:',f'{mannwhitneyu_py}', sep='\n')  
# MannwhitneyuResult(statistic=8.0, pvalue=0.6285714285714286)
# Выбор в пользу нулевой гипотезы H0'