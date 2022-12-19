from chapter13.textbook13_2 import rb_predecessor, rb_successor
from chapter14.textbook14_1 import os_insert, os_delete


def chained_os_minimum(T):
    return T.nil.next


def chained_os_maximum(T):
    return T.nil.prev


def chained_os_predecessor(T, x):
    return x.prev


def chained_os_successor(T, x):
    return x.next


def chained_os_insert(T, z):
    os_insert(T, z)
    z.prev = rb_predecessor(z, sentinel=T.nil)
    z.next = rb_successor(z, sentinel=T.nil)
    z.prev.next = z.next.prev = z


def chained_os_delete(T, z):
    y = os_delete(T, z)
    y.prev.next = y.next
    y.next.prev = y.prev
    return y
