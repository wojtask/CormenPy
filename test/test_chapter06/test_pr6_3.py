import math
import random
from unittest import TestCase

from chapter06.pr6_3 import young_extract_min, youngify, young_insert, young_sort, young_search
from datastructures.array import Array
from datastructures.matrix import Matrix
from test_datastructures.array_util import random_int_array


def random_young_tableau(max_rows=5, max_columns=5, max_value=999):
    threshold = 0.95 * max_value  # all numbers greater than threshold will be transformed to math.inf
    rows = random.randint(1, max_rows)
    columns = random.randint(1, max_columns)
    row = [random.randint(0, max_value) for _ in range(columns)]  # the first row
    data = [sorted([x if x <= threshold else math.inf for x in row])]
    for i in range(1, rows):
        if data[i - 1][0] < math.inf:
            row = [random.randint(data[i - 1][0], max_value)]
        else:
            row = [math.inf]
        for j in range(1, columns):
            bound = max(row[j - 1], data[i - 1][j])
            if bound < math.inf:
                row.append(random.randint(bound, max_value))
            else:
                row.append(math.inf)
        data.append(sorted([x if x <= threshold else math.inf for x in row]))
    return Matrix(data), data


class Problem6_3Test(TestCase):
    def assert_young(self, matrix):
        m, n = matrix.rows, matrix.columns
        for j in range(2, n + 1):
            self.assertTrue(matrix[1, j] >= matrix[1, j - 1])
        for i in range(2, m + 1):
            self.assertTrue(matrix[i, 1] >= matrix[i - 1, 1])
            for j in range(2, n + 1):
                self.assertTrue(matrix[i, j] >= matrix[i, j - 1])
                self.assertTrue(matrix[i, j] >= matrix[i - 1, j])

    def test_young_extract_min(self):
        young, data = random_young_tableau()
        m, n = young.rows, young.columns
        # make sure the young tableau is not empty
        if young[1, 1] == math.inf:
            young[1, 1] = data[0][0] = random.randint(0, 999)

        actual_min = young_extract_min(young, m, n, 1, 1)

        self.assert_young(young)
        self.assertEqual(actual_min, min(min(row for row in data)))
        expected_data = [x for row in data for x in row]
        expected_data[expected_data.index(actual_min)] = math.inf
        actual_data = [x for row in young.data for x in row]
        self.assertEqual(sorted(expected_data), sorted(actual_data))

    def test_youngify(self):
        young, data = random_young_tableau()
        m, n = young.rows, young.columns
        # make sure the young tableau is not full
        if young[m, n] < math.inf:
            young[m, n] = data[m - 1][n - 1] = math.inf

        # randomly decrease value of randomly chosen element
        i = random.randint(1, m)
        j = random.randint(1, n)
        if young[i, j] < math.inf:
            young[i, j] = data[i - 1][j - 1] = random.randint(0, young[i, j])

        youngify(young, i, j)

        self.assert_young(young)
        expected_data = [x for row in data for x in row]
        actual_data = [x for row in young.data for x in row]
        self.assertEqual(sorted(expected_data), sorted(actual_data))

    def test_young_insert(self):
        young, data = random_young_tableau()
        m, n = young.rows, young.columns
        # make sure the young tableau is not full
        if young[m, n] < math.inf:
            young[m, n] = data[m - 1][n - 1] = math.inf

        new_key = random.randint(0, 999)

        young_insert(young, m, n, new_key)

        self.assert_young(young)
        expected_data = [x for row in data for x in row] + [new_key]
        actual_data = [x for row in young.data for x in row] + [math.inf]
        self.assertEqual(sorted(expected_data), sorted(actual_data))

    def test_young_sort(self):
        n = random.randint(1, 5)
        array, data = random_int_array(min_size=n * n, max_size=n * n)

        young_sort(array)

        expected_array = Array(sorted(data))
        self.assertEqual(array, expected_array)

    def test_young_search_positive(self):
        young, data = random_young_tableau(max_value=20)
        m, n = young.rows, young.columns
        v = random.randint(0, 20)

        actual_found = young_search(young, m, n, v)

        if v in [x for row in data for x in row]:
            self.assertTrue(actual_found)
        else:
            self.assertFalse(actual_found)
