import copy
import random
from unittest import TestCase

from hamcrest import *

from chapter06.exercise6_5_7 import max_heap_delete
from heap_util import get_random_max_heap, assert_max_heap


class TestExercise6_5_7(TestCase):

    def test_max_heap_delete(self):
        heap = get_random_max_heap()
        original = copy.deepcopy(heap)
        i = random.randint(1, heap.heap_size)
        key_to_delete = heap[i]

        actual_deleted_key = max_heap_delete(heap, i)

        assert_that(actual_deleted_key, is_(equal_to(key_to_delete)))
        assert_max_heap(heap)
        expected_heap_keys = original.elements
        expected_heap_keys.remove(key_to_delete)
        assert_that(heap, contains_inanyorder(*expected_heap_keys))
