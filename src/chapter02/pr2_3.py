from util import scope


def naive_polynomial_evaluation(a, x):
    y = 0.0
    n = a.length - 1
    for i in scope(0, n):
        s = a[i]
        for j in scope(1, i):
            s = s * x
        y = y + s
    return y
