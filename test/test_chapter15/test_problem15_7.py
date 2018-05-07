import io
import itertools
import random
import re
from contextlib import redirect_stdout
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter15.problem15_7 import jobs_scheduling, print_schedule
from datastructures.array import Array
from util import between


def get_optimal_schedule_bruteforce(times, profits, deadlines):
    n = times.length
    max_profit = 0
    for m in between(1, n):
        for schedule in itertools.permutations(between(1, n), m):
            profit = get_schedule_total_profit(schedule, times, profits, deadlines)
            max_profit = max(max_profit, profit)
    return max_profit


def get_schedule_total_profit(schedule, times, profits, deadlines):
    total_time = 0
    profit = 0
    for job_id in schedule:
        total_time += times[job_id]
        if total_time <= deadlines[job_id]:
            profit += profits[job_id]
    return profit


class TestProblem15_7(TestCase):

    def test_jobs_scheduling(self):
        n = random.randint(1, 8)
        times, times_elements = get_random_array(min_size=n, max_size=n, min_value=1, max_value=n)
        profits, profits_elements = get_random_array(min_size=n, max_size=n)
        deadlines_elements = [random.randint(times_elements[j], n ** 2 + 10) for j in range(n)]
        deadlines = Array(deadlines_elements)
        captured_output = io.StringIO()

        actual_max_profits, actual_schedule, sorted_job_ids = jobs_scheduling(times, profits, deadlines)
        with redirect_stdout(captured_output):
            print_schedule(actual_schedule, sorted_job_ids, times, deadlines, n, actual_schedule[0].length - 1)

        expected_max_profit = get_optimal_schedule_bruteforce(
            Array(times_elements), Array(profits_elements), Array(deadlines_elements))
        assert_that(actual_max_profits[actual_max_profits.length - 1], is_(equal_to(expected_max_profit)))
        scheduled_jobs = [int(re.search('a(\d)+', job).group(1)) for job in captured_output.getvalue().splitlines()]
        profit_from_schedule = get_schedule_total_profit(
            scheduled_jobs, Array(times_elements), Array(profits_elements), Array(deadlines_elements))
        assert_that(profit_from_schedule, is_(equal_to(expected_max_profit)))
