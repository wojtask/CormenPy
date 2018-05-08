def horner(a, x):
    y = 0.0
    i = a.length - 1
    while i >= 0:
        y = a[i] + x * y
        i = i - 1
    return y
