import copy
import random
from unittest import TestCase

from hamcrest import *

from chapter06.exercise6_2_5 import iterative_max_heapify
from heap_util import get_random_max_heap, assert_max_heap


class TestExercise6_2_5(TestCase):

    def test_iterative_max_heapify(self):
        heap = get_random_max_heap()
        i = random.randint(1, heap.heap_size)
        heap[i] -= random.randint(0, 500)  # randomly decrease the value of a randomly chosen element
        original = copy.deepcopy(heap)

        iterative_max_heapify(heap, i)

        assert_max_heap(heap)
        assert_that(heap, contains_inanyorder(*original))
