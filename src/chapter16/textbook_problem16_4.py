from datastructures.array import Array
from util import between


def tasks_scheduling_(d, w):
    n = d.length
    tasks = list(zip(['a' + str(i) for i in between(1, n)], d, w))
    tasks.sort(key=lambda t: t[2], reverse=True)
    schedule = Array.indexed(1, n)
    for task in tasks:
        i = task[1]
        while i >= 1 and schedule[i] is not None:
            i -= 1
        if i >= 1:
            schedule[i] = task[0]
        else:
            j = n
            while schedule[j] is not None:
                j -= 1
            schedule[j] = task[0]
    return schedule
