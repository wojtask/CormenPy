import io
import math
import random
from contextlib import redirect_stdout
from unittest import TestCase

import numpy
from hamcrest import *

from array_util import get_random_array
from chapter15.textbook15_2 import matrix_multiply, matrix_chain_order, print_optimal_parens
from datastructures.array import Array
from datastructures.matrix import Matrix
from util import between


def get_random_matrix(rows, columns):
    elements = [[random.randint(0, 999) for _ in between(1, columns)] for _ in between(1, rows)]
    return Matrix(elements)


def get_minimum_matrix_product_cost(dimensions, i, j):
    if i == j:
        return 0
    minimum_cost = math.inf
    for k in between(i, j - 1):
        cost = get_minimum_matrix_product_cost(dimensions, i, k) \
               + get_minimum_matrix_product_cost(dimensions, k + 1, j) \
               + dimensions[i - 1] * dimensions[k] * dimensions[j]
        minimum_cost = min(cost, minimum_cost)
    return minimum_cost


def get_matrix_product_cost_from_solution(solution, dimensions, i, j):
    if i == j:
        return 0
    k = solution[i, j]
    return get_matrix_product_cost_from_solution(solution, dimensions, i, k) + \
        get_matrix_product_cost_from_solution(solution, dimensions, k + 1, j) + \
        dimensions[i - 1] * dimensions[k] * dimensions[j]


def get_optimal_parens_bruteforce(s, i, j):
    if i == j:
        return 'A' + str(i)
    return '(' + get_optimal_parens_bruteforce(s, i, s[i, j]) + get_optimal_parens_bruteforce(s, s[i, j] + 1, j) + ')'


class TestTextbook15_2(TestCase):

    def test_matrix_multiply(self):
        rows1 = random.randint(1, 3)
        columns1 = random.randint(1, 3)
        rows2 = random.randint(1, 3)
        columns2 = random.randint(1, 3)
        matrix1 = get_random_matrix(rows1, columns1)
        matrix2 = get_random_matrix(rows2, columns2)

        if columns1 != rows2:
            assert_that(calling(matrix_multiply).with_args(matrix1, matrix2),
                        raises(ValueError, 'incompatible dimensions'))
        else:
            actual_product = matrix_multiply(matrix1, matrix2)
            assert_that(actual_product.rows, is_(equal_to(rows1)))
            assert_that(actual_product.columns, is_(equal_to(columns2)))
            expected_product = numpy.dot(matrix1.elements, matrix2.elements)
            assert_that(actual_product.elements, is_(equal_to(expected_product.tolist())))

    def test_matrix_chain_order(self):
        n = random.randint(1, 10)
        dimensions = get_random_array(size=n + 1, start=0)

        actual_minimum_costs, optimal_solution = matrix_chain_order(dimensions)

        expected_minimum_cost = get_minimum_matrix_product_cost(dimensions, 1, n)
        assert_that(actual_minimum_costs[1, n], is_(equal_to(expected_minimum_cost)))
        expected_minimum_cost = get_matrix_product_cost_from_solution(optimal_solution, dimensions, 1, n)
        assert_that(actual_minimum_costs[1, n], is_(equal_to(expected_minimum_cost)))

    def test_print_optimal_parens(self):
        n = random.randint(1, 10)
        s = Array(Array.indexed(1, n) for _ in between(1, n))
        for i in between(1, n - 1):
            for j in between(i + 1, n):
                s[i, j] = random.randint(i, j - 1)
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            print_optimal_parens(s, 1, n)

        actual_output = Array(captured_output.getvalue().splitlines()[0])
        expected_output = Array(get_optimal_parens_bruteforce(s, 1, n))
        assert_that(actual_output, is_(equal_to(expected_output)))
