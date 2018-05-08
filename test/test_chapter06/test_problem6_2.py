import random
from unittest import TestCase

from hamcrest import *

from chapter06.problem6_2 import multiary_parent, multiary_child, multiary_max_heapify, multiary_heap_extract_max, \
    multiary_max_heap_insert, multiary_heap_increase_key
from heap_util import get_random_max_heap, assert_max_heap


class TestProblem6_2(TestCase):

    def test_multiary_parent_child(self):
        d = random.randint(2, 7)
        i = random.randint(1, 30)

        for k in range(1, d + 1):
            assert_that(multiary_parent(d, multiary_child(d, i, k)), is_(equal_to(i)))

    def test_multiary_max_heapify(self):
        ary = random.randint(2, 7)
        heap, elements = get_random_max_heap(ary=ary)
        i = random.randint(1, heap.heap_size)
        heap[i] = elements[i - 1] = random.randint(0, heap[i])  # randomly decrease value of randomly chosen element

        multiary_max_heapify(heap, ary, i)

        assert_that(heap.heap_size, is_(equal_to(len(elements))))
        assert_max_heap(heap, ary=ary)
        assert_that(heap.elements, contains_inanyorder(*elements))

    def test_multiary_heap_extract_max(self):
        ary = random.randint(2, 7)
        heap, elements = get_random_max_heap(ary=ary)

        actual_max = multiary_heap_extract_max(heap, ary)

        assert_that(actual_max, is_(equal_to(max(elements))))
        assert_max_heap(heap, ary=ary)
        actual_heap_keys = heap[1:heap.heap_size]
        expected_heap_keys = sorted(elements)[:-1]  # all but maximum
        assert_that(actual_heap_keys, contains_inanyorder(*expected_heap_keys))

    def test_multiary_max_heap_insert(self):
        ary = random.randint(2, 7)
        heap, elements = get_random_max_heap(ary=ary)
        heap.elements.append(None)  # to increase the heap's capacity for the new element
        heap.length += 1
        new_key = random.randrange(1000)

        multiary_max_heap_insert(heap, ary, new_key)

        assert_that(heap.heap_size, is_(equal_to(len(elements) + 1)))
        assert_max_heap(heap, ary=ary)
        expected_heap_keys = elements + [new_key]
        assert_that(heap.elements, contains_inanyorder(*expected_heap_keys))

    def test_multiary_heap_increase_key(self):
        ary = random.randint(2, 7)
        heap, elements = get_random_max_heap(ary=ary)
        i = random.randint(1, heap.heap_size)
        old_key = heap[i]
        new_key = random.randrange(1000)
        real_new_key = max(old_key, new_key)

        multiary_heap_increase_key(heap, ary, i, new_key)

        assert_that(heap.heap_size, is_(equal_to(len(elements))))
        assert_max_heap(heap, ary=ary)
        expected_heap_keys = list(elements)
        expected_heap_keys.remove(old_key)
        expected_heap_keys.append(real_new_key)
        assert_that(heap.elements, contains_inanyorder(*expected_heap_keys))
