import math

from chapter06.exercise6_5_3 import min_heap_insert, heap_minimum, heap_extract_min, heap_decrease_key
from datastructures.array import Array
from datastructures.essential import Activity
from datastructures.heap import Heap
from util import between


def act_schedule(p):
    n = p.length
    p.sort()
    c = Array.indexed(1, n)
    c[1] = p[1]
    for i in between(2, n):
        c[i] = c[i - 1] + p[i]
    return c


def preemptive_act_schedule(p, r):
    n = p.length
    Q = Heap(Array.indexed(1, n))
    c = Array.indexed(1, n)
    times = sorted(zip(p, r), key=lambda x: x[1])
    p, r = Array(x[0] for x in times), Array(x[1] for x in times)
    r.append(math.inf)
    for i in between(1, n):
        t = r[i]
        min_heap_insert(Q, Activity(i, p[i], r[i]))
        while t < r[i + 1] and Q.heap_size != 0:
            a = heap_minimum(Q)
            if t + a.p <= r[i + 1]:
                heap_extract_min(Q)
                t += a.p
                c[a.id] = t
            else:
                a_ = Activity(a.id, a.p - (r[i + 1] - t), a.r)
                heap_decrease_key(Q, 1, a_)
                t = r[i + 1]
    return c
