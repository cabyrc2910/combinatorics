# Даны заработные платы юристов, программистов и бухгалтеров. Определить, влияет ли профессия на заработную плату. 

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

y1 = np.array([70, 50, 65, 60 ,75, 67, 74])
y2 = np.array([80, 74, 90, 70, 75, 65, 85])
y3 = np.array([148, 142, 140, 150, 160, 170, 155])

k = 3
n = 21

y_mean_1 = np.mean(y1)
print(y_mean_1)   # 65.85714285714286

y_mean_2 = np.mean(y2)
print(y_mean_2)  #  77.0

y_mean_3 = np.mean(y3)
print(y_mean_3)  #  152.14285714285714

total = np.array([y1, y2, y3])
print(total)  #  [[ 70  50  65  60  75  67  74]
               #  [ 80  74  90  70  75  65  85]
               #  [148 142 140 150 160 170 155]]

y_mena_total = np.mean(total)
print(y_mena_total) # 98.33333333333333

# сумма квадратов отклонений наблюдений от общего группового

S_obh = np.sum((total - 98.33)**2) # отложим это значение
print(S_obh) # 32400.6669

# сумма квадратов отклонений средних групповых значений от общего среднего

S_f = np.sum((y_mean_1 - 98.33)**2)*7 + np.sum((y_mean_2 - 98.33)**2)*7 + np.sum((y_mean_3 - 98.33)**2)*7 
print(S_f)  # 30836.952614285707

#  Остаточная сумма кевадратов отклонений

S_ost = np.sum((y1 - y_mean_1)**2) + np.sum((y2 - y_mean_2)**2) +np.sum((y3 - y_mean_3)**2)
print(S_ost) #  1563.7142857142858

S_obh = S_f + S_ost
print(S_obh) # 32400.666899999993
 
D_f = S_f / (k - 1) # факторная дисперсия
print(D_f)  # 15418.476307142853

D_ost = S_ost /(n - k)  # остаточная дисперсия
print(D_ost)  # 86.87301587301587

F_n = D_f / D_ost
print(F_n)  # 177.48291747670376

f = stats.f_oneway(y1, y2, y3)
print(f) 
# F_onewayResult(statistic=177.48291613374704, pvalue=1.4204669001071745e-12)
# Вывод: профессия оказывает статистически значимый эффект на зарплату.

plt.scatter(y1, y2, y3)
print(plt.show())

from statsmodels.stats.multicomp import pairwise_tukeyhsd
import pandas as pd
df = pd.DataFrame({'score':[70, 50, 65, 60, 75, 67, 74,
                            80, 74, 90, 70, 75, 65, 85,
                            148, 142, 140, 150, 160, 170, 155],
                   'group': np.repeat(['accountant', 'lawyer', 'programmer'], repeats = 7)})
tukey = pairwise_tukeyhsd(endog = df['score'],
                          groups = df['group'],
                          alpha = 0.05)
print(tukey)
#     Multiple Comparison of Means - Tukey HSD, FWER=0.05     
# ============================================================
#   group1     group2   meandiff p-adj   lower   upper  reject
# ------------------------------------------------------------
# accountant     lawyer  11.1429 0.0918 -1.5722 23.8579  False
# accountant programmer  86.2857    0.0 73.5707 99.0007   True
#     lawyer programmer  75.1429    0.0 62.4278 87.8579   True
# ------------------------------------------------------------
