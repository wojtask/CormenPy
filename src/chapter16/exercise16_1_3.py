from chapter10.textbook10_1 import pop, push
from chapter13.textbook13_2 import rb_search
from chapter13.textbook13_3 import rb_insert
from chapter13.textbook13_4 import rb_delete
from datastructures.array import Array
from datastructures.red_black_tree import RedBlackTree, Node
from util import rbetween


def activity_scheduler(s, f):
    n = s.length
    A = Array.indexed(1, n)
    F = Array(rbetween(n, 1))
    F.top = n
    B = RedBlackTree()
    # events contains triples (a, b, c) where a = 0 if the event is finish of an activity and 1 if it is start,
    # b as the activity number, and c as the start time or the finish time
    events = Array([(0, i + 1, finish_time) for i, finish_time in enumerate(f)] +
                   [(1, i + 1, start_time) for i, start_time in enumerate(s)])
    events.sort(key=lambda e: (e[2], e[0]))
    for e in events:
        if e[0] == 1:
            hall_number = pop(F)
            A[e[1]] = hall_number
            rb_insert(B, Node(e[1], data=hall_number), sentinel=B.nil)
        else:
            hall = rb_search(B.root, e[1], sentinel=B.nil)
            push(F, hall.data)
            rb_delete(B, hall, sentinel=B.nil)
    return A
