from datastructures.array import Array
from util import between


def _sort_by_value_per_weight_unit(w, v):
    sorted_tuples = sorted(zip(w, v), key=lambda x: x[1] / x[0], reverse=True)
    w.elements = [x[0] for x in sorted_tuples]
    v.elements = [x[1] for x in sorted_tuples]


def fractional_knapsack(w, v, W):
    _sort_by_value_per_weight_unit(w, v)
    n = w.length
    K = Array.indexed(1, n)
    weight = 0
    for i in between(1, n):
        if weight + w[i] <= W:
            K[i] = w[i]
        elif weight < W:
            K[i] = W - weight
        else:
            K[i] = 0
        weight += K[i]
    return K
