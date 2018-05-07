def print_stations_(l, i, j):
    if j >= 1:
        print_stations_(l, l[i, j], j - 1)
        print('line ' + str(i) + ', station ' + str(j))
