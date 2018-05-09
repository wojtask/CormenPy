from datastructures.array import Array
from util import between


def dynamic_activity_selector(s, f):
    n = s.length - 2
    c = Array([Array.indexed(0, n + 1) for _ in between(0, n + 1)])
    A = Array([Array.indexed(0, n + 1) for _ in between(0, n + 1)])
    for i in between(0, n + 1):
        for j in between(0, n + 1):
            c[i, j] = 0
            A[i, j] = set()
    for l in between(2, n + 2):
        for i in between(0, n - l + 2):
            for j in between(i + 1, n + 1):
                for k in between(i + 1, j - 1):
                    if f[i] <= s[k] and f[k] <= s[j] and c[i, k] + c[k, j] + 1 > c[i, j]:
                        c[i, j] = c[i, k] + c[k, j] + 1
                        A[i, j] = A[i, k] | {'a' + str(k)} | A[k, j]
    return A[0, n + 1]
