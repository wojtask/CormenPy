from datastructures.array import Array
from util import between, rbetween


def _remove_impossible_jobs(t, p, d):
    filtered_tuples = [(tx, px, dx) for tx, px, dx in zip(t, p, d) if tx <= dx]
    t.elements = [tx for tx, _, _ in filtered_tuples]
    p.elements = [px for _, px, _ in filtered_tuples]
    d.elements = [dx for _, _, dx in filtered_tuples]
    t.length = p.length = d.length = len(filtered_tuples)


def _sort_jobs_by_deadlines(a, t, p, d):
    sorted_tuples = sorted(zip(a, t, p, d), key=lambda x: x[3])
    a.elements = [x[0] for x in sorted_tuples]
    t.elements = [x[1] for x in sorted_tuples]
    p.elements = [x[2] for x in sorted_tuples]
    d.elements = [x[3] for x in sorted_tuples]


def jobs_scheduling(t, p, d):
    _remove_impossible_jobs(t, p, d)
    n = p.length
    a = Array([x for x in between(1, n)])
    _sort_jobs_by_deadlines(a, t, p, d)
    for i in between(1, n):
        d[i] = min(d[i], n ** 2)
    P = Array.indexed(0, d[n])
    X = Array([Array.indexed(0, d[n]) for _ in between(1, n)])
    for i in between(1, n):
        for j in between(0, d[n]):
            X[i, j] = 0
    for j in between(0, t[1] - 1):
        P[j] = 0
    for j in between(t[1], d[n]):
        P[j] = p[1]
        X[1, j] = a[1]
    for i in between(2, n):
        for j in rbetween(d[n], t[i]):
            if P[min(j, d[i]) - t[i]] + p[i] > P[j]:
                P[j] = P[min(j, d[i]) - t[i]] + p[i]
                X[i, j] = a[i]
    return P[d[n]], X


def print_schedule(X, t, d, i, j):
    if i > 0:
        if X[i, j] > 0:
            print_schedule(X, t, d, i - 1, min(j, d[X[i, j]]) - t[X[i, j]])
            print('a' + str(X[i, j]))
        else:
            print_schedule(X, t, d, i - 1, j)
