import copy
import random
from unittest import TestCase

from hamcrest import *

from chapter06.problem6_2 import multiary_parent, multiary_child, multiary_max_heapify, multiary_heap_extract_max, \
    multiary_max_heap_insert, multiary_heap_increase_key
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
        heap[i] = random.randint(0, heap[i])  # randomly decrease the value of a randomly chosen element
        original = copy.deepcopy(heap)

        multiary_max_heapify(heap, arity, i)

        assert_max_heap(heap, arity=arity)
        assert_that(heap, contains_inanyorder(*original))

    def test_multiary_heap_extract_max(self):
        arity = random.randint(2, 7)
        heap = get_random_max_heap(arity=arity)
        original = copy.deepcopy(heap)

        actual_max = multiary_heap_extract_max(heap, arity)

        assert_that(actual_max, is_(equal_to(max(original))))
        assert_max_heap(heap, arity=arity)
        expected_heap_keys = original.sort(reverse=True)[2:]  # all but maximum
        assert_that(heap, contains_inanyorder(*expected_heap_keys))

    def test_multiary_max_heap_insert(self):
        arity = random.randint(2, 7)
        heap = get_random_max_heap(arity=arity)
        original = copy.deepcopy(heap)
        heap.elements.append(None)  # to increase the heap's capacity for the new element
        heap.length += 1
        new_key = random.randrange(1000)

        multiary_max_heap_insert(heap, arity, new_key)

        assert_max_heap(heap, arity=arity)
        assert_that(heap, contains_inanyorder(*original, new_key))

    def test_multiary_heap_increase_key(self):
        arity = random.randint(2, 7)
        heap = get_random_max_heap(arity=arity)
        original = copy.deepcopy(heap)
        i = random.randint(1, heap.heap_size)
        old_key = heap[i]
        new_key = random.randrange(1000)
        real_new_key = max(old_key, new_key)

        multiary_heap_increase_key(heap, arity, i, new_key)

        assert_max_heap(heap, arity=arity)
        expected_heap_keys = original.elements
        expected_heap_keys.remove(old_key)
        expected_heap_keys.append(real_new_key)
        assert_that(heap, contains_inanyorder(*expected_heap_keys))
