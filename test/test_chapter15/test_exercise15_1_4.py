import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter15.exercise15_1_4 import fastest_way_
from datastructures.array import Array
from test_chapter15.test_textbook15_1 import get_fastest_way_bruteforce, get_assembly_time_based_on_lines


class TestExercise15_1_4(TestCase):

    def test_fastest_way_(self):
        n = random.randint(1, 10)
        a = Array.of(get_random_array(size=n), get_random_array(size=n))
        t = Array.of(get_random_array(size=n - 1), get_random_array(size=n - 1))
        e = get_random_array(size=2)
        x = get_random_array(size=2)

        actual_assembly_time, lines, last_line = fastest_way_(a, t, e, x, n)

        assert_that(a.is_modified(), is_(False))
        assert_that(t.is_modified(), is_(False))
        assert_that(e.is_modified(), is_(False))
        assert_that(x.is_modified(), is_(False))
        expected_assembly_time = get_fastest_way_bruteforce(a, t, e, x, n)
        assert_that(actual_assembly_time, is_(equal_to(expected_assembly_time)))
        expected_assembly_time = get_assembly_time_based_on_lines(lines, last_line, a, t, e, x, n)
        assert_that(actual_assembly_time, is_(equal_to(expected_assembly_time)))
