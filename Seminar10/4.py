# Даны веса пациентов до и после диеты. Веса распределены нормально
# До 92.8 , 95.6, 92.1, 100.6, 96.2, 92.1, 96.7, 97.6, 97.0, 93.9
# После 87.1, 84.1, 81.3, 77.0, 86.0, 82.9, 83.0, 85.5, 85.2, 84.6
# Проверить гипотезу о, том что средний вес пациентов после диеты статистически меньше веса до диеты
# 1) Используйте alternative='greater‘
# 2) alternative=‘less‘
# 3) 'two-sided'
# Объясните полученные результаты p-value для каждого случая

import numpy as np
import scipy.stats as stats

a = np.array([92.8 , 95.6, 92.1, 100.6, 96.2, 92.1, 96.7, 97.6, 97.0, 93.9])
b = np.array([87.1, 84.1, 81.3, 77.0, 86.0, 82.9, 83.0, 85.5, 85.2, 84.6])

print(stats.ttest_rel(a,b, alternative ='less'))  # меньше μ1>μ2
# TtestResult(statistic=7.972831441034037, pvalue=0.9999886277862766, df=9)

print(stats.ttest_rel(a,b, alternative ='greater'))  # больше  μ1<μ2
# TtestResult(statistic=7.972831441034037, pvalue=1.137221372340802e-05, df=9)

print(stats.ttest_rel(a,b, alternative ='two-sided'))  # μ1=μ2
# TtestResult(statistic=7.972831441034037, pvalue=2.274442744681604e-05, df=9)