# Нормальное распределение остатков
# Распределение остатков следует нормальному распределению.
# Методы проверки этого условия:
# QQ-plot
# Тест Шапиро-Уилка

import numpy as np
import scipy.stats as stats


# resid = p - y_pred
resid = np.array([-0.01760804, -0.00506654, 0.00120421, -0.23127089, 0.12001646, 0.25876231, -0.15490054, 0.02886191])
print(resid)

print(stats.shapiro(resid))
# ShapiroResult(statistic=0.9600725769996643, pvalue=0.8107908368110657)

 