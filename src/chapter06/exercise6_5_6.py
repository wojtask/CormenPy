from chapter06.exercise6_5_3 import min_heap_insert, heap_extract_min
from chapter06.textbook6_5 import max_heap_insert, heap_extract_max


def priority_enqueue(Q, x):
    x.key = Q.rank
    min_heap_insert(Q, x)
    Q.rank += 1


def priority_dequeue(Q):
    return heap_extract_min(Q)


def priority_push(Q, x):
    x.key = Q.rank
    max_heap_insert(Q, x)
    Q.rank += 1


def priority_pop(Q):
    return heap_extract_max(Q)
