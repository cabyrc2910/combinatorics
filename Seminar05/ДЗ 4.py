# Задачу решать с помощью функции. Есть ли статистически значимые различия в росте дочерей и матерей?
# 4) Рост матерей 172, 177, 158, 170, 178,175, 164, 160, 169
# Рост взрослых дочерей: 173, 175, 162, 174, 175, 168, 155, 170, 160

import numpy
from scipy import stats

mothers = numpy.array([172, 177, 158, 170, 178, 175, 164, 160, 169, 165])
daughters = numpy.array([173, 175, 162, 174, 175, 168, 155, 170, 160, 163])

print(stats.ttest_rel(mothers, daughters)) #statistic=0.6648478531431979, pvalue=0.5228168632983574, df=9

print((mothers.mean() - daughters.mean()) / numpy.sqrt(
    mothers.var(ddof=1) / mothers.size
    + daughters.var(ddof=1) / daughters.size)
) # 0.41384114976800535

print('Так как p-value > α (0.05) статистически значимых различий в росте нет')
