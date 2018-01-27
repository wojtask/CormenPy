import io
import itertools
import math
import random
from contextlib import redirect_stdout
from unittest import TestCase

import numpy
from hamcrest import *

from array_util import get_random_matrix, get_random_array
from chapter15.textbook import fastest_way, print_stations, matrix_multiply, matrix_chain_order, print_optimal_parens, \
    recursive_matrix_chain, memoized_matrix_chain, lcs_length, print_lcs, optimal_bst
from datastructures.array import Array
from datastructures.matrix import Matrix
from util import rbetween, between


def get_other_line(current_line):
    return current_line % 2 + 1


def get_fastest_way_bruteforce(a, t, e, x, n):
    return min(e[1] + get_fastest_way_bruteforce_from(a, t, x, 1, n, 1),
               e[2] + get_fastest_way_bruteforce_from(a, t, x, 1, n, 2))


def get_fastest_way_bruteforce_from(a, t, x, pos, n, line):
    if pos == n:
        return a[line, n] + x[line]
    return min(a[line, pos] + get_fastest_way_bruteforce_from(a, t, x, pos + 1, n, line),
               a[line, pos] + t[line, pos] + get_fastest_way_bruteforce_from(a, t, x, pos + 1, n, get_other_line(line)))


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


def is_subsequence_of(subsequence, sequence):
    pos = 0
    for c in subsequence:
        try:
            pos += sequence.elements[pos:].index(c) + 1
        except ValueError:
            return False
    return True


def get_maximum_lcs_length_bruteforce(sequence1, sequence2):
    max_length = 0
    for i in between(1, min(sequence1.length, sequence2.length)):
        for subsequence in itertools.combinations(sequence1, i):
            if is_subsequence_of(subsequence, sequence2):
                max_length = len(subsequence)
    return max_length


def get_nwp_iteratively(b, sequence):
    result = ''
    i = b.rows
    j = b.columns
    while i > 0 and j > 0:
        if b[i, j] == '↖':
            result += sequence[i]
            i -= 1
            j -= 1
        elif b[i, j] == '↑':
            i -= 1
        else:
            j -= 1
    return result[::-1]


def get_probabilities_for_optimal_bst():
    n = random.randint(1, 10)
    p, _ = get_random_array(min_size=n, max_size=n)
    q, _ = get_random_array(min_size=n + 1, max_size=n + 1)
    q.start = 0
    total = sum([x for x in p.elements + q.elements])
    for i in between(1, n):
        p[i] /= total
    for i in between(0, n):
        q[i] /= total
    return p, q


def assert_root_array_consistent(root):
    n = root.length
    for i in between(1, n):
        for j in between(i, n):
            assert_that(root[i, j], is_(greater_than_or_equal_to(i)))
            assert_that(root[i, j], is_(less_than_or_equal_to(j)))


def get_bst_cost(root, p, q):
    return get_bst_subtree_cost(root, p, q, 0, 1, p.length)


def get_bst_subtree_cost(root, p, q, d, i, j):
    if i > j:
        return (d + 1) * q[j]
    return (d + 1) * p[root[i, j]] + \
        get_bst_subtree_cost(root, p, q, d + 1, i, root[i, j] - 1) + \
        get_bst_subtree_cost(root, p, q, d + 1, root[i, j] + 1, j)


def get_minimum_bst_cost_bruteforce(p, q):
    return get_minimum_subtree_cost_bruteforce(p, q, 1, p.length, 0)


def get_minimum_subtree_cost_bruteforce(p, q, i, j, d):
    if i > j:
        return (d + 1) * q[j]
    min_cost = math.inf
    for k in between(i, j):
        cost = (d + 1) * p[k] + \
               get_minimum_subtree_cost_bruteforce(p, q, i, k - 1, d + 1) + \
               get_minimum_subtree_cost_bruteforce(p, q, k + 1, j, d + 1)
        min_cost = min(min_cost, cost)
    return min_cost


class Textbook15Test(TestCase):

    def test_fastest_way(self):
        n = random.randint(1, 10)
        a, _ = get_random_matrix(2, n)
        t, _ = get_random_matrix(2, n - 1)
        e, _ = get_random_array(min_size=2, max_size=2)
        x, _ = get_random_array(min_size=2, max_size=2)

        actual_assembly_time, lines, last_line = fastest_way(a, t, e, x, n)

        expected_assembly_time = get_fastest_way_bruteforce(a, t, e, x, n)
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
        dimensions = Array([random.randint(1, 999) for _ in range(n + 1)], start=0)

        actual_minimum_costs, optimal_solution = matrix_chain_order(dimensions)

        expected_minimum_cost = get_minimum_matrix_product_cost(dimensions, 1, n)
        assert_that(actual_minimum_costs[1, n], is_(equal_to(expected_minimum_cost)))
        expected_minimum_cost = get_matrix_product_cost_from_solution(optimal_solution, dimensions, 1, n)
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
        expected_output = get_optimal_parens_bruteforce(s, 1, n)
        assert_that(actual_output, is_(equal_to(expected_output)))

    def test_recursive_matrix_chain(self):
        n = random.randint(1, 10)
        dimensions = Array([random.randint(1, 999) for _ in range(n + 1)], start=0)
        m = Matrix.of_dimensions(n, n)

        actual_minimum_cost = recursive_matrix_chain(dimensions, m, 1, n)

        expected_minimum_cost = get_minimum_matrix_product_cost(dimensions, 1, n)
        assert_that(actual_minimum_cost, is_(equal_to(expected_minimum_cost)))

    def test_memoized_matrix_chain(self):
        n = random.randint(1, 10)
        dimensions = Array([random.randint(1, 999) for _ in range(n + 1)], start=0)

        actual_minimum_cost = memoized_matrix_chain(dimensions)

        expected_minimum_cost = get_minimum_matrix_product_cost(dimensions, 1, n)
        assert_that(actual_minimum_cost, is_(equal_to(expected_minimum_cost)))

    def test_lcs_length(self):
        sequence1 = Array(''.join(random.choice('ABCD') for _ in range(random.randint(1, 10))))
        sequence2 = Array(''.join(random.choice('ABCD') for _ in range(random.randint(1, 10))))
        captured_output = io.StringIO()

        actual_maximum_lengths, optimal_solution = lcs_length(sequence1, sequence2)
        with redirect_stdout(captured_output):
            print_lcs(optimal_solution, sequence1, sequence1.length, sequence2.length)
            print()  # a blank line after the output

        expected_maximum_length = get_maximum_lcs_length_bruteforce(sequence1, sequence2)
        assert_that(actual_maximum_lengths[sequence1.length, sequence2.length], is_(equal_to(expected_maximum_length)))
        actual_lcs = captured_output.getvalue().splitlines()[0]
        assert_that(len(actual_lcs), is_(equal_to(expected_maximum_length)))
        assert_that(is_subsequence_of(actual_lcs, sequence1))
        assert_that(is_subsequence_of(actual_lcs, sequence2))

    def test_optimal_bst(self):
        p, q = get_probabilities_for_optimal_bst()

        e, root = optimal_bst(p, q, p.length)

        assert_root_array_consistent(root)
        expected_minimum_cost = get_minimum_bst_cost_bruteforce(p, q)
        actual_minimum_cost = get_bst_cost(root, p, q)
        assert_that(actual_minimum_cost, expected_minimum_cost)
