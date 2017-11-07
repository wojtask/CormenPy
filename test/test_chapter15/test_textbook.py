import io
import math
import random
from contextlib import redirect_stdout
from unittest import TestCase

import numpy
from hamcrest import *

from array_util import get_random_matrix, get_random_array
from chapter15.textbook import fastest_way, print_stations, matrix_multiply, matrix_chain_order, print_optimal_parens
from datastructures.matrix import Matrix
from datastructures.standard_array import StandardArray
from util import rbetween, between


def get_other_line(current_line):
    return current_line % 2 + 1


def get_fastest_way_brute_force_from(a, t, x, pos, n, line):
    if pos == n:
        return a[line, n] + x[line]

    return min(a[line, pos]
               + get_fastest_way_brute_force_from(a, t, x, pos + 1, n, line),
               a[line, pos] + t[line, pos]
               + get_fastest_way_brute_force_from(a, t, x, pos + 1, n, get_other_line(line)))


def get_fastest_way_brute_force(a, t, e, x, n):
    return min(e[1] + get_fastest_way_brute_force_from(a, t, x, 1, n, 1),
               e[2] + get_fastest_way_brute_force_from(a, t, x, 1, n, 2))


def get_assembly_time_based_on_lines(lines, last_line, a, t, e, x, n):
    i = last_line
    assembly_time = x[i]
    for j in rbetween(n, 2):
        assembly_time += a[i, j]
        if i != lines[i, j]:
            i = lines[i, j]
            assembly_time += t[i, j - 1]
    assembly_time += a[i, 1] + e[i]
    return assembly_time


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


def get_matrix_product_cost_based_on_solution(solution, dimensions, i, j):
    if i == j:
        return 0
    k = solution[i, j]
    return get_matrix_product_cost_based_on_solution(solution, dimensions, i, k) \
           + get_matrix_product_cost_based_on_solution(solution, dimensions, k + 1, j) \
           + dimensions[i - 1] * dimensions[k] * dimensions[j]


def get_optimal_parens_brute_force(s, i, j):
    if i == j:
        return 'A' + str(i)
    return '(' + get_optimal_parens_brute_force(s, i, s[i, j]) + get_optimal_parens_brute_force(s, s[i, j] + 1, j) + ')'


class Textbook15Test(TestCase):
    def test_fastest_way(self):
        n = random.randint(1, 10)
        a, _ = get_random_matrix(2, n)
        t, _ = get_random_matrix(2, n - 1)
        e, _ = get_random_array(min_size=2, max_size=2)
        x, _ = get_random_array(min_size=2, max_size=2)

        actual_assembly_time, last_line, lines = fastest_way(a, t, e, x, n)

        expected_assembly_time = get_fastest_way_brute_force(a, t, e, x, n)
        assert_that(actual_assembly_time, is_(equal_to(expected_assembly_time)))
        expected_assembly_time = get_assembly_time_based_on_lines(lines, last_line, a, t, e, x, n)
        assert_that(actual_assembly_time, is_(equal_to(expected_assembly_time)))

    def test_print_stations(self):
        n = random.randint(1, 10)
        l, _ = get_random_matrix(2, n, min_value=1, max_value=2)
        l[1, 1] = l[2, 1] = 0
        l_star = random.randint(1, 2)
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            print_stations(l, l_star, n)

        actual_output = captured_output.getvalue().splitlines()
        expected_output = []
        i = l_star
        expected_output.append('line ' + str(i) + ', station ' + str(n))
        for j in rbetween(n, 2):
            i = l[i, j]
            expected_output.append('line ' + str(i) + ', station ' + str(j - 1))
        assert_that(actual_output, is_(equal_to(expected_output)))

    def test_matrix_multiply(self):
        rows1 = random.randint(1, 3)
        columns1 = random.randint(1, 3)
        rows2 = random.randint(1, 3)
        columns2 = random.randint(1, 3)
        matrix1, elements1 = get_random_matrix(rows1, columns1)
        matrix2, elements2 = get_random_matrix(rows2, columns2)

        if columns1 != rows2:
            assert_that(calling(matrix_multiply).with_args(matrix1, matrix2),
                        raises(RuntimeError, 'incompatible dimensions'))
        else:
            actual_product = matrix_multiply(matrix1, matrix2)
            assert_that(actual_product.rows, is_(equal_to(rows1)))
            assert_that(actual_product.columns, is_(equal_to(columns2)))
            expected_product = numpy.dot(elements1, elements2)
            assert_that(actual_product.elements, is_(equal_to(expected_product.tolist())))

    def test_matrix_chain_order(self):
        n = random.randint(1, 10)
        dimensions = StandardArray([random.randint(1, 999) for _ in range(n + 1)])

        actual_minimum_costs, optimal_solution = matrix_chain_order(dimensions)

        expected_minimum_cost = get_minimum_matrix_product_cost(dimensions, 1, n)
        assert_that(actual_minimum_costs[1, n], is_(equal_to(expected_minimum_cost)))
        expected_minimum_cost = get_matrix_product_cost_based_on_solution(optimal_solution, dimensions, 1, n)
        assert_that(actual_minimum_costs[1, n], is_(equal_to(expected_minimum_cost)))

    def test_print_optimal_parens(self):
        n = random.randint(1, 10)
        s = Matrix.of_dimensions(n, n)
        for i in between(1, n - 1):
            for j in between(i + 1, n):
                s[i, j] = random.randint(i, j - 1)
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            print_optimal_parens(s, 1, n)

        actual_output = captured_output.getvalue().splitlines()[0]
        expected_output = get_optimal_parens_brute_force(s, 1, n)
        assert_that(actual_output, is_(equal_to(expected_output)))
