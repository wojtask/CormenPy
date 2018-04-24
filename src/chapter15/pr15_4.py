def company_party(x):
    x.invited = x.conv
    x.uninvited = 0
    y = x.left_child
    while y is not None:
        company_party(y)
        x.invited = x.invited + y.uninvited
        x.uninvited = x.uninvited + max(y.invited, y.uninvited)
        y = y.right_sibling
    return max(x.invited, x.uninvited)


def print_guests(x):
    if x.invited > x.uninvited:
        print(x.name)
        y = x.left_child
        while y is not None:
            print_uninvited(y)
            y = y.right_sibling
    else:
        print_uninvited(x)


def print_uninvited(x):
    y = x.left_child
    while y is not None:
        print_guests(y)
        y = y.right_sibling
