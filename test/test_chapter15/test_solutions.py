import io
import itertools
import random
import re
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
from chapter15.ex15_4_5 import lis_length, print_lis
from chapter15.ex15_4_6 import lis_length_
from chapter15.ex15_5_1 import construct_optimal_bst
from chapter15.textbook import matrix_chain_order, matrix_multiply, lcs_length, optimal_bst
from datastructures.array import Array
from test_chapter15.test_textbook import get_fastest_way_brute_force, get_assembly_time_based_on_lines, \
    get_maximum_lcs_length_bruteforce, is_subsequence_of, get_probabilities_for_optimal_bst
from util import rbetween, between


def get_matrix_product(A):
    n = A.length
    product = A[1]
    for i in between(2, n):
        product = matrix_multiply(product, A[i])
    return product


def is_monotonically_increasing(sequence):
    for i in between(1, len(sequence) - 1):
        if sequence[i] < sequence[i - 1]:
            return False
    return True


def get_maximum_lis_length_brute_force(sequence):
    max_length = 0
    for i in between(1, sequence.length):
        for subsequence in itertools.combinations(sequence, i):
            if is_monotonically_increasing(subsequence):
                max_length = len(subsequence)
    return max_length


def assert_optimal_bst_output(actual_output, root):
    n = root.length
    root_id = int(re.search('k(\d+) is the root', actual_output[0]).group(1))
    assert_that(root_id, is_(equal_to(root[1, n])))
    line_no = assert_left_child_output(actual_output, root, 1, root_id - 1, 1)
    line_no = assert_right_child_output(actual_output, root, root_id + 1, n, line_no + 1)
    assert_that(actual_output, has_length(line_no + 1))


def assert_left_child_output(actual_output, root, i, j, line_no):
    parent = j + 1
    comp = re.compile('([kd])(\d+) is the left child of k(\d+)')
    node_type = comp.search(actual_output[line_no]).group(1)
    node_id = int(comp.search(actual_output[line_no]).group(2))
    actual_parent = int(comp.search(actual_output[line_no]).group(3))
    assert_that(actual_parent, is_(equal_to(parent)))
    if i <= j:
        assert_that(node_type, is_(equal_to('k')))
        assert_that(node_id, is_(equal_to(root[i, j])))
        line_no = assert_left_child_output(actual_output, root, i, node_id - 1, line_no + 1)
        line_no = assert_right_child_output(actual_output, root, node_id + 1, j, line_no + 1)
    else:
        assert_that(node_type, is_(equal_to('d')))
        assert_that(node_id, is_(equal_to(j)))
    return line_no


def assert_right_child_output(actual_output, root, i, j, line_no):
    parent = i - 1
    comp = re.compile('([kd])(\d+) is the right child of k(\d+)')
    node_type = comp.search(actual_output[line_no]).group(1)
    node_id = int(comp.search(actual_output[line_no]).group(2))
    actual_parent = int(comp.search(actual_output[line_no]).group(3))
    assert_that(actual_parent, is_(equal_to(parent)))
    if i <= j:
        assert_that(node_type, is_(equal_to('k')))
        assert_that(node_id, is_(equal_to(root[i, j])))
        line_no = assert_left_child_output(actual_output, root, i, node_id - 1, line_no + 1)
        line_no = assert_right_child_output(actual_output, root, node_id + 1, j, line_no + 1)
    else:
        assert_that(node_type, is_(equal_to('d')))
        assert_that(node_id, is_(equal_to(j)))
    return line_no


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

        actual_assembly_time, lines, last_line = fastest_way_(a, t, e, x, n)

        expected_assembly_time = get_fastest_way_brute_force(a, t, e, x, n)
        assert_that(actual_assembly_time, is_(equal_to(expected_assembly_time)))
        expected_assembly_time = get_assembly_time_based_on_lines(lines, last_line, a, t, e, x, n)
        assert_that(actual_assembly_time, is_(equal_to(expected_assembly_time)))

    def test_matrix_chain_multiply(self):
        n = random.randint(1, 10)
        dimensions = Array([random.randint(1, 10) for _ in range(n + 1)], start=0)
        A = Array.indexed(1, n)
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

        expected_maximum_length = get_maximum_lcs_length_bruteforce(sequence1, sequence2)
        assert_that(actual_maximum_lengths[sequence1.length, sequence2.length], is_(equal_to(expected_maximum_length)))
        actual_lcs = captured_output.getvalue().splitlines()[0]
        assert_that(len(actual_lcs), is_(equal_to(expected_maximum_length)))
        assert_that(is_subsequence_of(actual_lcs, sequence1))
        assert_that(is_subsequence_of(actual_lcs, sequence2))

    def test_memoized_lcs_length(self):
        sequence1 = Array(''.join(random.choice('ABCD') for _ in range(random.randint(1, 10))))
        sequence2 = Array(''.join(random.choice('ABCD') for _ in range(random.randint(1, 10))))

        actual_maximum_length = memoized_lcs_length(sequence1, sequence2)

        expected_maximum_length = get_maximum_lcs_length_bruteforce(sequence1, sequence2)
        assert_that(actual_maximum_length, is_(equal_to(expected_maximum_length)))

    def test_lcs_length_(self):
        sequence1 = Array(''.join(random.choice('ABCD') for _ in range(random.randint(1, 10))))
        sequence2 = Array(''.join(random.choice('ABCD') for _ in range(random.randint(1, 10))))

        actual_maximum_length = lcs_length_(sequence1, sequence2)

        expected_maximum_length = get_maximum_lcs_length_bruteforce(sequence1, sequence2)
        assert_that(actual_maximum_length, is_(equal_to(expected_maximum_length)))

    def test_lcs_length__(self):
        sequence1 = Array(''.join(random.choice('ABCD') for _ in range(random.randint(1, 10))))
        sequence2 = Array(''.join(random.choice('ABCD') for _ in range(random.randint(1, 10))))

        actual_maximum_length = lcs_length__(sequence1, sequence2)

        expected_maximum_length = get_maximum_lcs_length_bruteforce(sequence1, sequence2)
        assert_that(actual_maximum_length, is_(equal_to(expected_maximum_length)))

    def test_lis_length(self):
        sequence, _ = get_random_array(max_value=10)
        captured_output = io.StringIO()

        actual_maximum_length, terms, last_term = lis_length(sequence)
        with redirect_stdout(captured_output):
            print_lis(terms, sequence, last_term)

        expected_maximum_length = get_maximum_lis_length_brute_force(sequence)
        assert_that(actual_maximum_length, is_(equal_to(expected_maximum_length)))
        actual_lis = [int(x) for x in captured_output.getvalue().splitlines()]
        assert_that(len(actual_lis), is_(equal_to(expected_maximum_length)))
        assert_that(is_subsequence_of(actual_lis, sequence))
        assert_that(is_monotonically_increasing(actual_lis))

    def test_lis_length_(self):
        sequence, _ = get_random_array(max_value=10)
        captured_output = io.StringIO()

        actual_maximum_length, terms, last_term = lis_length_(sequence)
        with redirect_stdout(captured_output):
            print_lis(terms, sequence, last_term)

        expected_maximum_length = get_maximum_lis_length_brute_force(sequence)
        assert_that(actual_maximum_length, is_(equal_to(expected_maximum_length)))
        actual_lis = [int(x) for x in captured_output.getvalue().splitlines()]
        assert_that(len(actual_lis), is_(equal_to(expected_maximum_length)))
        assert_that(is_subsequence_of(actual_lis, sequence))
        assert_that(is_monotonically_increasing(actual_lis))

    def test_construct_optimal_bst(self):
        p, q = get_probabilities_for_optimal_bst()
        _, root = optimal_bst(p, q, p.length)
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            construct_optimal_bst(root)

        actual_output = captured_output.getvalue().splitlines()
        assert_optimal_bst_output(actual_output, root)
