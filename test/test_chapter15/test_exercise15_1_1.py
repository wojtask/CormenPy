import io
import random
from contextlib import redirect_stdout
from unittest import TestCase

from hamcrest import *

from chapter15.exercise15_1_1 import print_stations_increasing
from datastructures.array import Array
from util import between, rbetween


class TestExercise15_1_1(TestCase):

    def test_print_stations_increasing(self):
        n = random.randint(1, 10)
        l = Array.of(Array.indexed(1, n), Array.indexed(1, n))
        l[1, 1], l[2, 1] = 0, 0
        for i in between(2, n):
            l[1, i], l[2, i] = Array.of((1, 1), (1, 2), (2, 2)).random_choice()
        l.save_state()
        l[1].save_state()
        l[2].save_state()
        l_star = random.randint(1, 2)
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            print_stations_increasing(l, l_star, n)

        assert_that(l.is_modified(), is_(False))
        assert_that(l[1].is_modified(), is_(False))
        assert_that(l[2].is_modified(), is_(False))
        actual_output = Array(captured_output.getvalue().splitlines())
        expected_output = Array()
        i = l_star
        expected_output.append('line %d, station %d' % (i, n))
        for j in rbetween(n, 2):
            i = l[i, j]
            expected_output.append('line %d, station %d' % (i, j - 1))
        expected_output = Array(reversed(expected_output))
        assert_that(actual_output, is_(equal_to(expected_output)))
