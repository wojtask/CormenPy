from chapter06.exercise6_5_3 import min_heap_insert, heap_extract_min
from datastructures.array import Array
from datastructures.essential import Element
from datastructures.list import List


def merge_sorted_lists(lists):
    k = lists.length
    Q = Array.indexed(1, k)
    Q.heap_size = 0
    for list_ in lists:
        if list_.head is not None:
            x = list_.head
            list_.head = list_.head.next
            x.next = None
            min_heap_insert(Q, Element(key=x.key, data=(x, list_)))
    merged_list = List()
    tail = None
    while Q.heap_size > 0:
        element, list_ = heap_extract_min(Q).data
        if merged_list.head is None:
            tail = merged_list.head = element
        else:
            tail.next = element
            tail = tail.next
        if list_.head is not None:
            min_heap_insert(Q, Element(key=list_.head.key, data=(list_.head, list_)))
            list_.head = list_.head.next
    return merged_list
