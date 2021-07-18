from chapter08.textbook8_3 import radix_sort
from datastructures.array import Array
from util import between, rbetween


def integers_sort(A):
    n = sum(len(str(integer)) for integer in A)
    nonnegative = Array(integer for integer in A if integer >= 0)
    negative = Array(-integer for integer in A if integer < 0)
    sorted_nonnegative = _nonnegative_integers_sort(nonnegative, n)
    sorted_negative = _nonnegative_integers_sort(negative, n)
    A.elements = list(reversed([-integer for integer in sorted_negative])) + sorted_nonnegative


def _nonnegative_integers_sort(nonnegative, n):
    integers_by_length = _sort_by_length(nonnegative, n)
    sorted_integers = []
    for length, integers in enumerate(integers_by_length.elements):
        if integers is not None:
            radix_sort(integers, length + 1)
            sorted_integers.extend(integers.elements)
    return sorted_integers


def _sort_by_length(A, n):
    numbers_by_length = Array.indexed(1, n)
    for number in A:
        if numbers_by_length[len(str(number))] is None:
            numbers_by_length[len(str(number))] = []
        numbers_by_length[len(str(number))].append(number)
    for i in between(1, n):
        if numbers_by_length[i] is not None:
            numbers_by_length[i] = Array(numbers_by_length[i])
    return numbers_by_length


def strings_sort(A):
    _strings_sort(A, 1, A.length, 1)


def _strings_sort(A, p, r, position):
    q = _move_strings_with_exact_length_to_front(A, p, r, position)
    _sort_by_character(A, q, r, position)
    while q <= r:
        q_ = q + 1
        while q_ <= r and A[q][position - 1] == A[q_][position - 1]:
            q_ += 1
        if q_ - q >= 2:
            _strings_sort(A, q, q_ - 1, position + 1)
        q = q_


def _move_strings_with_exact_length_to_front(A, p, r, position):
    q = p
    for j in between(p, r):
        if len(A[j]) == position - 1:
            A[q], A[j] = A[j], A[q]
            q += 1
    return q


def _sort_by_character(A, p, r, position):
    k = ord('z') - ord('a')
    C = Array([0] * (k + 1), start=0)
    for j in between(p, r):
        x = ord(A[j][position - 1]) - ord('a')
        C[x] += 1
    for i in between(1, k):
        C[i] += C[i - 1]
    B = Array.indexed(1, r - p + 1)
    for j in rbetween(r, p):
        x = ord(A[j][position - 1]) - ord('a')
        B[C[x]] = A[j]
        C[x] -= 1
    A.elements[p - 1:r] = B.elements
