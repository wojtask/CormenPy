import random
from unittest import TestCase

from hamcrest import *

from chapter06.exercise6_5_3 import heap_minimum, heap_extract_min, heap_decrease_key, min_heap_insert
from datastructures.array import Array
from heap_util import get_random_min_heap, assert_min_heap


class TestExercise6_5_3(TestCase):

    def test_heap_minimum(self):
        heap = get_random_min_heap()

        actual_min = heap_minimum(heap)

        assert_that(heap.is_modified(), is_(False))
        assert_that(actual_min, is_(equal_to(min(heap))))

    def test_extract_min(self):
        heap = get_random_min_heap()
        original_elements = Array(heap)

        actual_min = heap_extract_min(heap)

        assert_that(actual_min, is_(equal_to(min(original_elements))))
        assert_min_heap(heap)
        original_elements.remove(actual_min)
        assert_that(heap, contains_inanyorder(*original_elements))

    def test_heap_decrease_key(self):
        heap = get_random_min_heap()
        original_elements = Array(heap)
        i = random.randint(1, heap.heap_size)
        old_key = heap[i]
        new_key = random.randint(0, 999)

        if new_key > old_key:
            assert_that(calling(heap_decrease_key).with_args(heap, i, new_key),
                        raises(ValueError, 'new key is larger than current key'))
        else:
            heap_decrease_key(heap, i, new_key)

            original_elements.remove(old_key)
            original_elements.append(new_key)
            assert_that(heap, contains_inanyorder(*original_elements))

    def test_min_heap_insert(self):
        heap = get_random_min_heap()
        original_elements = Array(heap)
        heap.append(None)  # to increase the heap's capacity for the new element
        new_key = random.randint(0, 999)

        min_heap_insert(heap, new_key)

        assert_min_heap(heap)
        assert_that(heap, contains_inanyorder(*original_elements, new_key))
