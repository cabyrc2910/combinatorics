import numpy as np
from scipy import stats

x = np.array([10.50,9.49,10.42,10.47,10.4,9.93,9.17,9.26,10.11,10.15,10.5,10.47])
print(np.mean(x)) # 10.0725

print(np.std(x,ddof=1)) # 0.5001113512372657

print(len(x)) # 12

t = (10.11-10)/(0.468/np.sqrt(12))
print(t) # 0.8142119180879295