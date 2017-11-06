def print_stations_(l, l_star, n):
    if n >= 1:
        print_stations_(l, l[l_star, n], n - 1)
        print('line ' + str(l_star) + ', station ' + str(n))
