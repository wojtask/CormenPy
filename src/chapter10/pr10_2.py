from chapter06.ex6_5_8 import merge_sorted_lists
from chapter10.ex10_2_1 import singly_linked_list_insert, singly_linked_list_delete
from chapter11.textbook import chained_hash_insert, chained_hash_search
from datastructures.array import Array
from datastructures.hash_table import ChainedElement
from datastructures.list import List, SNode
from datastructures.standard_array import StandardArray


def sorted_list_make_min_heap():
    return List()


def sorted_list_min_heap_insert(heap, key):
    x = SNode(key)
    if heap.head is None:
        heap.head = x
        return
    if key < heap.head.key:
        x.next = heap.head
        heap.head = x
        return
    y = heap.head
    while y.next is not None and y.next.key < key:
        y = y.next
    x.next = y.next
    y.next = x


def sorted_list_heap_minimum(heap):
    return heap.head.key


def sorted_list_heap_extract_min(heap):
    if heap.head is None:
        raise RuntimeError('heap underflow')
    min = heap.head.key
    heap.head = heap.head.next
    return min


def sorted_list_min_heap_union(heap1, heap2):
    merged_heaps = merge_sorted_lists(Array([heap1, heap2]))
    x = merged_heaps.head
    while x is not None:
        y = x.next
        if y is not None and x.key == y.key:
            x.next = y.next
        x = x.next
    return merged_heaps


def list_make_min_heap():
    heap = List()
    heap.tail = None
    return heap


def list_min_heap_insert(heap, key):
    x = SNode(key)
    if heap.head is None or key < heap.head.key:
        singly_linked_list_insert(heap, x)
        if heap.tail is None:
            heap.tail = x
    else:
        x.next = heap.head.next
        heap.head.next = x
        if heap.tail is heap.head:
            heap.tail = x


def list_heap_minimum(heap):
    return heap.head.key


def list_heap_extract_min(heap):
    if heap.head is None:
        raise RuntimeError('heap underflow')
    min = heap.head.key
    heap.head = heap.head.next
    if heap.head is None:
        heap.tail = None
        return min
    x = new_min = heap.head
    while x is not None:
        if x.key < new_min.key:
            new_min = x
        x = x.next
    singly_linked_list_delete(heap, new_min)
    singly_linked_list_insert(heap, new_min)
    x = heap.head
    while x.next is not None:
        x = x.next
    heap.tail = x
    return min


def list_min_heap_union(heap1, heap2):
    if heap1.head is not None and heap2.head is not None and heap1.head.key < heap2.head.key:
        new_min = heap1.head
    else:
        new_min = heap2.head
    # according to the textbook, 701 is a 'good' value for hash table size when using the division method
    hash_table = StandardArray.of_length(701)
    h = lambda k, m: k % m
    x = heap1.head
    while x is not None:
        y = ChainedElement(x.key)
        chained_hash_insert(hash_table, y, h)
        x = x.next
    x = heap2.head
    while x is not None:
        y = x.next
        if chained_hash_search(hash_table, x.key, h) is None:
            singly_linked_list_insert(heap1, x)
        x = y
    singly_linked_list_delete(heap1, new_min)
    singly_linked_list_insert(heap1, new_min)
    return heap1


def list_min_heap_disjoint_union(heap1, heap2):
    if heap1.head is None:
        return heap2
    if heap2.head is None:
        return heap1
    if heap1.head.key < heap2.head.key:
        heap1.tail.next = heap2.head
        heap1.tail = heap2.tail
        return heap1
    else:
        heap2.tail.next = heap1.head
        heap2.tail = heap1.tail
        return heap2
