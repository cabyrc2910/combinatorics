# Провести двусторонний тест и ответить на вопрос, есть ли статистически значимые
# различия между средними 2х нормально распределенных генеральных совокупностей,
# представленных следующими независимыми выборками:

# Уровень статистической значимости принять за 5%
# 1 . Используйте функцию в Python:
# 2. Имея p-value из функции рассчитать наблюдаемое значение критерия.

import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

a = np.array([12, 10, 11, 19, 13, 11, 17, 15, 19, 14, 21, 18, 21, 11, 17, 14, 15, 17, 20, 19])
b = np.array([11, 13, 18, 15, 17, 18, 10, 21, 26, 15, 11, 12, 15, 17, 10, 18, 18, 12,21, 20])

s1 = np.std(a, ddof=1)
print(s1)      # 3.5850567051229985
s2 = np.std(b, ddof=1)
print(s2)      # 4.290748922483052
print(len(a))  # 20
print(len(b))  # 20
print(np.sqrt(s1**2/20+s2**2/20))   # 1.250263130199736
print((np.mean(a) - np.mean(b))/1.250263130199736)  #-0.1599663264228627
print(stats.ttest_ind(a, b, equal_var=True))  
# Ttest_indResult(statistic=-0.1599663264228627, pvalue=0.8737549039369696)
print(stats.t.ppf(1-0.8737549039369696/2, 38))  # 0.15996632632476554
plt.scatter(a,b)
print(plt.show())
print(np.corrcoef(a,b))  # [[1.         0.01847613]
                         #  [0.01847613 1.        ]]
print(stats.ttest_ind(a, b,alternative='greater', equal_var = True))
# Ttest_indResult(statistic=-0.1599663264228627, pvalue=0.5631225480315152)
print(stats.ttest_ind(a, b,alternative='less', equal_var = True))
# Ttest_indResult(statistic=-0.1599663264228627, pvalue=0.4368774519684848)
print(np.mean(a))  # 15.7
print(np.mean(b))  # 15.9


