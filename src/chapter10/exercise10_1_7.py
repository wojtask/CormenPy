from chapter10.exercise10_1_4 import queue_empty
from chapter10.textbook10_1 import enqueue, dequeue
from datastructures.array import Array
from util import between


def queue_push(Q, x):
    enqueue(Q, x)


def queue_pop(Q):
    if queue_empty(Q):
        raise RuntimeError('underflow')
    Q_ = Array.indexed(1, Q.length - 1)
    Q_.head = Q_.tail = 1
    n = 0
    while not queue_empty(Q):
        enqueue(Q_, dequeue(Q))
        n += 1
    for i in between(1, n - 1):
        enqueue(Q, dequeue(Q_))
    return dequeue(Q_)
