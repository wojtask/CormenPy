def print_stations_increasing(l, i, j):
    if j >= 1:
        print_stations_increasing(l, l[i, j], j - 1)
        print('line ' + str(i) + ', station ' + str(j))
