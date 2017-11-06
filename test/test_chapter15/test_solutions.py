import io
import random
from contextlib import redirect_stdout
from unittest import TestCase

from hamcrest import *

from array_util import get_random_matrix
from chapter15.ex15_1_1 import print_stations_
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
