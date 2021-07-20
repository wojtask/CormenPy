import copy
import random
from unittest import TestCase

from hamcrest import *

from chapter06.exercise6_2_2 import min_heapify
from heap_util import get_random_min_heap, assert_min_heap


class TestExercise6_2_2(TestCase):

    def test_min_heapify(self):
        heap = get_random_min_heap()
        i = random.randint(1, heap.heap_size)
        heap[i] += random.randint(0, 500)  # randomly increase the value of a randomly chosen element
        original = copy.deepcopy(heap)

        min_heapify(heap, i)

        assert_min_heap(heap)
        assert_that(heap, contains_inanyorder(*original))
