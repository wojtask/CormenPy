import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_unique_array
from chapter10.problem10_2 import sorted_list_make_min_heap, sorted_list_min_heap_insert, sorted_list_heap_minimum, \
    sorted_list_heap_extract_min, sorted_list_min_heap_union, list_make_min_heap, list_min_heap_insert, \
    list_heap_minimum, list_heap_extract_min, list_min_heap_union, list_min_heap_disjoint_union
from list_util import get_linked_list_keys


def assert_sorted_list(list_):
    if list_.head is None:
        return
    x = list_.head
    while x.next is not None:
        assert_that(x.key < x.next.key)
        x = x.next


class TestProblem10_2(TestCase):

    def test_mergeable_heap_on_sorted_list(self):
        _, elements1 = get_random_unique_array(min_size=0)
        _, elements2 = get_random_unique_array(min_size=0)

        heap1 = sorted_list_make_min_heap()
        heap2 = sorted_list_make_min_heap()

        for element in elements1:
            sorted_list_min_heap_insert(heap1, element)
        for element in elements2:
            sorted_list_min_heap_insert(heap2, element)
        assert_sorted_list(heap1)
        assert_sorted_list(heap2)

        expected_elements = elements1 + elements2

        if elements1:
            actual_min = sorted_list_heap_minimum(heap1)
            actual_extracted_min = sorted_list_heap_extract_min(heap1)
            expected_min = min(elements1)
            expected_elements.remove(expected_min)
            assert_that(actual_min, is_(equal_to(expected_min)))
            assert_that(actual_extracted_min, is_(equal_to(expected_min)))
            assert_sorted_list(heap1)
        else:
            assert_that(calling(sorted_list_heap_extract_min).with_args(heap1), raises(ValueError, 'heap underflow'))

        if elements2:
            actual_min = sorted_list_heap_minimum(heap2)
            actual_extracted_min = sorted_list_heap_extract_min(heap2)
            expected_min = min(elements2)
            expected_elements.remove(expected_min)
            assert_that(actual_min, is_(equal_to(expected_min)))
            assert_that(actual_extracted_min, is_(equal_to(expected_min)))
            assert_sorted_list(heap2)
        else:
            assert_that(calling(sorted_list_heap_extract_min).with_args(heap2), raises(ValueError, 'heap underflow'))

        merged_heap = sorted_list_min_heap_union(heap1, heap2)

        actual_elements = get_linked_list_keys(merged_heap)
        expected_elements = list(sorted(set(expected_elements)))
        assert_that(actual_elements, is_(equal_to(expected_elements)))
        assert_sorted_list(merged_heap)

    def test_mergeable_heap_on_unsorted_list(self):
        _, elements1 = get_random_unique_array(min_size=0)
        _, elements2 = get_random_unique_array(min_size=0)

        heap1 = list_make_min_heap()
        heap2 = list_make_min_heap()

        for element in elements1:
            list_min_heap_insert(heap1, element)
        for element in elements2:
            list_min_heap_insert(heap2, element)

        expected_elements = elements1 + elements2

        if elements1:
            actual_min = list_heap_minimum(heap1)
            actual_extracted_min = list_heap_extract_min(heap1)
            expected_min = min(elements1)
            expected_elements.remove(expected_min)
            assert_that(actual_min, is_(equal_to(expected_min)))
            assert_that(actual_extracted_min, is_(equal_to(expected_min)))
        else:
            assert_that(calling(list_heap_extract_min).with_args(heap1), raises(ValueError, 'heap underflow'))

        if elements2:
            actual_min = list_heap_minimum(heap2)
            actual_extracted_min = list_heap_extract_min(heap2)
            expected_min = min(elements2)
            expected_elements.remove(expected_min)
            assert_that(actual_min, is_(equal_to(expected_min)))
            assert_that(actual_extracted_min, is_(equal_to(expected_min)))
        else:
            assert_that(calling(list_heap_extract_min).with_args(heap2), raises(ValueError, 'heap underflow'))

        merged_heap = list_min_heap_union(heap1, heap2)

        actual_elements = get_linked_list_keys(merged_heap)
        expected_elements = list(sorted(set(expected_elements)))
        assert_that(actual_elements, contains_inanyorder(*expected_elements))

    def test_list_min_heap_disjoint_union(self):
        array, elements = get_random_unique_array(min_size=0)
        heap1_size = random.randint(0, len(elements))
        elements1 = array[1:heap1_size].elements
        elements2 = array[heap1_size + 1:array.length].elements

        heap1 = list_make_min_heap()
        heap2 = list_make_min_heap()

        for element in elements1:
            list_min_heap_insert(heap1, element)
        for element in elements2:
            list_min_heap_insert(heap2, element)

        merged_heap = list_min_heap_disjoint_union(heap1, heap2)

        actual_elements = get_linked_list_keys(merged_heap)
        assert_that(actual_elements, contains_inanyorder(*elements))
