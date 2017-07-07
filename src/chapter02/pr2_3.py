from util import between


def naive_polynomial_evaluation(a, x):
    y = 0.0
    n = a.length - 1
    for i in between(0, n):
        s = a[i]
        for j in between(1, i):
            s = s * x
        y = y + s
    return y
