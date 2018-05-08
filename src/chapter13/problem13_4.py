from chapter12.textbook_exercise12_3_3 import tree_insert
from chapter13.exercise13_2_1 import right_rotate
from chapter13.textbook13_2 import left_rotate


def treap_insert(T, x):
    tree_insert(T, x)
    while x is not T.root and x.priority < x.p.priority:
        if x is x.p.left:
            right_rotate(T, x.p)
        else:
            left_rotate(T, x.p)
