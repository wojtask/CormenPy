from util import rbetween


def greedy_activity_selector_(s, f):
    n = s.length - 2
    A = {'a' + str(n)}
    i = n
    for m in rbetween(n - 1, 1):
        if f[m] <= s[i]:
            A.add('a' + str(m))
            i = m
    return A
