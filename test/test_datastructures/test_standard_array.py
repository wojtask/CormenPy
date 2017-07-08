import unittest

from datastructures.standard_array import StandardArray


class StandardArrayTest(unittest.TestCase):
    def setUp(self):
        self.array = StandardArray([4, 5, 1, 0, 2])

    def test_has_correct_length(self):
        self.assertEqual(5, self.array.length)

    def test_gets_item(self):
        self.assertEqual(0, self.array[3])

    def test_sets_item(self):
        self.array[2] = 3
        self.assertEqual(3, self.array.data[2])

    def test_data_is_copied(self):
        another_array = StandardArray(self.array.data)
        another_array[2] = 100
        self.assertEqual(1, self.array[2])

    def test_gets_all_items(self):
        elements = [x for x in self.array]
        self.assertEqual([4, 5, 1, 0, 2], elements)
