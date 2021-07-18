import copy
import random
from unittest import TestCase

from hamcrest import *

from chapter06.exercise6_5_3 import heap_minimum, heap_extract_min, heap_decrease_key, min_heap_insert
from heap_util import get_random_min_heap, assert_min_heap


class TestExercise6_5_3(TestCase):

    def test_heap_minimum(self):
        heap = get_random_min_heap()
        original = copy.deepcopy(heap)

        actual_min = heap_minimum(heap)

        assert_that(actual_min, is_(equal_to(min(heap))))
        assert_that(heap, is_(equal_to(original)))

    def test_extract_min(self):
        heap = get_random_min_heap()
        original = copy.deepcopy(heap)

        actual_min = heap_extract_min(heap)

        assert_that(actual_min, is_(equal_to(min(original))))
        assert_min_heap(heap)
        expected_heap_keys = original.elements
        expected_heap_keys.remove(actual_min)
        assert_that(heap, contains_inanyorder(*expected_heap_keys))

    def test_heap_decrease_key(self):
        heap = get_random_min_heap()
        original = copy.deepcopy(heap)
        i = random.randint(1, heap.heap_size)
        old_key = heap[i]
        new_key = random.randrange(1000)

        if new_key > old_key:
            assert_that(calling(heap_decrease_key).with_args(heap, i, new_key),
                        raises(ValueError, 'new key is larger than current key'))
        else:
            heap_decrease_key(heap, i, new_key)

            expected_heap_keys = original.elements
            expected_heap_keys.remove(old_key)
            expected_heap_keys.append(new_key)
            assert_that(heap, contains_inanyorder(*expected_heap_keys))

    def test_min_heap_insert(self):
        heap = get_random_min_heap()
        original = copy.deepcopy(heap)
        heap.elements.append(None)  # to increase the heap's capacity for the new element
        heap.length += 1
        new_key = random.randrange(1000)

        min_heap_insert(heap, new_key)

        assert_min_heap(heap)
        assert_that(heap, contains_inanyorder(*original, new_key))
