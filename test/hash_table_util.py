import random

from chapter11.ex11_4_2 import Deleted
from datastructures.array import Array
from datastructures.hash_table import Element, ChainedElement
from datastructures.standard_array import StandardArray


def random_direct_address_table():
    table_size = random.randint(1, 10)
    nelements = random.randint(0, table_size)
    elements = [Element(key) for key in random.sample(range(table_size), nelements)]
    table = StandardArray.of_length(table_size)
    for element in elements:
        table[element.key] = element
    return table, elements


def random_bit_vector():
    bit_vector_size = random.randint(1, 10)
    nelements = random.randint(0, bit_vector_size)
    keys = random.sample(range(bit_vector_size), nelements)
    bit_vector = StandardArray([1 if i in keys else 0 for i in range(bit_vector_size)])
    return bit_vector, keys


def random_chained_direct_address_table():
    table_size = random.randint(1, 10)
    nelements = random.randint(0, table_size)
    elements = [ChainedElement(random.randint(0, table_size - 1)) for _ in range(nelements)]
    table = StandardArray.of_length(table_size)

    for element in elements:
        list_ = table[element.key]
        if list_:
            list_.prev = element
        element.next = list_
        table[element.key] = element
    return table, elements


def random_chained_hash_table(max_value=999):
    table_size = random.randint(1, 10)
    nelements = random.randint(0, 3 * table_size)
    elements = [ChainedElement(random.randint(0, max_value)) for _ in range(nelements)]
    table = StandardArray.of_length(table_size)
    h = _modular_hash

    for element in elements:
        list_ = table[h(element.key, table_size)]
        if list_:
            list_.prev = element
        element.next = list_
        table[h(element.key, table_size)] = element
    return table, elements, h


def random_huge_array(max_value=999):
    table_size = max_value
    table_capacity = random.randint(1, min(20, max_value))
    nelements = random.randint(0, table_capacity)
    table = StandardArray.of_length(table_size)
    stack = Array.of_length(table_capacity)
    keys = random.sample(range(max_value), nelements)

    for i, key in enumerate(keys):
        table[key] = i + 1
        stack[i + 1] = Element(key)
    stack.top = len(keys)

    return table, stack, keys


def _modular_hash(k, m):
    return k % m


def get_chained_hash_table_elements(table):
    elements = []
    for list_ in table:
        x = list_
        while x is not None:
            elements.append(x)
            x = x.next
    return elements


def random_hash_table_linear_probing(max_value=999):
    table, keys = _random_hash_table(_linear_hash, max_value)
    return table, keys, _linear_hash


def _linear_hash(k, i, m):
    return (_modular_hash(k, m) + i) % m


def random_hash_table_quadratic_probing(max_value=999):
    table, keys = _random_hash_table(_quadratic_hash, max_value)
    return table, keys, _quadratic_hash, _modular_hash


def _quadratic_hash(k, i, m):
    return (_modular_hash(k, m) + i * (i + 1) // 2) % m


def _random_hash_table(h, max_value):
    table_size = random.randint(1, 10)
    table = StandardArray.of_length(table_size)
    nelements = random.randint(0, table.length)
    keys = [random.randint(0, max_value) for _ in range(nelements)]
    for key in keys:
        i = 0
        while table[h(key, i, table_size)] is not None:
            i += 1
        table[h(key, i, table_size)] = key
    return table, keys


def get_hash_table_keys(table):
    return [key for key in table if key is not None and key is not Deleted]