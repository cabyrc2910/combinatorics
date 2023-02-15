# Произвести вычисления как в пункте 2, но с вычислением intercept.
# Учесть, что изменение коэффициентов должно производиться на каждом шаге одновременно 
# (то есть изменение одного коэффициента не должно влиять на изменение другого во время одной итерации).

import numpy
import matplotlib.pyplot as plt

zp = numpy.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = numpy.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
n = ks.size

b1 = (numpy.mean(zp * ks) - numpy.mean(zp) * numpy.mean(ks)) / (numpy.mean(zp**2) - numpy.mean(zp)**2)
# 2.620538882402765

b0 = numpy.mean(ks) - b1 * numpy.mean(zp)
# 444.1773573243596

alpha = 1e-6
 
for i in range(1000):
    y_pred3 = b0 + b1 * zp
    b0 -= alpha * (2 / n) * numpy.sum((y_pred3 - ks))
    b1 -= alpha * (2 / n) * numpy.sum((y_pred3 - ks) * zp)
    if i % 100 == 0:
        print('iteration = {i}, B1 = {b1}, mse = {mse}'.format(i=i, b1=b1, mse=(numpy.sum((b0 + b1 * zp - ks) ** 2) / n)))
# iteration = 0, B1 = 2.620538882402765, mse = 6470.414201176658
# iteration = 100, B1 = 2.620538882402765, mse = 6470.414201176658
# iteration = 200, B1 = 2.620538882402765, mse = 6470.414201176658
# iteration = 300, B1 = 2.620538882402765, mse = 6470.414201176658
# iteration = 400, B1 = 2.620538882402765, mse = 6470.414201176658
# iteration = 500, B1 = 2.620538882402765, mse = 6470.414201176658
# iteration = 600, B1 = 2.620538882402765, mse = 6470.414201176658
# iteration = 700, B1 = 2.620538882402765, mse = 6470.414201176658
# iteration = 800, B1 = 2.620538882402765, mse = 6470.414201176658
# iteration = 900, B1 = 2.620538882402765, mse = 6470.414201176658