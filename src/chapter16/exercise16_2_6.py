import math

from chapter09.textbook9_3 import select
from datastructures.array import Array
from util import between


class Item:
    def __init__(self, id, weight, value):
        self.id = id
        self.weight = weight
        self.value = value


def _sort_by_value_per_weight_unit(w, v):
    sorted_tuples = sorted(zip(w, v), key=lambda x: x[1] / x[0], reverse=True)
    w.elements = [x[0] for x in sorted_tuples]
    v.elements = [x[1] for x in sorted_tuples]


def effective_fractional_knapsack(w, v, W):
    n = w.length
    _sort_by_value_per_weight_unit(w, v)
    items = Array(Item(i, w[i], v[i]) for i in between(1, n))
    K = Array([0] * n)
    return _effective_fractional_knapsack(items, K, W)


def _effective_fractional_knapsack(items, K, W):
    n = items.length
    if n == 0:
        return K
    unit_values = Array(item.value / item.weight for item in items)
    m = select(unit_values, 1, n, math.floor((n + 1) / 2))
    G = Array(item for item in items if item.value / item.weight > m)
    E = Array(item for item in items if item.value / item.weight == m)
    L = Array(item for item in items if item.value / item.weight < m)
    w_G = sum(item.weight for item in G)
    w_E = sum(item.weight for item in E)
    if w_G >= W:
        return _effective_fractional_knapsack(G, K, W)
    for item in G:
        K[item.id] = item.weight
    weight_sum = w_G
    for item in E:
        if weight_sum + item.weight > W:
            K[item.id] = W - weight_sum
            break
        K[item.id] = item.weight
        weight_sum += item.weight
    if w_G + w_E >= W:
        return K
    else:
        return _effective_fractional_knapsack(L, K, W - w_G - w_E)
