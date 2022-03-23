import random
from unittest import TestCase

from hamcrest import *

from chapter06.problem6_2 import multiary_parent, multiary_child, multiary_max_heapify, multiary_heap_extract_max, \
    multiary_max_heap_insert, multiary_heap_increase_key
from datastructures.array import Array
from heap_util import get_random_max_heap, assert_max_heap
from util import between


class TestProblem6_2(TestCase):

    def test_multiary_parent_child(self):
        d = random.randint(2, 7)
        i = random.randint(1, 30)

        for k in between(1, d):
            assert_that(multiary_parent(d, multiary_child(d, i, k)), is_(equal_to(i)))

    def test_multiary_max_heapify(self):
        arity = random.randint(2, 7)
        heap = get_random_max_heap(arity=arity)
        i = random.randint(1, heap.heap_size)
        heap[i] -= random.randint(0, 500)  # randomly decrease the value of a randomly chosen element
        original_elements = Array(heap)

        multiary_max_heapify(heap, arity, i)

        assert_max_heap(heap, arity=arity)
        assert_that(heap, contains_inanyorder(*original_elements))

    def test_multiary_heap_extract_max(self):
        arity = random.randint(2, 7)
        heap = get_random_max_heap(arity=arity)
        original_elements = Array(heap)

        actual_max = multiary_heap_extract_max(heap, arity)

        assert_that(actual_max, is_(equal_to(max(original_elements))))
        assert_max_heap(heap, arity=arity)
        expected_heap_keys = original_elements.sort(reverse=True)[2:]  # all but maximum
        assert_that(heap, contains_inanyorder(*expected_heap_keys))

    def test_multiary_max_heap_insert(self):
        arity = random.randint(2, 7)
        heap = get_random_max_heap(arity=arity)
        original_elements = Array(heap)
        heap.append(None)  # to increase the heap's capacity for the new element
        new_key = random.randint(0, 999)

        multiary_max_heap_insert(heap, arity, new_key)

        assert_max_heap(heap, arity=arity)
        assert_that(heap, contains_inanyorder(*original_elements, new_key))

    def test_multiary_heap_increase_key(self):
        arity = random.randint(2, 7)
        heap = get_random_max_heap(arity=arity)
        original_elements = Array(heap)
        i = random.randint(1, heap.heap_size)
        old_key = heap[i]
        new_key = random.randint(0, 999)
        real_new_key = max(old_key, new_key)

        multiary_heap_increase_key(heap, arity, i, new_key)

        assert_max_heap(heap, arity=arity)
        original_elements.remove(old_key)
        original_elements.append(real_new_key)
        assert_that(heap, contains_inanyorder(*original_elements))
