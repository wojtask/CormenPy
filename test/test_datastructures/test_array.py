import unittest

from datastructures.array import Array


class ArrayTest(unittest.TestCase):
    def setUp(self):
        self.array = Array([4, 5, 1, 0, 2])

    def test_has_correct_length(self):
        self.assertEqual(5, self.array.length)

    def test_gets_item(self):
        self.assertEqual(1, self.array[3])

    def test_sets_item(self):
        self.array[2] = 3
        self.assertEqual(3, self.array.data[1])

    def test_data_is_copied(self):
        another_array = Array(self.array.data)
        another_array[2] = 100
        self.assertEqual(5, self.array[2])

    def test_gets_all_items(self):
        elements = [x for x in self.array]
        self.assertEqual([4, 5, 1, 0, 2], elements)

    def test_gets_subarray(self):
        subarray = self.array[3:4]
        self.assertEqual(Array([1, 0]), subarray)
