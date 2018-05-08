import io
import random
from contextlib import redirect_stdout
from unittest import TestCase

from hamcrest import *

from chapter14.problem14_2 import josephus_simulate, josephus


class TestProblem14_2(TestCase):

    def test_josephus_simulate(self):
        n = random.randint(1, 20)
        m = random.randint(1, n)

        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            josephus_simulate(n, m)

        persons = list(range(1, n + 1))
        expected_permutation = []
        idx = 0
        while persons:
            idx = (idx + m) % len(persons)
            expected_permutation.append(persons.pop(idx))
        actual_permutation = [int(x) for x in captured_output.getvalue().splitlines()]
        assert_that(actual_permutation, is_(equal_to(expected_permutation)))

    def test_josephus(self):
        n = random.randint(1, 20)
        m = random.randint(1, n)

        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            josephus(n, m)

        persons = list(range(1, n + 1))
        expected_permutation = []
        idx = 0
        while persons:
            idx = (idx + m) % len(persons)
            expected_permutation.append(persons.pop(idx))
        actual_permutation = [int(x) for x in captured_output.getvalue().splitlines()]
        assert_that(actual_permutation, is_(equal_to(expected_permutation)))
