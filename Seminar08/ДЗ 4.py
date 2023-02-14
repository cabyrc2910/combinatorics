import numpy
from scipy import stats


if __name__ == '__main__':

    x1 = numpy.array([131, 125, 115, 122, 131, 115, 107, 99, 125, 111])

    n1 = x1.size
    d1 = x1.var(ddof=1)
    m1 = x1.mean()

    t1 = stats.t.ppf(0.975, (n1 - 1))

    L = numpy.round(m1 - t1 * numpy.sqrt(d1 / n1), 2)
    U = numpy.round(m1 + t1 * numpy.sqrt(d1 / n1), 2)

    print(f'Доверительный интервал [ {L} ; {U} ]')