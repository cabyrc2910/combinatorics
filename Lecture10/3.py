# Двухфакторный дисперсионный анализ в Python

import statsmodels.api as sm
from statsmodels.formula.api import ols
import numpy as np
import pandas as pd

fA = np.array(["low", "low", "low", "low", "hight", "hight", "hight", "hight"])
print(fA) 

# array(["low", "low", "low", "low", "hight", "hight", "hight", "hight"],dtype = '<U4')

fB = np.array(["low", "low", "hight", "hight", "low", "low", "hight", "hight"])
print(fB)

# array(["low", "low", "low", "low", "hight", "hight", "hight", "hight"],dtype = '<U4')

values = np.array([57, 59, 56, 58, 32, 34, 71, 71])
print(values)
# array([57, 59, 56, 58, 32, 34, 71, 71])


df = pd.DataFrame({'fA': fA, 'fB' : fB, 'values' : values})
print(df)
#       fA     fB  values
# 0    low    low      57
# 1    low    low      59
# 2    low  hight      56
# 3    low  hight      58
# 4  hight    low      32
# 5  hight    low      34
# 6  hight  hight      71
# 7  hight  hight      71