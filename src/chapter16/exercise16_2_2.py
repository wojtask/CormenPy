from datastructures.array import Array
from util import between


def knapsack(w, v, W):
    n = w.length
    V = Array((Array.indexed(0, W) for _ in between(0, n)), start=0)
    for j in between(0, W):
        V[0, j] = 0
    for i in between(1, n):
        for j in between(0, W):
            if w[i] > j:
                V[i, j] = V[i - 1, j]
            else:
                V[i, j] = max(V[i - 1, j], V[i - 1, j - w[i]] + v[i])
    return V


def print_knapsack(V, w, i, j):
    if i >= 1:
        if V[i, j] == V[i - 1, j]:
            print_knapsack(V, w, i - 1, j)
        else:
            print_knapsack(V, w, i - 1, j - w[i])
            print('a' + str(i))
