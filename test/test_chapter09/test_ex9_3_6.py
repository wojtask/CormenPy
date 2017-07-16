import random
from unittest import TestCase

from chapter09.ex9_3_6 import quantiles
from test.test_datastructures.array_util import random_unique_int_array


class Ex9_3_6Test(TestCase):
    def test_quantiles(self):
        array, data = random_unique_int_array()
        k = random.randint(1, array.length + 1)
        actual_quantiles = quantiles(array, 1, array.length, k)
        self.assertEqual(len(actual_quantiles), k - 1)
        if k > 1:
            self._assert_quantiles(actual_quantiles, data)

    def _assert_quantiles(self, actual_quantiles, data):
        quantiles_count = len(actual_quantiles)
        sorted_data = sorted(data)
        quantiles_indexes = sorted([sorted_data.index(quantile) for quantile in actual_quantiles])
        subarray_lengths = {quantiles_indexes[0]}
        for i in range(1, quantiles_count):
            subarray_lengths.add(quantiles_indexes[i] - quantiles_indexes[i - 1] - 1)
        # the subarrays can differ at most 1 so their lengths can be one of 2 possible values
        self.assertTrue(len(subarray_lengths) <= 2)
