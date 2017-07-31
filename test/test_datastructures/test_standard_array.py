from unittest import TestCase

from hamcrest import *

from datastructures.standard_array import StandardArray


class StandardArrayTest(TestCase):

    def setUp(self):
        self.array = StandardArray([4, 5, 1, 0, 2])

    def test_has_correct_length(self):
        assert_that(self.array.length, is_(equal_to(5)))

    def test_gets_element(self):
        assert_that(self.array[3], is_(equal_to(0)))

    def test_sets_element(self):
        self.array[2] = 3
        assert_that(self.array.elements[2], is_(equal_to(3)))

    def test_elements_are_copied(self):
        another_array = StandardArray(self.array.elements)
        another_array[2] = 100
        assert_that(self.array[2], is_(equal_to(1)))

    def test_gets_all_elements(self):
        actual_elements = [x for x in self.array]
        assert_that(actual_elements, is_(equal_to([4, 5, 1, 0, 2])))

    def test_gets_subarray(self):
        actual_subarray = self.array[1:3]
        expected_subarray = StandardArray([5, 1, 0])
        assert_that(actual_subarray, is_(equal_to(expected_subarray)))
