from chapter02.textbook import insertion_sort
from chapter09.textbook import select
from datastructures.array import Array
from datastructures.standard_array import StandardArray
from util import between


def small_order_select(A, i):
    _small_order_select(A, 1, A.length, i)
    return A[i]


def _small_order_select(A, p, r, i):
    n = r - p + 1
    m = n // 2
    if i >= m:
        return _permutation_producing_select(A, p, r, i)
    permutation = StandardArray(list(range(n)))
    for j in between(0, m - 1):
        if A[p + j] < A[p + m + j]:
            A[p + j], A[p + m + j] = A[p + m + j], A[p + j]
            permutation[j], permutation[m + j] = permutation[m + j], permutation[j]
    permutation_changes = _small_order_select(A, p + m, r, i)
    _apply_permutation_changes(permutation, permutation_changes, m)
    _apply_permutation_changes_with_array_update(permutation, permutation_changes, A, p, p + m - 1)
    for j in between(0, i - 1):
        A[p + i + j], A[p + m + j] = A[p + m + j], A[p + i + j]
        permutation[i + j], permutation[m + j] = permutation[m + j], permutation[i + j]
    permutation_changes = _permutation_producing_select(A, p, p + 2 * i - 1, i)
    _apply_permutation_changes(permutation, permutation_changes, 0)
    return permutation


def _permutation_producing_select(A, p, r, i):
    n = r - p + 1
    permutation = StandardArray(list(range(n)))
    if n == 1:
        return permutation
    fives = [Array(A.data[k:min(k + 5, r)]) for k in range(p - 1, r, 5)]
    for group in fives:
        insertion_sort(group)
    medians = Array([group[(group.length + 1) // 2] for group in fives])
    x = select(medians, 1, medians.length, (medians.length + 1) // 2)
    q = _permutation_changing_partition_around(A, p, r, x, permutation)
    k = q - p + 1
    if i < k:
        permutation_changes = select(A, p, q - 1, i)
        _apply_permutation_changes(permutation, permutation_changes, 0)
    elif i > k:
        permutation_changes = select(A, q + 1, r, i - k)
        _apply_permutation_changes(permutation, permutation_changes, k)
    return permutation


def _permutation_changing_partition_around(A, p, r, x, permutation):
    q = p
    while A[q] != x:
        q += 1
    A[q], A[r] = A[r], A[q]
    permutation[q - p], permutation[r - p] = permutation[r - p], permutation[q - p]
    i = p - 1
    for j in between(p, r - 1):
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
            permutation[i - p], permutation[j - p] = permutation[j - p], permutation[i - p]
    A[i + 1], A[r] = A[r], A[i + 1]
    permutation[i + 1 - p], permutation[r - p] = permutation[r - p], permutation[i + 1 - p]
    return i + 1


def _apply_permutation_changes(permutation, permutation_changes, offset):
    n = permutation_changes.length
    applied_changes = StandardArray([permutation[offset + permutation_changes[j]] for j in between(0, n - 1)])
    for j in between(0, n - 1):
        permutation[offset + j] = applied_changes[j]


def _apply_permutation_changes_with_array_update(permutation, permutation_changes, A, p, r):
    n = r - p + 1
    applied_changes = StandardArray.of_length(n)
    permuted_array_fragment = Array.of_length(n)
    for j in between(0, n - 1):
        if permutation_changes[j] < n - 1:
            applied_changes[j] = permutation[permutation_changes[j]]
            permuted_array_fragment[j + 1] = A[p + permutation_changes[j]]
        else:
            applied_changes[j] = permutation[permutation_changes[n - 1]]
            permuted_array_fragment[j + 1] = A[p + permutation_changes[n - 1]]
    for j in between(0, n - 1):
        permutation[j] = applied_changes[j]
        A[p + j] = permuted_array_fragment[j + 1]
