import io
import math
import random
from contextlib import redirect_stdout
from unittest import TestCase

from hamcrest import *

from chapter15.problem15_3 import edit_distance, print_operations, optimal_alignment
from datastructures.array import Array


def get_edit_distance_bruteforce(x, y, cost, i=1, j=1):
    m = x.length
    n = y.length
    if i == m + 1 and j == n + 1:
        return 0
    min_cost = math.inf
    if i <= m and j <= n and x[i] == y[j]:
        min_cost = min(min_cost, get_edit_distance_bruteforce(x, y, cost, i + 1, j + 1) + cost['copy'])
    if i <= m and j <= n and x[i] != y[j]:
        min_cost = min(min_cost, get_edit_distance_bruteforce(x, y, cost, i + 1, j + 1) + cost['replace'])
    if i <= m:
        min_cost = min(min_cost, get_edit_distance_bruteforce(x, y, cost, i + 1, j) + cost['delete'])
    if j <= n:
        min_cost = min(min_cost, get_edit_distance_bruteforce(x, y, cost, i, j + 1) + cost['insert'])
    if i < m and j < n and x[i] == y[j + 1] and x[i + 1] == y[j]:
        min_cost = min(min_cost, get_edit_distance_bruteforce(x, y, cost, i + 2, j + 2) + cost['twiddle'])
    if i <= m and j == n + 1:
        min_cost = min(min_cost, get_edit_distance_bruteforce(x, y, cost, m + 1, n + 1) + cost['kill'])
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


def get_optimal_alignment_bruteforce(x, y, i=1, j=1):
    m = x.length
    n = y.length
    if i == m + 1 and j == n + 1:
        return 0
    max_score = -math.inf
    if i <= m:
        max_score = max(max_score, get_optimal_alignment_bruteforce(x, y, i + 1, j) - 2)
    if j <= n:
        max_score = max(max_score, get_optimal_alignment_bruteforce(x, y, i, j + 1) - 2)
    if i <= m and j <= n:
        if x[i] == y[j]:
            max_score = max(max_score, get_optimal_alignment_bruteforce(x, y, i + 1, j + 1) + 1)
        else:
            max_score = max(max_score, get_optimal_alignment_bruteforce(x, y, i + 1, j + 1) - 1)
    return max_score


class TestProblem15_3(TestCase):

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

    def test_optimal_alignment(self):
        len1 = random.randint(0, 8)
        len2 = random.randint(0, 8)
        word1 = Array(''.join(random.choice('ACGT') for _ in range(len1)))
        word2 = Array(''.join(random.choice('ACGT') for _ in range(len2)))

        actual_score, _, _, _ = optimal_alignment(word1, word2)

        expected_score = get_optimal_alignment_bruteforce(word1, word2)
        assert_that(actual_score, is_(equal_to(expected_score)))
