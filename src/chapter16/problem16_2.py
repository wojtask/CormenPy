from util import between


def average_time_schedule(P):
    n = P.length
    P.elements.sort()
    sum = c = P[1]
    for i in between(2, n):
        c += P[i]
        sum += c
    return sum / n
