import random
from unittest import TestCase

from chapter04.pr4_7 import monge_minimums
from datastructures.array import Array
from datastructures.matrix import Matrix


def random_monge_array(m, n):
    data = [[random.randrange(1000) for _ in range(n)]]  # the first row
    for i in range(1, m):
        row = [random.randrange(1000)]  # the first element in next row can be anything
        for j in range(1, n):
            upper_bound = row[j - 1] + data[i - 1][j] - data[i - 1][j - 1]  # but later elements should be bounded
            row.append(random.randrange(upper_bound - 100, upper_bound + 1))
        data.append(row)
    return data


class Problem4_7Test(TestCase):
    def test_monge_minimums(self):
        m = random.randint(1, 10)
        n = random.randint(1, 10)
        monge_data = random_monge_array(m, n)
        monge_array = Matrix(monge_data)
        actual_minimums = monge_minimums(monge_array)
        expected_minimums = Array([min(row) for row in monge_data])
        self.assertEqual(actual_minimums, expected_minimums)
