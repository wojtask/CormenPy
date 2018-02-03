from datastructures.array import Array
from util import between, rbetween


def _sort_jobs_by_deadlines(a, t, p, d):
    sorted_tuples = sorted(zip(a, t, p, d), key=lambda x: x[3])
    a.elements = [x[0] for x in sorted_tuples]
    t.elements = [x[1] for x in sorted_tuples]
    p.elements = [x[2] for x in sorted_tuples]
    d.elements = [x[3] for x in sorted_tuples]


def jobs_scheduling(t, p, d):
    n = p.length
    a = Array(list(between(1, n)))
    _sort_jobs_by_deadlines(a, t, p, d)
    for i in between(1, n):
        d[i] = min(d[i], n ** 2)
    P = Array.indexed(0, d[n])
    s = Array([Array.indexed(0, d[n]) for _ in between(1, n)])
    for j in between(0, d[n]):
        P[j] = 0
    for i in between(1, n):
        for j in between(0, d[n]):
            s[i, j] = 0
    for i in between(1, n):
        if t[i] <= d[i]:
            for j in rbetween(d[n], t[i]):
                if P[min(j, d[i]) - t[i]] + p[i] > P[j]:
                    P[j] = P[min(j, d[i]) - t[i]] + p[i]
                    s[i, j] = 1
    return P, s, a


def print_schedule(s, a, t, d, i, j):
    if i > 0:
        if s[i, j] == 1:
            print_schedule(s, a, t, d, i - 1, min(j, d[i]) - t[i])
            print('a' + str(a[i]))
        else:
            print_schedule(s, a, t, d, i - 1, j)
