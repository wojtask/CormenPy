from util import between


def recursive_activity_selector(s, f, i, n):
    m = i + 1
    while m <= n and s[m] < f[i]:
        m = m + 1
    if m <= n:
        return {'a' + str(m)} | recursive_activity_selector(s, f, m, n)
    else:
        return set()


def greedy_activity_selector(s, f):
    n = s.length - 2
    A = {'a1'}
    i = 1
    for m in between(2, n):
        if s[m] >= f[i]:
            A.add('a' + str(m))
            i = m
    return A
