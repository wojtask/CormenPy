import itertools
import math
import random
import re
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter16.textbook16_5 import tasks_scheduling
from datastructures.array import Array
from util import between


def decode_tasks(tasks):
    return Array([int(re.search('a(\d+)', task).group(1)) for task in tasks])


def assert_early_first_form(schedule, deadlines):
    n = schedule.length
    i = 1
    prev_deadline = -math.inf
    while i <= n and i <= deadlines[schedule[i]]:
        assert_that(prev_deadline <= deadlines[schedule[i]])
        prev_deadline = deadlines[schedule[i]]
        i += 1
    while i <= n:
        assert_that(i > deadlines[schedule[i]])
        i += 1


def get_min_total_penalty_bruteforce(deadlines, penalties):
    min_total_penalty = math.inf
    n = deadlines.length
    tasks = list(zip([i for i in between(1, n)], deadlines, penalties))
    for tasks_reordering in itertools.permutations(tasks):
        schedule_ids = Array([task[0] for task in tasks_reordering])
        min_total_penalty = \
            min(min_total_penalty, get_total_penalty(schedule_ids, deadlines, penalties))
    return min_total_penalty


def get_total_penalty(schedule, deadlines, penalties):
    n = schedule.length
    total_penalty = 0
    for i in between(1, n):
        if i > deadlines[schedule[i]]:
            total_penalty += penalties[schedule[i]]
    return total_penalty


class TestTextbook16_5(TestCase):

    def test_tasks_scheduling(self):
        n = random.randint(1, 8)
        deadlines, _ = get_random_array(min_size=n, max_size=n, min_value=1, max_value=n)
        penalties, _ = get_random_array(min_size=n, max_size=n)

        actual_schedule = tasks_scheduling(deadlines, penalties)

        schedule_ids = decode_tasks(actual_schedule)
        assert_early_first_form(schedule_ids, deadlines)
        expected_min_total_penalty = get_min_total_penalty_bruteforce(deadlines, penalties)
        actual_total_penalty = get_total_penalty(schedule_ids, deadlines, penalties)
        assert_that(actual_total_penalty, is_(equal_to(expected_min_total_penalty)))
