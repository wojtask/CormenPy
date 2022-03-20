import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter15.exercise15_2_2 import matrix_chain_multiply
from chapter15.textbook15_2 import matrix_multiply, matrix_chain_order
from datastructures.array import Array
from test_chapter15.test_textbook15_2 import get_random_matrix
from util import between


def get_matrix_product(A):
    n = A.length
    product = A[1]
    for i in between(2, n):
        product = matrix_multiply(product, A[i])
    return product


class TestExercise15_2_2(TestCase):

    def test_matrix_chain_multiply(self):
        n = random.randint(1, 10)
        dimensions = get_random_array(size=n + 1, min_value=1, max_value=10, start=0)
        A = Array.indexed(1, n)
        for i in between(1, n):
            A[i] = get_random_matrix(dimensions[i - 1], dimensions[i])
        _, optimal_solution = matrix_chain_order(dimensions)

        actual_product = matrix_chain_multiply(A, optimal_solution, 1, n)

        expected_product = get_matrix_product(A)
        assert_that(actual_product, expected_product)
