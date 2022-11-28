from chapter10.textbook10_1 import pop, push
from datastructures.array import Array
from datastructures.stack import Stack
from util import rbetween


def activity_scheduler(s, f):
    n = s.length
    A = Array.indexed(1, n)
    F = Stack(rbetween(n, 1), top=n)
    H = Array.indexed(1, n)
    # events contains triples (a, b, c) where a = 0 if the event is finish of an activity and 1 if it is start,
    # b as the activity number, and c is the start time or the finish time
    events = Array((0, i + 1, finish_time) for i, finish_time in enumerate(f)) + \
        Array((1, i + 1, start_time) for i, start_time in enumerate(s))
    events.sort(key=lambda e: (e[2], e[0]))
    for e in events:
        if e[0] == 1:
            A[e[1]] = H[e[1]] = pop(F)
        else:
            push(F, H[e[1]])
            H[e[1]] = None
    return A
