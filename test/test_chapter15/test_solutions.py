import io
import random
from contextlib import redirect_stdout
from unittest import TestCase

from hamcrest import *

from array_util import get_random_matrix, get_random_array
from chapter15.ex15_1_1 import print_stations_
from chapter15.ex15_1_4 import effective_fastest_way
from test_chapter15.test_textbook import get_fastest_way_brute_force, get_assembly_time_based_on_lines
from util import rbetween


class Solutions14Test(TestCase):

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

    def test_effective_fastest_way(self):
        n = random.randint(1, 10)
        a, _ = get_random_matrix(2, n)
        t, _ = get_random_matrix(2, n - 1)
        e, _ = get_random_array(min_size=2, max_size=2)
        x, _ = get_random_array(min_size=2, max_size=2)

        actual_assembly_time, last_line, lines = effective_fastest_way(a, t, e, x, n)

        expected_assembly_time = get_fastest_way_brute_force(a, t, e, x, n)
        assert_that(actual_assembly_time, is_(equal_to(expected_assembly_time)))
        expected_assembly_time = get_assembly_time_based_on_lines(lines, last_line, a, t, e, x, n)
        assert_that(actual_assembly_time, is_(equal_to(expected_assembly_time)))
