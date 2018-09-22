from chapter10.textbook10_1 import stack_empty, push, pop


def effective_stack_enqueue(S1, x):
    push(S1, x)


def effective_stack_dequeue(S1, S2):
    if stack_empty(S2):
        while not stack_empty(S1):
            push(S2, pop(S1))
    return pop(S2)
