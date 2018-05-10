def greedy_knapsack(w, v, W):
    weight_sum = 0
    value_sum = 0
    i = 1
    while i <= w.length and weight_sum + w[i] <= W:
        print('a' + str(i))
        weight_sum += w[i]
        value_sum += v[i]
        i += 1
    return value_sum
