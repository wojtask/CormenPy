import io
import random
from contextlib import redirect_stdout
from unittest import TestCase

from hamcrest import *

from array_util import get_random_matrix, get_random_array
from chapter15.ex15_1_1 import print_stations_
from chapter15.ex15_1_4 import fastest_way_
from chapter15.ex15_2_2 import matrix_chain_multiply
from chapter15.ex15_4_2 import print_lcs_
from chapter15.ex15_4_3 import memoized_lcs_length
from chapter15.ex15_4_4 import lcs_length_, lcs_length__
from chapter15.textbook import matrix_chain_order, matrix_multiply, lcs_length
from datastructures.array import Array
from datastructures.standard_array import StandardArray
from test_chapter15.test_textbook import get_fastest_way_brute_force, get_assembly_time_based_on_lines, \
    get_maximum_lcs_length_brute_force, is_subsequence_of
from util import rbetween, between


def get_matrix_product(A):
    n = A.length
    product = A[1]
    for i in between(2, n):
        product = matrix_multiply(product, A[i])
    return product


class Solutions15Test(TestCase):

    def test_print_stations_(self):
        n = random.randint(1, 10)
        l, _ = get_random_matrix(2, n, min_value=1, max_value=2)
        l[1, 1] = l[2, 1] = 0
        l_star = random.randint(1, 2)
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            print_stations_(l, l_star, n)

        actual_output = captured_output.getvalue().splitlines()
        expected_output = []
        i = l_star
        expected_output.append('line ' + str(i) + ', station ' + str(n))
        for j in rbetween(n, 2):
            i = l[i, j]
            expected_output.append('line ' + str(i) + ', station ' + str(j - 1))
        expected_output.reverse()
        assert_that(actual_output, is_(equal_to(expected_output)))

    def test_fastest_way_(self):
        n = random.randint(1, 10)
        a, _ = get_random_matrix(2, n)
        t, _ = get_random_matrix(2, n - 1)
        e, _ = get_random_array(min_size=2, max_size=2)
        x, _ = get_random_array(min_size=2, max_size=2)

        actual_assembly_time, last_line, lines = fastest_way_(a, t, e, x, n)

        expected_assembly_time = get_fastest_way_brute_force(a, t, e, x, n)
        assert_that(actual_assembly_time, is_(equal_to(expected_assembly_time)))
        expected_assembly_time = get_assembly_time_based_on_lines(lines, last_line, a, t, e, x, n)
        assert_that(actual_assembly_time, is_(equal_to(expected_assembly_time)))

    def test_matrix_chain_multiply(self):
        n = random.randint(1, 10)
        dimensions = StandardArray([random.randint(1, 10) for _ in range(n + 1)])
        A = Array.of_length(n)
        for i in between(1, n):
            A[i], _ = get_random_matrix(dimensions[i - 1], dimensions[i])
        _, optimal_solution = matrix_chain_order(dimensions)

        actual_product = matrix_chain_multiply(A, optimal_solution, 1, n)

        expected_product = get_matrix_product(A)
        assert_that(actual_product, expected_product)

    def test_print_lcs_(self):
        sequence1 = Array(''.join(random.choice('ABCD') for _ in range(random.randint(1, 10))))
        sequence2 = Array(''.join(random.choice('ABCD') for _ in range(random.randint(1, 10))))
        captured_output = io.StringIO()

        actual_maximum_lengths, _ = lcs_length(sequence1, sequence2)
        with redirect_stdout(captured_output):
            print_lcs_(actual_maximum_lengths, sequence1, sequence2, sequence1.length, sequence2.length)
            print()  # a blank line after the output

        expected_maximum_length = get_maximum_lcs_length_brute_force(sequence1, sequence2)
        assert_that(actual_maximum_lengths[sequence1.length, sequence2.length], is_(equal_to(expected_maximum_length)))
        actual_lcs = captured_output.getvalue().splitlines()[0]
        assert_that(len(actual_lcs), is_(equal_to(expected_maximum_length)))
        assert_that(is_subsequence_of(actual_lcs, sequence1))
        assert_that(is_subsequence_of(actual_lcs, sequence2))

    def test_memoized_lcs_length(self):
        sequence1 = Array(''.join(random.choice('ABCD') for _ in range(random.randint(1, 10))))
        sequence2 = Array(''.join(random.choice('ABCD') for _ in range(random.randint(1, 10))))

        actual_maximum_length = memoized_lcs_length(sequence1, sequence2)

        expected_maximum_length = get_maximum_lcs_length_brute_force(sequence1, sequence2)
        assert_that(actual_maximum_length, is_(equal_to(expected_maximum_length)))

    def test_lcs_length_(self):
        sequence1 = Array(''.join(random.choice('ABCD') for _ in range(random.randint(1, 10))))
        sequence2 = Array(''.join(random.choice('ABCD') for _ in range(random.randint(1, 10))))

        actual_maximum_length = lcs_length_(sequence1, sequence2)

        expected_maximum_length = get_maximum_lcs_length_brute_force(sequence1, sequence2)
        assert_that(actual_maximum_length, is_(equal_to(expected_maximum_length)))

    def test_lcs_length__(self):
        sequence1 = Array(''.join(random.choice('ABCD') for _ in range(random.randint(1, 10))))
        sequence2 = Array(''.join(random.choice('ABCD') for _ in range(random.randint(1, 10))))

        actual_maximum_length = lcs_length__(sequence1, sequence2)

        expected_maximum_length = get_maximum_lcs_length_brute_force(sequence1, sequence2)
        assert_that(actual_maximum_length, is_(equal_to(expected_maximum_length)))
