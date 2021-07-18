import copy
import math
import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter06.problem6_3 import young_extract_min, youngify, young_insert, young_sort, young_search
from datastructures.matrix import Matrix
from util import between


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
    return Matrix(elements)


def assert_young_tableau(matrix):
    m, n = matrix.rows, matrix.columns
    for j in between(2, n):
        assert_that(matrix[1, j], is_(greater_than_or_equal_to(matrix[1, j - 1])))
    for i in between(2, m):
        assert_that(matrix[i, 1], is_(greater_than_or_equal_to(matrix[i - 1, 1])))
        for j in between(2, n):
            assert_that(matrix[i, j], is_(greater_than_or_equal_to(matrix[i, j - 1])))
            assert_that(matrix[i, j], is_(greater_than_or_equal_to(matrix[i - 1, j])))


def get_young_tableau_elements(young):
    return [x for row in young for x in row if x != math.inf]


class TestProblem6_3(TestCase):

    def test_young_extract_min(self):
        young = random_young_tableau()
        m, n = young.rows, young.columns
        # make sure the Young tableau is not empty
        if young[1, 1] == math.inf:
            young[1, 1] = random.randrange(1000)
        original = copy.deepcopy(young)

        actual_min = young_extract_min(young, m, n, 1, 1)

        assert_young_tableau(young)
        assert_that(actual_min, is_(equal_to(min(min(original)))))
        actual_elements = get_young_tableau_elements(young)
        expected_elements = get_young_tableau_elements(original)
        expected_elements.remove(actual_min)
        assert_that(actual_elements, contains_inanyorder(*expected_elements))

    def test_youngify(self):
        young = random_young_tableau()
        m, n = young.rows, young.columns
        # make sure the Young tableau is not full
        if young[m, n] < math.inf:
            young[m, n] = math.inf

        # randomly decrease the value of a randomly chosen element
        i = random.randint(1, m)
        j = random.randint(1, n)
        if young[i, j] < math.inf:
            young[i, j] = random.randint(0, young[i, j])
        original = copy.deepcopy(young)

        youngify(young, i, j)

        assert_young_tableau(young)
        actual_elements = get_young_tableau_elements(young)
        expected_elements = get_young_tableau_elements(original)
        assert_that(actual_elements, contains_inanyorder(*expected_elements))

    def test_young_insert(self):
        young = random_young_tableau()
        m, n = young.rows, young.columns
        # make sure the Young tableau is not full
        if young[m, n] < math.inf:
            young[m, n] = math.inf
        original = copy.deepcopy(young)

        new_key = random.randint(0, 999)

        young_insert(young, m, n, new_key)

        assert_young_tableau(young)
        actual_elements = get_young_tableau_elements(young)
        expected_elements = get_young_tableau_elements(original)
        expected_elements.append(new_key)
        assert_that(actual_elements, contains_inanyorder(*expected_elements))

    def test_young_sort(self):
        n = random.randint(1, 5)
        array = get_random_array(size=n * n)
        original = copy.deepcopy(array)

        young_sort(array)

        expected_array = original.sort()
        assert_that(array, is_(equal_to(expected_array)))

    def test_young_search(self):
        young = random_young_tableau(max_value=20)
        original = copy.deepcopy(young)
        m, n = young.rows, young.columns
        v = random.randint(0, 20)

        actual_found = young_search(young, m, n, v)

        if v in get_young_tableau_elements(young):
            assert_that(actual_found, is_(True))
        else:
            assert_that(actual_found, is_(False))
        assert_that(young, is_(equal_to(original)))
