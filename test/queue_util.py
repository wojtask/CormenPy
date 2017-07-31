def get_stack_keys(stack):
    return stack[1:stack.top].data


def get_queue_keys(queue):
    if queue.head <= queue.tail:
        return queue[queue.head:queue.tail - 1].data
    return queue[queue.head:queue.length].data + queue[1:queue.tail - 1].data
