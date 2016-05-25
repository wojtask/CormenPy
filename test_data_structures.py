import unittest

from data_structures import Array


class ArrayTest(unittest.TestCase):
    def setUp(self):
        self.array = Array(5)
        self.array.array = [4, 5, 1, 0, 2]

    def test_has_correct_length(self):
        self.assertEqual(5, self.array.length)

    def test_gets_item(self):
        self.assertEqual(1, self.array[3])

    def test_sets_item(self):
        self.array[2] = 3
        self.assertEqual(3, self.array.array[1])

if __name__ == '__main__':
    unittest.main()
