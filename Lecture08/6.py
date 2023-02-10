# Расчёт коэффицента корреляции Спирмена

import numpy as np
import scipy.stats as stats

p = np.array ([1.2, 1.6, 1.8, 1.8, 2.5, 2.6, 3. , 3.3])
print(p)

s = np.array ([27, 37, 42, 48, 57, 56, 77, 88])
print(s)

print(np.corrcoef(p,s))  # [[1.        0.9745776]
                         #  [0.9745776 1.       ]]
print(stats.spearmanr(p,s))
# SignificanceResult(statistic=0.9700772721497398, pvalue=6.548558831120599e-05)

