import math
import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter06.problem6_3 import young_extract_min, youngify, young_insert, young_sort, young_search
from datastructures.array import Array
from datastructures.matrix import Matrix


def random_young_tableau(max_value=999):
    threshold = 0.95 * max_value  # all numbers greater than threshold will be transformed to math.inf
    rows = random.randint(1, 5)
    columns = random.randint(1, 5)
    row = [random.randint(0, max_value) for _ in range(columns)]  # the first row
    elements = [sorted([x if x <= threshold else math.inf for x in row])]
    for i in range(1, rows):
        if elements[i - 1][0] < math.inf:
            row = [random.randint(elements[i - 1][0], max_value)]
        else:
            row = [math.inf]
        for j in range(1, columns):
            bound = max(row[j - 1], elements[i - 1][j])
            if bound < math.inf:
                row.append(random.randint(bound, max_value))
            else:
                row.append(math.inf)
        elements.append(sorted([x if x <= threshold else math.inf for x in row]))
    return Matrix(elements), elements


def assert_young_tableau(matrix):
    m, n = matrix.rows, matrix.columns
    for j in range(2, n + 1):
        assert_that(matrix[1, j], is_(greater_than_or_equal_to(matrix[1, j - 1])))
    for i in range(2, m + 1):
        assert_that(matrix[i, 1], is_(greater_than_or_equal_to(matrix[i - 1, 1])))
        for j in range(2, n + 1):
            assert_that(matrix[i, j], is_(greater_than_or_equal_to(matrix[i, j - 1])))
            assert_that(matrix[i, j], is_(greater_than_or_equal_to(matrix[i - 1, j])))


class TestProblem6_3(TestCase):

    def test_young_extract_min(self):
        young, elements = random_young_tableau()
        m, n = young.rows, young.columns
        # make sure the young tableau is not empty
        if young[1, 1] == math.inf:
            young[1, 1] = elements[0][0] = random.randrange(1000)

        actual_min = young_extract_min(young, m, n, 1, 1)

        assert_young_tableau(young)
        assert_that(actual_min, is_(equal_to(min(min(row for row in elements)))))
        actual_elements = [x for row in young.elements for x in row]
        expected_elements = [x for row in elements for x in row]
        expected_elements.remove(actual_min)
        expected_elements.append(math.inf)
        assert_that(actual_elements, contains_inanyorder(*expected_elements))

    def test_youngify(self):
        young, elements = random_young_tableau()
        m, n = young.rows, young.columns
        # make sure the young tableau is not full
        if young[m, n] < math.inf:
            young[m, n] = elements[m - 1][n - 1] = math.inf

        # randomly decrease value of randomly chosen element
        i = random.randint(1, m)
        j = random.randint(1, n)
        if young[i, j] < math.inf:
            young[i, j] = elements[i - 1][j - 1] = random.randint(0, young[i, j])

        youngify(young, i, j)

        assert_young_tableau(young)
        actual_elements = [x for row in young.elements for x in row]
        expected_elements = [x for row in elements for x in row]
        assert_that(actual_elements, contains_inanyorder(*expected_elements))

    def test_young_insert(self):
        young, elements = random_young_tableau()
        m, n = young.rows, young.columns
        # make sure the young tableau is not full
        if young[m, n] < math.inf:
            young[m, n] = elements[m - 1][n - 1] = math.inf

        new_key = random.randint(0, 999)

        young_insert(young, m, n, new_key)

        assert_young_tableau(young)
        actual_elements = [x for row in young.elements for x in row]
        expected_elements = [x for row in elements for x in row]
        expected_elements.remove(math.inf)
        expected_elements.append(new_key)
        assert_that(actual_elements, contains_inanyorder(*expected_elements))

    def test_young_sort(self):
        n = random.randint(1, 5)
        array, elements = get_random_array(min_size=n * n, max_size=n * n)

        young_sort(array)

        expected_array = Array(sorted(elements))
        assert_that(array, is_(equal_to(expected_array)))

    def test_young_search(self):
        young, elements = random_young_tableau(max_value=20)
        m, n = young.rows, young.columns
        v = random.randint(0, 20)

        actual_found = young_search(young, m, n, v)

        if v in [x for row in elements for x in row]:
            assert_that(actual_found, is_(True))
        else:
            assert_that(actual_found, is_(False))
