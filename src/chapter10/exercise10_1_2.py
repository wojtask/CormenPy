def left_stack_push(A, x):
    if _stacks_full(A):
        raise ValueError('overflow')
    A.left_top += 1
    A[A.left_top] = x


def _stacks_full(A):
    return A.left_top == A.right_top - 1


def left_stack_pop(A):
    if _left_stack_empty(A):
        raise ValueError('underflow')
    A.left_top -= 1
    return A[A.left_top + 1]


def _left_stack_empty(A):
    return A.left_top == 0


def right_stack_push(A, x):
    if _stacks_full(A):
        raise ValueError('overflow')
    A.right_top -= 1
    A[A.right_top] = x


def right_stack_pop(A):
    if _right_stack_empty(A):
        raise ValueError('underflow')
    A.right_top += 1
    return A[A.right_top - 1]


def _right_stack_empty(A):
    return A.right_top == A.length + 1
