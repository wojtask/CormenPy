import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter15.exercise15_1_4 import fastest_way_
from datastructures.array import Array
from util import rbetween


def get_other_line(current_line):
    return current_line % 2 + 1


def get_fastest_way_bruteforce(a, t, e, x, n):
    return min(e[1] + get_fastest_way_bruteforce_from(a, t, x, 1, n, 1),
               e[2] + get_fastest_way_bruteforce_from(a, t, x, 1, n, 2))


def get_fastest_way_bruteforce_from(a, t, x, pos, n, line):
    if pos == n:
        return a[line, n] + x[line]
    return min(a[line, pos] + get_fastest_way_bruteforce_from(a, t, x, pos + 1, n, line),
               a[line, pos] + t[line, pos] + get_fastest_way_bruteforce_from(a, t, x, pos + 1, n, get_other_line(line)))


def get_assembly_time_based_on_lines(lines, last_line, a, t, e, x, n):
    i = last_line
    assembly_time = x[i]
    for j in rbetween(n, 2):
        assembly_time += a[i, j]
        if i != lines[i, j]:
            i = lines[i, j]
            assembly_time += t[i, j - 1]
    assembly_time += a[i, 1] + e[i]
    return assembly_time


class TestExercise15_1_4(TestCase):

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
