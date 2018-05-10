from datastructures.array import Array
from util import between


def knapsack(w, v, W):
    n = w.length
    K = Array([Array.indexed(0, W) for _ in between(0, n)], start=0)
    for j in between(0, W):
        K[0, j] = 0
    for i in between(1, n):
        for j in between(0, W):
            K[i, j] = K[i - 1, j]
            if w[i] <= j and K[i - 1, j - w[i]] + v[i] > K[i, j]:
                K[i, j] = K[i - 1, j - w[i]] + v[i]
    return K


def print_knapsack(K, w, i, j):
    if i >= 1:
        if K[i, j] == K[i - 1, j]:
            print_knapsack(K, w, i - 1, j)
        else:
            print_knapsack(K, w, i - 1, j - w[i])
            print('a' + str(i))
