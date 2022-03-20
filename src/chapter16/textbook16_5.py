from chapter16.exercise16_5_2 import tasks_independent
from datastructures.array import Array
from util import between


def _build_early_first_schedule(A, tasks):
    schedule = Array()
    tasks.sort(key=lambda t: t[1])
    for task in tasks:
        if task[0] in A:
            schedule.append(task[0])
    for task in tasks:
        if task[0] not in A:
            schedule.append(task[0])
    return schedule


def tasks_scheduling(d, w):
    n = d.length
    A = set()
    deadlines = Array()
    tasks = Array(zip(['a' + str(i) for i in between(1, n)], d, w))
    tasks.sort(key=lambda t: t[2], reverse=True)
    for task in tasks:
        if tasks_independent(deadlines + [task[1]], n):
            deadlines.append(task[1])
            A.add(task[0])
    return _build_early_first_schedule(A, tasks)
