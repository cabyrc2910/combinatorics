# Утверждается , что средний рост мужчин национальности Х 179,5. 
# Была взята выборка  из 100 человек, по которой получилось среднее арифметическое 178,5 
# Проверить это утверждение с помощью одностороннего теста, если известло, что стандартное отклонение генеральной совокупности 3 см. 
# А уровень статистической значимости принять за 1 %
import scipy.stats as stats
import numpy as np

μ = 179.5 
X = 178.5 
A = 0.05
Σ = 0.03
n = 100
Z = ( X - μ) / (Σ /np.sqrt(n))
print(Z)