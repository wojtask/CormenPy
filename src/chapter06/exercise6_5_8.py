import math

from chapter06.textbook6_1 import parent, left, right
from datastructures.array import Array
from datastructures.list import List, SNode


def merge_sorted_lists(lists):
    k = lists.length
    Q = Array.indexed(1, k)
    Q.heap_size = 0
    for list_ in lists:
        if list_.head is not None:
            x = list_.head
            list_.head = list_.head.next
            x.next = None
            _min_heap_insert_pair(Q, (x, list_))
    merged_list = List()
    tail = None
    while Q.heap_size > 0:
        element, list_ = _heap_extract_min_pair(Q)
        if merged_list.head is None:
            tail = merged_list.head = element
        else:
            tail.next = element
            tail = tail.next
        if list_.head is not None:
            _min_heap_insert_pair(Q, (list_.head, list_))
            list_.head = list_.head.next
    return merged_list


def _min_heap_insert_pair(A, pair):
    A.heap_size += 1
    A[A.heap_size] = (SNode(math.inf), None)
    _heap_decrease_pair_key(A, A.heap_size, pair)


def _heap_decrease_pair_key(A, i, pair):
    if pair[0].key > A[i][0].key:
        raise ValueError('new key is larger than current key')
    A[i] = pair
    while i > 1 and A[parent(i)][0].key > A[i][0].key:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)


def _heap_extract_min_pair(A):
    if A.heap_size < 1:
        raise ValueError('heap underflow')
    min_pair = A[1]
    A[1] = A[A.heap_size]
    A.heap_size -= 1
    _min_heapify_pair(A, 1)
    return min_pair


def _min_heapify_pair(A, i):
    l = left(i)
    r = right(i)
    if l <= A.heap_size and A[l][0].key < A[i][0].key:
        smallest = l
    else:
        smallest = i
    if r <= A.heap_size and A[r][0].key < A[smallest][0].key:
        smallest = r
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        _min_heapify_pair(A, smallest)
