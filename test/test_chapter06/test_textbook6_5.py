import copy
import random
from unittest import TestCase

from hamcrest import *

from chapter06.textbook6_5 import heap_maximum, heap_extract_max, heap_increase_key, max_heap_insert
from heap_util import assert_max_heap, get_random_max_heap


class TestTextbook6_5(TestCase):

    def test_heap_maximum(self):
        heap = get_random_max_heap()
        original = copy.deepcopy(heap)

        actual_max = heap_maximum(heap)

        assert_that(actual_max, is_(equal_to(max(heap))))
        assert_that(heap, is_(equal_to(original)))

    def test_extract_max(self):
        heap = get_random_max_heap()
        original = copy.deepcopy(heap)

        actual_max = heap_extract_max(heap)

        assert_that(actual_max, is_(equal_to(max(original))))
        assert_max_heap(heap)
        expected_heap_keys = original.sort(reverse=True)[2:]  # all but maximum
        assert_that(heap, contains_inanyorder(*expected_heap_keys))

    def test_heap_increase_key(self):
        heap = get_random_max_heap()
        original = copy.deepcopy(heap)
        i = random.randint(1, heap.heap_size)
        old_key = heap[i]
        new_key = random.randrange(1000)

        if new_key < old_key:
            assert_that(calling(heap_increase_key).with_args(heap, i, new_key),
                        raises(ValueError, 'new key is smaller than current key'))
        else:
            heap_increase_key(heap, i, new_key)

            assert_max_heap(heap)
            expected_heap_keys = original.elements
            expected_heap_keys.remove(old_key)
            expected_heap_keys.append(new_key)
            assert_that(heap, contains_inanyorder(*expected_heap_keys))

    def test_max_heap_insert(self):
        heap = get_random_max_heap()
        original = copy.deepcopy(heap)
        heap.elements.append(None)  # to increase the heap's capacity for the new element
        heap.length += 1
        new_key = random.randrange(1000)

        max_heap_insert(heap, new_key)

        assert_max_heap(heap)
        assert_that(heap, contains_inanyorder(*original, new_key))
