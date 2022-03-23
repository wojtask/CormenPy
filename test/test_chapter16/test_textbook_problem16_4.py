import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter16.textbook_problem16_4 import tasks_scheduling_
from test_chapter16.test_textbook16_5 import decode_tasks, get_min_total_penalty_bruteforce, get_total_penalty


class TestTextbookProblem16_4(TestCase):

    def test_tasks_scheduling_(self):
        n = random.randint(1, 8)
        deadlines = get_random_array(size=n, min_value=1, max_value=n)
        penalties = get_random_array(size=n)

        actual_schedule = tasks_scheduling_(deadlines, penalties)

        assert_that(deadlines.is_modified(), is_(False))
        assert_that(penalties.is_modified(), is_(False))
        schedule_ids = decode_tasks(actual_schedule)
        expected_min_total_penalty = get_min_total_penalty_bruteforce(deadlines, penalties)
        actual_total_penalty = get_total_penalty(schedule_ids, deadlines, penalties)
        assert_that(actual_total_penalty, is_(equal_to(expected_min_total_penalty)))
