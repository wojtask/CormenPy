import random
from unittest import TestCase

from hamcrest import *

from chapter06.exercise6_5_7 import max_heap_delete
from datastructures.array import Array
from heap_util import get_random_max_heap, assert_max_heap


class TestExercise6_5_7(TestCase):

    def test_max_heap_delete(self):
        heap = get_random_max_heap()
        original_elements = Array(heap)
        i = random.randint(1, heap.heap_size)
        key_to_delete = heap[i]

        max_heap_delete(heap, i)

        assert_max_heap(heap)
        original_elements.remove(key_to_delete)
        assert_that(heap, contains_inanyorder(*original_elements))
