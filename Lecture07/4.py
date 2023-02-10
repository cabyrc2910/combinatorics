# У нас есть 5 пациентов и для каждого из них три измерения гемоглобина.  Для первого пациента  это значения 123, 126 и 141, следовательно, для 126 –наименьший ранг 1, а для 141 –наибольший ранг 3.

import numpy as np
import scipy.stats as stats

before = np.array([1223, 135, 119, 109, 145])
diet_1 = np.array([126, 144, 117, 156, 170])
diet_2 = np.array([141, 150, 164, 147, 169])

print(stats.friedmanchisquare(before, diet_1, diet_2))
# FriedmanchisquareResult(statistic=1.6000000000000014, pvalue=0.44932896411722134)