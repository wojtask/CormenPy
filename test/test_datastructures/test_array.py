from unittest import TestCase

from hamcrest import *

from datastructures.array import Array


class TestArray(TestCase):

    def setUp(self):
        self.array = Array.of(4, 5, 1, 0, 2)

    def test_has_correct_length(self):
        assert_that(self.array.length, is_(equal_to(5)))
        assert_that(self.array.is_modified(), is_(False))

    def test_gets_element(self):
        assert_that(self.array[3], is_(equal_to(1)))
        assert_that(self.array.is_modified(), is_(False))

    def test_sets_element(self):
        self.array[2] = 3
        assert_that(self.array.elements[1], is_(equal_to(3)))
        assert_that(self.array.is_modified(), is_(True))

    def test_elements_are_copied(self):
        another_array = Array(self.array.elements)
        another_array[2] = 100
        assert_that(self.array.is_modified(), is_(False))

    def test_gets_all_elements(self):
        assert_that([x for x in self.array], is_(equal_to([4, 5, 1, 0, 2])))
        assert_that(self.array.is_modified(), is_(False))

    def test_gets_infix_subarray(self):
        actual_subarray = self.array[3:4]
        expected_subarray = Array.of(1, 0)
        assert_that(actual_subarray, is_(equal_to(expected_subarray)))
        assert_that(self.array.is_modified(), is_(False))

    def test_gets_prefix_subarray(self):
        actual_subarray = self.array[:4]
        expected_subarray = Array.of(4, 5, 1, 0)
        assert_that(actual_subarray, is_(equal_to(expected_subarray)))
        assert_that(self.array.is_modified(), is_(False))

    def test_gets_suffix_subarray(self):
        actual_subarray = self.array[3:]
        expected_subarray = Array.of(1, 0, 2)
        assert_that(actual_subarray, is_(equal_to(expected_subarray)))
        assert_that(self.array.is_modified(), is_(False))

    def test_addressing_by_invalid_indexes(self):
        try:
            self.array[3:10]
        except IndexError:
            assert_that(self.array.is_modified(), is_(False))
            return
        self.fail()

    def test_instantiate_with_custom_start_index(self):
        array = Array.of(4, 5, 1, 0, 2, start=2)
        assert_that(array.length, is_(equal_to(5)))
        assert_that(array.start, is_(equal_to(2)))
        assert_that(array[4], is_(equal_to(1)))

    def test_create_empty_array_with_custom_indexes(self):
        array = Array.indexed(3, 7)
        assert_that(array.length, is_(equal_to(5)))
        assert_that(array.start, is_(equal_to(3)))
        assert_that(array[4], is_(none()))

    def test_get_index_of_an_element(self):
        actual_index = self.array.index(1)
        assert_that(actual_index, is_(equal_to(3)))
        assert_that(self.array.is_modified(), is_(False))

    def test_insert_at_specified_index(self):
        self.array.insert(3, 9)
        assert_that(self.array.elements[2], is_(equal_to(9)))
        assert_that(self.array.is_modified(), is_(True))

    def test_append_element(self):
        self.array.append(9)
        assert_that(self.array.elements[5], is_(equal_to(9)))
        assert_that(self.array.is_modified(), is_(True))

    def test_sort(self):
        self.array.sort()
        assert_that(self.array.elements, is_(equal_to([0, 1, 2, 4, 5])))
        assert_that(self.array.is_modified(), is_(True))

    def test_shuffle(self):
        self.array.shuffle()
        assert_that(self.array.elements, contains_inanyorder(0, 1, 2, 4, 5))
        assert_that(self.array.is_modified(), is_(True))

    def test_random_choice(self):
        element = self.array.random_choice()
        assert_that(element, is_in([0, 1, 2, 4, 5]))
        assert_that(self.array.is_modified(), is_(False))

    def test_extend(self):
        self.array.extend([8, 9])
        assert_that(self.array.elements, is_(equal_to([4, 5, 1, 0, 2, 8, 9])))
        assert_that(self.array.is_modified(), is_(True))

    def test_pop(self):
        self.array.pop(2)
        assert_that(self.array.elements, is_(equal_to([4, 1, 0, 2])))
        assert_that(self.array.is_modified(), is_(True))

    def test_save_state(self):
        self.array[2] = 3
        self.array.save_state()
        assert_that(self.array.is_modified(), is_(False))
