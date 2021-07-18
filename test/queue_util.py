from datastructures.array import Array


def get_stack_elements(stack):
    return Array(stack[1:stack.top].elements)


def get_queue_elements(queue):
    if queue.head <= queue.tail:
        return Array(queue[queue.head:queue.tail - 1].elements)
    return Array(queue[queue.head:queue.length].elements + queue[1:queue.tail - 1].elements)
