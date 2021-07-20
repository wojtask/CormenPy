from util import between


def radix_sort(A, d):
    for i in between(1, d):
        _stable_sort_on_digit(A, i)


def _stable_sort_on_digit(A, digit):
    A.sort(key=lambda x: _get_digit(x, digit))


def _get_digit(number, digit):
    power_of_10 = 10 ** (digit - 1)
    return number // power_of_10 % 10
