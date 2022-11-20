from chapter06.exercise6_5_3 import min_heap_insert, heap_extract_min
from chapter06.textbook6_5 import max_heap_insert, heap_extract_max, heap_maximum


def priority_enqueue(Q, x):
    x.key = Q.rank
    min_heap_insert(Q, x)
    Q.rank += 1


def priority_dequeue(Q):
    return heap_extract_min(Q)


def priority_push(Q, x):
    maximum = heap_maximum(Q)
    x.key = maximum.key + 1 if maximum is not None else 1
    max_heap_insert(Q, x)


def priority_pop(Q):
    return heap_extract_max(Q)
