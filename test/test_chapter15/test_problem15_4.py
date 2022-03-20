import io
import random
from contextlib import redirect_stdout
from unittest import TestCase

from hamcrest import *

from chapter15.problem15_4 import company_party, print_guests
from datastructures.array import Array
from datastructures.rooted_tree import RootedTree, EmployeeNode
from util import between


def get_company_hierarchy():
    company_size = random.randint(1, 20)
    boss = employee = None
    for i in between(1, company_size):
        new_employee = EmployeeNode(None, 'employee %d' % i, random.randint(-20, 20))
        if i == 1:
            boss = new_employee
        elif i == 2 or random.randint(0, 1) == 0:
            employee.left_child = new_employee
        else:
            employee.right_sibling = new_employee
        employee = new_employee
    return RootedTree(boss)


def get_conviviality(employee, invited_employees):
    if not employee:
        return 0
    conviviality = employee.conv if employee.name in invited_employees else 0
    conviviality += get_conviviality(employee.left_child, invited_employees)
    conviviality += get_conviviality(employee.right_sibling, invited_employees)
    return conviviality


def get_maximum_conviviality_bruteforce(hierarchy):
    return get_maximum_conviviality_from(hierarchy.root)


def get_maximum_conviviality_from(employee):
    conviviality_if_invited = employee.conv
    conviviality_if_uninvited = 0
    subordinate = employee.left_child
    while subordinate:
        conviviality_if_invited += get_maximum_conviviality_from_uninvited(subordinate)
        conviviality_if_uninvited += get_maximum_conviviality_from(subordinate)
        subordinate = subordinate.right_sibling
    return max(conviviality_if_invited, conviviality_if_uninvited)


def get_maximum_conviviality_from_uninvited(employee):
    conviviality = 0
    subordinate = employee.left_child
    while subordinate:
        conviviality += get_maximum_conviviality_from(subordinate)
        subordinate = subordinate.right_sibling
    return conviviality


class TestProblem15_4(TestCase):

    def test_company_party(self):
        company_hierarchy = get_company_hierarchy()
        captured_output = io.StringIO()

        actual_maximum_conviviality = company_party(company_hierarchy.root)
        with redirect_stdout(captured_output):
            print_guests(company_hierarchy.root)

        expected_maximum_conviviality = get_maximum_conviviality_bruteforce(company_hierarchy)
        assert_that(actual_maximum_conviviality, is_(equal_to(expected_maximum_conviviality)))
        actual_output = Array(captured_output.getvalue().splitlines())
        actual_maximum_conviviality = get_conviviality(company_hierarchy.root, actual_output)
        assert_that(actual_maximum_conviviality, is_(equal_to(expected_maximum_conviviality)))
