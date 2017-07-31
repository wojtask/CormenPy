def below_square_sort(A):
    n = A.length
    _stable_sort_on_digit(A, 1, n)
    _stable_sort_on_digit(A, 2, n)


def _stable_sort_on_digit(A, digit, base):
    A.elements.sort(key=lambda x: _get_digit(x, digit, base))


def _get_digit(number, digit, base):
    power_of_base = base ** (digit - 1)
    return number // power_of_base % base
