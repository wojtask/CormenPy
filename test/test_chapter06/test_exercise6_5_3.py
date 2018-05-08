import random
from unittest import TestCase

from hamcrest import *

from chapter06.exercise6_5_3 import heap_minimum, heap_extract_min, heap_decrease_key, min_heap_insert
from heap_util import get_random_min_heap, assert_min_heap


class TestExercise6_5_3(TestCase):

    def test_heap_minimum(self):
        heap, elements = get_random_min_heap()

        actual_min = heap_minimum(heap)

        assert_that(actual_min, is_(equal_to(min(elements))))

    def test_extract_min(self):
        heap, elements = get_random_min_heap()

        actual_min = heap_extract_min(heap)

        assert_that(actual_min, is_(equal_to(min(elements))))
        assert_min_heap(heap)
        actual_heap_keys = heap[1:heap.heap_size]
        expected_heap_keys = sorted(elements)[1:]  # all but minimum
        assert_that(actual_heap_keys, contains_inanyorder(*expected_heap_keys))

    def test_heap_decrease_key(self):
        heap, elements = get_random_min_heap()
        i = random.randint(1, heap.heap_size)
        old_key = heap[i]
        new_key = random.randrange(1000)

        if new_key > old_key:
            assert_that(calling(heap_decrease_key).with_args(heap, i, new_key),
                        raises(RuntimeError, 'new key is larger than current key'))
        else:
            heap_decrease_key(heap, i, new_key)

            assert_that(heap.heap_size, is_(equal_to(len(elements))))
            expected_heap_keys = list(elements)
            expected_heap_keys.remove(old_key)
            expected_heap_keys.append(new_key)
            assert_that(heap.elements, contains_inanyorder(*expected_heap_keys))

    def test_min_heap_insert(self):
        heap, elements = get_random_min_heap()
        heap.elements.append(None)  # to increase the heap's capacity for the new element
        heap.length += 1
        new_key = random.randrange(1000)

        min_heap_insert(heap, new_key)

        assert_that(heap.heap_size, is_(equal_to(len(elements) + 1)))
        assert_min_heap(heap)
        expected_heap_keys = elements + [new_key]
        assert_that(heap.elements, contains_inanyorder(*expected_heap_keys))
