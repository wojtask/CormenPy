from datastructures.array import Array
from util import between


def lis_length(X):
    n = X.length
    c = Array.indexed(1, n)
    b = Array.indexed(1, n)
    longest = 0
    b_star = 0
    for i in between(1, n):
        c[i] = 1
        b[i] = 0
        for j in between(1, i - 1):
            if X[j] <= X[i] and c[j] + 1 > c[i]:
                c[i] = c[j] + 1
                b[i] = j
        if c[i] > longest:
            longest = c[i]
            b_star = i
    return longest, b, b_star


def print_lis(b, X, i):
    if b[i] > 0:
        print_lis(b, X, b[i])
    print(X[i])
