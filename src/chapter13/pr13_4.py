from chapter12.textbook import tree_insert
from chapter13.ex13_2_1 import right_rotate
from chapter13.textbook import left_rotate


def treap_insert(T, x):
    tree_insert(T, x)
    while x != T.root and x.priority < x.p.priority:
        if x == x.p.left:
            right_rotate(T, x.p)
        else:
            left_rotate(T, x.p)
