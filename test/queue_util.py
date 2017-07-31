def get_stack_elements(stack):
    return stack[1:stack.top].elements


def get_queue_elements(queue):
    if queue.head <= queue.tail:
        return queue[queue.head:queue.tail - 1].elements
    return queue[queue.head:queue.length].elements + queue[1:queue.tail - 1].elements
