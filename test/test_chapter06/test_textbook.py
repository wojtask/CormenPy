import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter06.textbook import heapsort, heap_maximum, heap_extract_max, heap_increase_key, max_heap_insert, \
    build_max_heap_
from datastructures.array import Array
from heap_util import assert_max_heap, get_random_max_heap


class Textbook06Test(TestCase):

    def test_heapsort(self):
        array, data = get_random_array()

        heapsort(array)

        expected_array = Array(sorted(data))
        assert_that(array, is_(equal_to(expected_array)))

    def test_heap_maximum(self):
        heap, data = get_random_max_heap()

        actual_max = heap_maximum(heap)

        assert_that(actual_max, is_(equal_to(max(data))))

    def test_extract_max(self):
        heap, data = get_random_max_heap()

        actual_max = heap_extract_max(heap)

        assert_that(actual_max, is_(equal_to(max(data))))
        assert_max_heap(heap)
        actual_heap_keys = heap[1:heap.heap_size]
        expected_heap_keys = sorted(data)[:-1]  # all but maximum
        assert_that(actual_heap_keys, contains_inanyorder(*expected_heap_keys))

    def test_heap_increase_key(self):
        heap, data = get_random_max_heap()
        i = random.randint(1, heap.heap_size)
        old_key = heap[i]
        new_key = random.randrange(1000)

        if new_key < old_key:
            assert_that(calling(heap_increase_key).with_args(heap, i, new_key),
                        raises(RuntimeError, 'new key is smaller than current key'))
        else:
            heap_increase_key(heap, i, new_key)

            assert_that(heap.heap_size, is_(equal_to(len(data))))
            assert_max_heap(heap)
            expected_heap_keys = list(data)
            expected_heap_keys.remove(old_key)
            expected_heap_keys.append(new_key)
            assert_that(heap.data, contains_inanyorder(*expected_heap_keys))

    def test_max_heap_insert(self):
        heap, data = get_random_max_heap()
        heap.data.append(None)  # to increase the heap's capacity for the new element
        heap.length += 1
        new_key = random.randrange(1000)

        max_heap_insert(heap, new_key)

        assert_that(heap.heap_size, is_(equal_to(len(data) + 1)))
        assert_max_heap(heap)
        expected_heap_keys = data + [new_key]
        assert_that(heap.data, contains_inanyorder(*expected_heap_keys))

    def test_build_max_heap_(self):
        array, data = get_random_array()

        build_max_heap_(array)

        assert_that(array, has_property('heap_size'))
        assert_that(array.heap_size, is_(equal_to(array.length)))
        assert_max_heap(array)
