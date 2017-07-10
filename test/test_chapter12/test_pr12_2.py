import unittest

import io
from contextlib import redirect_stdout

from chapter12.pr12_2 import bit_strings_sort
from datastructures.array import Array


class Problem12_2Test(unittest.TestCase):
    def test_bit_strings_sort(self):
        data = ['1011', '10', '011', '100', '0']
        array = Array(data)
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            bit_strings_sort(array)
        self.assertEqual(['0', '011', '10', '100', '1011'], captured_output.getvalue().splitlines())
