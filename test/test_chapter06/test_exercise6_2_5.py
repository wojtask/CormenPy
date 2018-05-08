import random
from unittest import TestCase

from hamcrest import *

from chapter06.exercise6_2_5 import iterative_max_heapify
from heap_util import get_random_max_heap, assert_max_heap


class TestExercise6_2_5(TestCase):

    def test_iterative_max_heapify(self):
        heap, elements = get_random_max_heap()
        i = random.randint(1, heap.heap_size)
        heap[i] = elements[i - 1] = random.randint(0, heap[i])  # randomly decrease value of randomly chosen element

        iterative_max_heapify(heap, i)

        assert_that(heap.heap_size, is_(equal_to(len(elements))))
        assert_max_heap(heap)
        assert_that(heap.elements, contains_inanyorder(*elements))
