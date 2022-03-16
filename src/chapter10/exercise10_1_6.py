from chapter10.textbook10_1 import stack_empty, push, pop
from datastructures.array import Array
from datastructures.stack import Stack


def stack_enqueue(S, x):
    push(S, x)


def stack_dequeue(S):
    if stack_empty(S):
        raise ValueError('underflow')
    S_ = Stack(Array.indexed(1, S.length))
    while not stack_empty(S):
        push(S_, pop(S))
    x = pop(S_)
    while not stack_empty(S_):
        push(S, pop(S_))
    return x
