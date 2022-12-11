from chapter06.exercise6_5_8 import merge_sorted_lists
from chapter10.exercise10_2_1 import singly_linked_list_insert, singly_linked_list_delete
from chapter10.exercise10_2_3 import singly_linked_list_enqueue
from datastructures.array import Array
from datastructures.list import List, SinglyLinkedNode, ListWithTail


def sorted_list_make_min_heap():
    return List()


def sorted_list_min_heap_insert(heap, key):
    x = SinglyLinkedNode(key)
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
        raise ValueError('heap underflow')
    min = heap.head.key
    heap.head = heap.head.next
    return min


def sorted_list_min_heap_union(heap1, heap2):
    merged_heaps = merge_sorted_lists(Array.of(heap1, heap2))
    x = merged_heaps.head
    while x is not None:
        y = x.next
        if y is not None and x.key == y.key:
            x.next = y.next
        x = x.next
    return merged_heaps


def list_make_min_heap():
    return ListWithTail()


def list_min_heap_insert(heap, key):
    x = SinglyLinkedNode(key)
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
        raise ValueError('heap underflow')
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


def _merge_list(p, q, r):
    x = p
    y = q.next
    merged_list = ListWithTail()
    while x is not q.next and y is not r.next:
        if x.key <= y.key:
            singly_linked_list_enqueue(merged_list, x.key)
            x = x.next
        else:
            singly_linked_list_enqueue(merged_list, y.key)
            y = y.next
    while x is not q.next:
        singly_linked_list_enqueue(merged_list, x.key)
        x = x.next
    while y is not r.next:
        singly_linked_list_enqueue(merged_list, y.key)
        y = y.next
    x = p
    z = merged_list.head
    while z is not None:
        x.key = z.key
        x = x.next
        z = z.next


def _merge_sort_list(p, r):
    if p is not None and p is not r:
        q = qq = p
        while qq is not r and qq.next is not r:
            q = q.next
            qq = qq.next.next
        _merge_sort_list(p, q)
        _merge_sort_list(q.next, r)
        _merge_list(p, q, r)


def list_min_heap_union(heap1, heap2):
    _merge_sort_list(heap1.head, heap1.tail)
    _merge_sort_list(heap2.head, heap2.tail)
    return sorted_list_min_heap_union(heap1, heap2)


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
