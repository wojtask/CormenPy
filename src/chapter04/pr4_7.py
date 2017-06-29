import math

from datastructures.array import Array
from util import scope


def monge_minimums(A):
    m = A.length
    minimums_indices = monge_minimums_indices(A)
    minimums = Array.of_length(m)
    for i in scope(1, m):
        minimums[i] = A[i][minimums_indices[i]]
    return minimums


def monge_minimums_indices(A):
    m = A.length
    if m == 0:
        return Array([])
    n = A[1].length
    A_ = Array.of_length(m // 2)
    for j in scope(1, m // 2):
        A_[j] = A[2 * j]
    minimums_indices_even_rows = monge_minimums_indices(A_)
    minimums_indices = Array.of_length(m)
    for j in scope(1, m // 2):
        minimums_indices[2 * j] = minimums_indices_even_rows[j]
    for j in scope(1, math.ceil(m / 2)):
        i = 2 * j - 1
        prev_minimum_index = minimums_indices[i - 1] if i > 1 else 1
        next_minimum_index = minimums_indices[i + 1] if i < m else n
        minimum = min([A[i][k] for k in scope(prev_minimum_index, next_minimum_index)])
        for k in scope(prev_minimum_index, next_minimum_index):
            if A[i][k] == minimum:
                minimums_indices[i] = k
                break
    return minimums_indices
