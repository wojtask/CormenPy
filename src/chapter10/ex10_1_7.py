from chapter10.ex10_1_4 import queue_empty
from chapter10.textbook import enqueue, dequeue
from datastructures.array import Array


def queue_push(Q, x):
    enqueue(Q, x)


def queue_pop(Q):
    if queue_empty(Q):
        raise RuntimeError('underflow')
    x = None
    Q_ = Array.of_length(Q.length - 1)
    Q_.head = Q_.tail = 1
    while not queue_empty(Q):
        x = dequeue(Q)
        if not queue_empty(Q):
            enqueue(Q_, x)
    while not queue_empty(Q_):
        enqueue(Q, dequeue(Q_))
    return x
