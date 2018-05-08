import random
from unittest import TestCase

from hamcrest import *

from chapter06.exercise6_2_2 import min_heapify
from heap_util import get_random_min_heap, assert_min_heap


class TestExercise6_2_2(TestCase):

    def test_min_heapify(self):
        heap, elements = get_random_min_heap()
        i = random.randint(1, heap.heap_size)
        heap[i] = elements[i - 1] = random.randint(heap[i], 999)  # randomly increase value of randomly chosen element

        min_heapify(heap, i)

        assert_that(heap.heap_size, is_(equal_to(len(elements))))
        assert_min_heap(heap)
        assert_that(heap.elements, contains_inanyorder(*elements))
