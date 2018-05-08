from unittest import TestCase

from hamcrest import *

from datastructures.array import Array


class TestArray(TestCase):

    def setUp(self):
        self.array = Array([4, 5, 1, 0, 2])

    def test_has_correct_length(self):
        assert_that(self.array.length, is_(equal_to(5)))

    def test_gets_element(self):
        assert_that(self.array[3], 1)

    def test_sets_element(self):
        self.array[2] = 3
        assert_that(self.array.elements[1], is_(equal_to(3)))

    def test_elements_are_copied(self):
        another_array = Array(self.array.elements)
        another_array[2] = 100
        assert_that(self.array[2], is_(equal_to(5)))

    def test_gets_all_elements(self):
        actual_elements = [x for x in self.array]
        assert_that(actual_elements, is_(equal_to([4, 5, 1, 0, 2])))

    def test_gets_subarray(self):
        actual_subarray = self.array[3:4]
        expected_subarray = Array([1, 0])
        assert_that(actual_subarray, is_(equal_to(expected_subarray)))

    def test_instantiate_with_custom_start_index(self):
        array = Array([4, 5, 1, 0, 2], start=2)
        assert_that(array.length, is_(equal_to(5)))
        assert_that(array.start, is_(equal_to(2)))
        assert_that(array[4], is_(equal_to(1)))

    def test_create_empty_array_with_custom_indexes(self):
        array = Array.indexed(3, 7)
        assert_that(array.length, is_(equal_to(5)))
        assert_that(array.start, is_(equal_to(3)))
        assert_that(array[4], is_(none()))
