def rb_enumerate(T, x, a, b):
    if x is not T.nil:
        if x.key > a:
            rb_enumerate(T, x.left, a, b)
        if a <= x.key <= b:
            print(x.key)
        if x.key < b:
            rb_enumerate(T, x.right, a, b)
