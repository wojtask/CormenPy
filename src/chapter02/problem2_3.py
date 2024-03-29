from util import between


def polynomial_evaluate(a, x):
    y = 0.0
    n = a.length - 1
    for i in between(0, n):
        s = a[i]
        for j in between(1, i):
            s *= x
        y += s
    return y
