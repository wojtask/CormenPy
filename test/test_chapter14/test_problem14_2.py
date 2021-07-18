import io
import random
from contextlib import redirect_stdout
from unittest import TestCase

from hamcrest import *

from chapter14.problem14_2 import josephus_simulate, josephus
from datastructures.array import Array
from util import between


class TestProblem14_2(TestCase):

    def test_josephus_simulate(self):
        n = random.randint(1, 20)
        m = random.randint(1, n)

        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            josephus_simulate(n, m)

        persons = Array(between(1, n))
        expected_permutation = Array()
        idx = 0
        while persons:
            idx = (idx + m) % persons.length
            expected_permutation.append(persons.pop(idx + 1))
        actual_permutation = Array(int(x) for x in captured_output.getvalue().splitlines())
        assert_that(actual_permutation, is_(equal_to(expected_permutation)))

    def test_josephus(self):
        n = random.randint(1, 20)
        m = random.randint(1, n)

        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            josephus(n, m)

        persons = Array(between(1, n))
        expected_permutation = Array()
        idx = 0
        while persons:
            idx = (idx + m) % persons.length
            expected_permutation.append(persons.pop(idx + 1))
        actual_permutation = Array(int(x) for x in captured_output.getvalue().splitlines())
        assert_that(actual_permutation, is_(equal_to(expected_permutation)))
