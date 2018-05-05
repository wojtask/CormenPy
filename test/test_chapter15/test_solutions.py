import io
import itertools
import math
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
from chapter15.ex15_5_4 import effective_optimal_bst
from chapter15.pr15_1 import bitonic_tsp, print_bitonic_path
from chapter15.pr15_2 import break_lines, print_lines
from chapter15.pr15_3 import edit_distance, print_operations
from chapter15.pr15_4 import company_party, print_guests
from chapter15.pr15_6 import checkerboard, print_moves
from chapter15.pr15_7 import jobs_scheduling, print_schedule
from chapter15.textbook import matrix_chain_order, matrix_multiply, lcs_length, optimal_bst
from datastructures.array import Array
from datastructures.point_2d import Point2D
from datastructures.rooted_tree import RootedTree, Node
from test_chapter15.test_textbook import get_fastest_way_bruteforce, get_assembly_time_based_on_lines, \
    get_maximum_lcs_length_bruteforce, is_subsequence_of, get_probabilities_for_optimal_bst, \
    assert_root_array_consistent, get_minimum_bst_cost_bruteforce, get_bst_cost
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


def get_maximum_lis_length_bruteforce(sequence):
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


def get_shortest_bitonic_path_length_bruteforce(points):
    n = points.length
    min_length = math.inf
    for k in between(0, n - 2):
        for right_path in itertools.combinations(between(2, n - 1), k):
            left_path = [x for x in rbetween(n - 1, 2) if x not in right_path]
            path_length = get_path_length(points, [1] + list(right_path) + [n] + left_path + [1])
            min_length = min(min_length, path_length)
    return min_length


def get_path_length(points, path):
    return sum([euclidean_distance(points[path[i - 1]], points[path[i]]) for i in range(1, len(path))])


def get_path_length_from_bitonic_path(path):
    return sum([euclidean_distance(path[i], path[i + 1]) for i in range(-1, len(path) - 1)])


def euclidean_distance(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


def get_lines_break_minimum_cost_bruteforce(word_lengths, line_capacity, division=None, word_id=2):
    if division is None:
        division = [1]
    n = len(word_lengths)
    min_cost = get_cost_of_lines_break(division, word_lengths, line_capacity)
    while word_id <= n:
        min_cost = min(min_cost, get_lines_break_minimum_cost_bruteforce(
            word_lengths, line_capacity, division + [word_id], word_id + 1))
        word_id += 1
    return min_cost


def get_cost_of_lines_break(division, word_lengths, line_capacity):
    cost = 0
    for i in range(1, len(division)):
        line_length = get_line_length(division[i - 1], division[i] - 1, word_lengths)
        if line_length > line_capacity:
            return math.inf
        cost += (line_capacity - line_length) ** 3
    line_length = get_line_length(division[-1], len(word_lengths), word_lengths)
    if line_length > line_capacity:
        return math.inf
    return cost


def get_line_length(first_word_id, last_word_id, word_lengths):
    return sum([word_lengths[j - 1] for j in range(first_word_id, last_word_id + 1)]) + last_word_id - first_word_id


def get_edit_distance_bruteforce(x, y, cost, c=0, i=1, j=1):
    m = x.length
    n = y.length
    if i == m + 1 and j == n + 1:
        return c
    min_cost = math.inf
    if i <= m and j <= n and x[i] == y[j]:
        min_cost = min(min_cost, get_edit_distance_bruteforce(x, y, cost, c + cost['copy'], i + 1, j + 1))
    if i <= m and j <= n and x[i] != y[j]:
        min_cost = min(min_cost, get_edit_distance_bruteforce(x, y, cost, c + cost['replace'], i + 1, j + 1))
    if i <= m:
        min_cost = min(min_cost, get_edit_distance_bruteforce(x, y, cost, c + cost['delete'], i + 1, j))
    if j <= n:
        min_cost = min(min_cost, get_edit_distance_bruteforce(x, y, cost, c + cost['insert'], i, j + 1))
    if i < m and j < n and x[i] == y[j + 1] and x[i + 1] == y[j]:
        min_cost = min(min_cost, get_edit_distance_bruteforce(x, y, cost, c + cost['twiddle'], i + 2, j + 2))
    if i <= m and j == n + 1:
        min_cost = min(min_cost, get_edit_distance_bruteforce(x, y, cost, c + cost['kill'], m + 1, n + 1))
    return min_cost


def assert_valid_operations(operations, word1, word2):
    i = 1
    j = 1
    m = word1.length
    n = word2.length
    result = Array.indexed(1, n)
    for op in operations:
        if op == 'copy':
            result[j] = word1[i]
            i += 1
            j += 1
        elif op[:11] == 'replace by ':
            ch = op[11:]
            result[j] = ch
            i += 1
            j += 1
        elif op == 'delete':
            i += 1
        elif op[:7] == 'insert ':
            ch = op[7:]
            result[j] = ch
            j += 1
        elif op == 'twiddle':
            result[j] = word1[i + 1]
            result[j + 1] = word1[i]
            i += 2
            j += 2
        else:
            assert_that(op, is_(equal_to('kill')))
            assert_that(op, is_(equal_to(operations[-1])))
            i = m + 1
    assert_that(i, is_(equal_to(m + 1)))
    assert_that(result, is_(equal_to(word2)))


def get_operations_cost(operations, cost):
    c = 0
    for op in operations:
        if op[:7] == 'replace':
            c += cost['replace']
        elif op[:6] == 'insert':
            c += cost['insert']
        else:
            c += cost[op]
    return c


def get_company_hierarchy():
    company_size = random.randint(1, 20)
    boss = employee = None
    for i in range(company_size):
        new_employee = Node(None)
        new_employee.name = 'employee' + str(i + 1)
        new_employee.conv = random.randint(-20, 20)
        if i == 0:
            boss = new_employee
        elif i == 1 or random.randint(0, 1) == 0:
            employee.left_child = new_employee
        else:
            employee.right_sibling = new_employee
        employee = new_employee
    return RootedTree(boss)


def get_conviviality(employee, invited_employees):
    if employee is None:
        return 0
    conviviality = employee.conv if employee.name in invited_employees else 0
    conviviality += get_conviviality(employee.left_child, invited_employees)
    conviviality += get_conviviality(employee.right_sibling, invited_employees)
    return conviviality


def get_maximum_conviviality_bruteforce(hierarchy):
    return get_maximum_conviviality_from(hierarchy.root)


def get_maximum_conviviality_from(employee):
    conviviality_if_invited = employee.conv
    conviviality_if_uninvited = 0
    subordinate = employee.left_child
    while subordinate is not None:
        conviviality_if_invited += get_maximum_conviviality_from_uninvited(subordinate)
        conviviality_if_uninvited += get_maximum_conviviality_from(subordinate)
        subordinate = subordinate.right_sibling
    return max(conviviality_if_invited, conviviality_if_uninvited)


def get_maximum_conviviality_from_uninvited(employee):
    conviviality = 0
    subordinate = employee.left_child
    while subordinate is not None:
        conviviality += get_maximum_conviviality_from(subordinate)
        subordinate = subordinate.right_sibling
    return conviviality


def checkerboard_profit(profit, x, y):
    if x[0] != y[0] - 1 or abs(x[1] - y[1]) > 1:
        raise ValueError('invalid argument')
    return profit[x][y[1] - x[1] + 1]


def get_optimal_checkerboard_path_bruteforce(n, p):
    max_profit = -math.inf
    for j in between(1, n):
        max_profit = max(max_profit, get_optimal_checkerboard_subpath_bruteforce((1, j), n, p))
    return max_profit


def get_optimal_checkerboard_subpath_bruteforce(x, n, p):
    if x[0] == n:
        return 0
    y = (x[0] + 1, x[1])
    result = p(x, y) + get_optimal_checkerboard_subpath_bruteforce(y, n, p)
    if x[1] > 1:
        y = (x[0] + 1, x[1] - 1)
        result = max(result, p(x, y) + get_optimal_checkerboard_subpath_bruteforce(y, n, p))
    if x[1] < n:
        y = (x[0] + 1, x[1] + 1)
        result = max(result, p(x, y) + get_optimal_checkerboard_subpath_bruteforce(y, n, p))
    return result


def assert_squares_path(n, lines, profit, max_profit):
    comp = re.compile('\((\d+), (\d+)\)')
    actual_squares_path = [(int(comp.search(line).group(1)), int(comp.search(line).group(2))) for line in lines]
    assert_that(actual_squares_path, has_length(n))
    assert_that(actual_squares_path[0][0], is_(equal_to(1)))
    profit_from_path = 0
    for k in range(1, n):
        profit_from_path += checkerboard_profit(profit, actual_squares_path[k - 1], actual_squares_path[k])
    assert_that(profit_from_path, is_(equal_to(max_profit)))


def get_optimal_schedule_bruteforce(times, profits, deadlines):
    n = times.length
    max_profit = 0
    for m in between(1, n):
        for schedule in itertools.permutations(between(1, n), m):
            profit = get_schedule_total_profit(schedule, times, profits, deadlines)
            max_profit = max(max_profit, profit)
    return max_profit


def get_schedule_total_profit(schedule, times, profits, deadlines):
    total_time = 0
    profit = 0
    for job_id in schedule:
        total_time += times[job_id]
        if total_time <= deadlines[job_id]:
            profit += profits[job_id]
    return profit


class Solutions15Test(TestCase):

    def test_print_stations_(self):
        n = random.randint(1, 10)
        l = Array([Array.indexed(1, n), Array.indexed(1, n)])
        l[1, 1], l[2, 1] = 0, 0
        for i in between(2, n):
            l[1, i], l[2, i] = random.choice([(1, 1), (1, 2), (2, 2)])
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
        a = Array([get_random_array(min_size=n, max_size=n)[0],
                   get_random_array(min_size=n, max_size=n)[0]])
        t = Array([get_random_array(min_size=n - 1, max_size=n - 1)[0],
                   get_random_array(min_size=n - 1, max_size=n - 1)[0]])
        e, _ = get_random_array(min_size=2, max_size=2)
        x, _ = get_random_array(min_size=2, max_size=2)

        actual_assembly_time, lines, last_line = fastest_way_(a, t, e, x, n)

        expected_assembly_time = get_fastest_way_bruteforce(a, t, e, x, n)
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

        expected_maximum_length = get_maximum_lis_length_bruteforce(sequence)
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

        expected_maximum_length = get_maximum_lis_length_bruteforce(sequence)
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

    def test_effective_optimal_bst(self):
        p, q = get_probabilities_for_optimal_bst()

        e, root = effective_optimal_bst(p, q, p.length)

        assert_root_array_consistent(root)
        expected_minimum_cost = get_minimum_bst_cost_bruteforce(p, q)
        actual_minimum_cost = get_bst_cost(root, p, q)
        assert_that(actual_minimum_cost, expected_minimum_cost)

    def test_bitonic_tsp(self):
        n = random.randint(3, 12)
        xcoords, _ = get_random_array(min_size=n, max_size=n)
        ycoords, _ = get_random_array(min_size=n, max_size=n)
        points = Array([Point2D(x, y) for x, y in zip(xcoords, ycoords)])
        captured_output = io.StringIO()

        actual_path_lengths, optimal_paths = bitonic_tsp(points)
        with redirect_stdout(captured_output):
            print_bitonic_path(points, optimal_paths)

        expected_bitonic_path_length = get_shortest_bitonic_path_length_bruteforce(points)
        assert_that(actual_path_lengths[n, n], is_(close_to(expected_bitonic_path_length, .000001)))
        pattern = re.compile('\((\d+), (\d+)\)')
        actual_bitonic_path = [Point2D(int(pattern.match(point).group(1)), int(pattern.match(point).group(2)))
                               for point in captured_output.getvalue().splitlines()]
        assert_that(actual_bitonic_path, has_length(n))
        path_length_from_bitonic_path = get_path_length_from_bitonic_path(actual_bitonic_path)
        assert_that(path_length_from_bitonic_path, is_(close_to(expected_bitonic_path_length, .000001)))

    def test_break_lines(self):
        n = random.randint(1, 15)
        line_capacity = random.randint(5, 100)
        word_lengths, _ = get_random_array(min_size=n, max_size=n, min_value=1, max_value=line_capacity)
        captured_output = io.StringIO()

        actual_costs, words_division = break_lines(word_lengths, line_capacity)
        with redirect_stdout(captured_output):
            print_lines(words_division, n)

        expected_cost = get_lines_break_minimum_cost_bruteforce(word_lengths.elements, line_capacity)
        assert_that(actual_costs[n], is_(equal_to(expected_cost)))
        actual_lines_break = [int(first_word) for first_word in captured_output.getvalue().splitlines()]
        actual_cost_of_lines_break = get_cost_of_lines_break(actual_lines_break, word_lengths.elements, line_capacity)
        assert_that(actual_cost_of_lines_break, is_(equal_to(expected_cost)))

    def test_edit_distance(self):
        len1 = random.randint(0, 8)
        len2 = random.randint(0, 8)
        word1 = Array(''.join(random.choice('abcde') for _ in range(len1)))
        word2 = Array(''.join(random.choice('abcde') for _ in range(len2)))
        cost_insert = random.randint(0, 10)
        cost_delete = random.randint(0, 10)
        cost = {'copy': random.randint(0, max(10, cost_insert + cost_delete)),
                'replace': random.randint(0, max(10, cost_insert + cost_delete)),
                'insert': cost_insert,
                'delete': cost_delete,
                'twiddle': random.randint(0, 10),
                'kill': random.randint(0, 10)}
        captured_output = io.StringIO()

        actual_costs, actual_op, actual_left, actual_right = edit_distance(word1, word2, cost)
        with redirect_stdout(captured_output):
            print_operations(actual_op, actual_left, actual_right, len1, len2)

        expected_cost = get_edit_distance_bruteforce(word1, word2, cost)
        assert_that(actual_costs[len1, len2], is_(equal_to(expected_cost)))
        actual_operations = captured_output.getvalue().splitlines()
        assert_valid_operations(actual_operations, word1, word2)
        cost_of_operations = get_operations_cost(actual_operations, cost)
        assert_that(cost_of_operations, is_(equal_to(expected_cost)))

    def test_company_party(self):
        company_hierarchy = get_company_hierarchy()
        captured_output = io.StringIO()

        actual_maximum_conviviality = company_party(company_hierarchy.root)
        with redirect_stdout(captured_output):
            print_guests(company_hierarchy.root)

        expected_maximum_conviviality = get_maximum_conviviality_bruteforce(company_hierarchy)
        assert_that(actual_maximum_conviviality, is_(equal_to(expected_maximum_conviviality)))
        actual_output = captured_output.getvalue().splitlines()
        actual_maximum_conviviality = get_conviviality(company_hierarchy.root, actual_output)
        assert_that(actual_maximum_conviviality, is_(equal_to(expected_maximum_conviviality)))

    def test_checkerboard(self):
        n = random.randint(1, 8)
        # profit[i, j] contains a triple (a, b, c), where the profit of moving from square of coords (i, j):
        # to square of coords (i+1, j-1) is a, to square of coords (i+1, j) is b, to square of coords (i+1, j+1) is c,
        # where (i, j) means i-th row from the bottom and j-th column from the left
        profit = Array([Array.indexed(1, n) for _ in between(1, n - 1)])
        for i in between(1, n - 1):
            profit[i, 1] = (None, random.randint(-100, 100), random.randint(-100, 100))
            for j in between(2, n - 1):
                profit[i, j] = (random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100))
            profit[i, n] = (random.randint(-100, 100), random.randint(-100, 100), None)
        captured_output = io.StringIO()

        actual_maximum_profit, squares, last_square = checkerboard(n, lambda x, y: checkerboard_profit(profit, x, y))
        with redirect_stdout(captured_output):
            print_moves(squares, n, last_square)

        expected_maximum_profit = \
            get_optimal_checkerboard_path_bruteforce(n, lambda x, y: checkerboard_profit(profit, x, y))
        assert_that(actual_maximum_profit, is_(equal_to(expected_maximum_profit)))
        assert_squares_path(n, captured_output.getvalue().splitlines(), profit, expected_maximum_profit)

    def test_jobs_scheduling(self):
        n = random.randint(1, 8)
        times, times_elements = get_random_array(min_size=n, max_size=n, min_value=1, max_value=n)
        profits, profits_elements = get_random_array(min_size=n, max_size=n)
        deadlines_elements = [random.randint(times_elements[j], n ** 2 + 10) for j in range(n)]
        deadlines = Array(deadlines_elements)
        captured_output = io.StringIO()

        actual_max_profits, actual_schedule, sorted_job_ids = jobs_scheduling(times, profits, deadlines)
        with redirect_stdout(captured_output):
            print_schedule(actual_schedule, sorted_job_ids, times, deadlines, n, actual_schedule[0].length - 1)

        expected_max_profit = get_optimal_schedule_bruteforce(
            Array(times_elements), Array(profits_elements), Array(deadlines_elements))
        assert_that(actual_max_profits[actual_max_profits.length - 1], is_(equal_to(expected_max_profit)))
        scheduled_jobs = [int(re.search('a(\d)+', job).group(1)) for job in captured_output.getvalue().splitlines()]
        profit_from_schedule = get_schedule_total_profit(
            scheduled_jobs, Array(times_elements), Array(profits_elements), Array(deadlines_elements))
        assert_that(profit_from_schedule, is_(equal_to(expected_max_profit)))
