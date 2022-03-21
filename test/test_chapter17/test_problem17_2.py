import copy
import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter17.problem17_2 import dynamic_binary_search, dynamic_binary_insert, dynamic_binary_delete
from datastructures.array import Array
from util import between


def _create_arrays():
    k = random.randint(1, 5)
    arrays = Array.indexed(0, k - 1)
    for i in between(0, k - 1):
        if random.randint(0, 1) == 0:
            arrays[i] = Array()
        else:
            arrays[i] = get_random_array(size=2 ** i, max_value=2 ** (k - 1)).sort()
    return arrays


class TestProblem17_2(TestCase):

    def test_dynamic_binary_search(self):
        arrays = _create_arrays()
        k = arrays.length
        element = random.randint(0, 2 ** (k - 1))

        p = dynamic_binary_search(arrays, element)

        if p:
            assert_that(arrays[p[0]][p[1]], is_(equal_to(element)))
        else:
            for i in between(0, k - 1):
                assert_that(element, not_(is_in(arrays[i])))

    def test_dynamic_binary_insert(self):
        arrays = _create_arrays()
        k = arrays.length
        element = random.randint(0, 2 ** (k - 1))
        elements_before = Array(x for arr in arrays for x in arr)
        # make sure there is a place for the new element
        if elements_before.length == 2 ** k - 1:
            elements_before.remove(arrays[0][1])
            arrays[0] = Array()

        dynamic_binary_insert(arrays, element)

        actual_elements_after = Array(x for arr in arrays for x in arr)
        expected_elements_after = elements_before + [element]
        assert_that(actual_elements_after, contains_inanyorder(*expected_elements_after))
        for i in between(0, k - 1):
            assert_that(arrays[i].length, is_(any_of(0, 2 ** i)))

    def test_dynamic_binary_delete(self):
        arrays = _create_arrays()
        k = arrays.length
        elements_before = Array(x for arr in arrays for x in arr)
        # make sure there is an element to remove
        if elements_before.length == 0:
            arrays[0] = Array(random.randint(0, 2 ** (k - 1)))
            elements_before.append(arrays[0][1])
        element = elements_before.random_choice()

        dynamic_binary_delete(arrays, element)

        actual_elements_after = Array(x for arr in arrays for x in arr)
        expected_elements_after = copy.deepcopy(elements_before)
        expected_elements_after.remove(element)
        assert_that(actual_elements_after, contains_inanyorder(*expected_elements_after))
        for i in between(0, k - 1):
            assert_that(arrays[i].length, is_(any_of(0, 2 ** i)))
