# distances[1] is the distance from the start to the first station
# distances[i], i > 1, is the distance from station i - 1 to station i
# distances[m + 1] is the distance from station m to the finish
# Assumption: for all i = 1, ..., m + 1, distance[i] <= n


def greedy_refueling(distances, n):
    m = distances.length - 1
    S = set()
    i = 1
    while i <= m + 1:
        current_distance = 0
        while i <= m + 1 and current_distance + distances[i] <= n:
            current_distance += distances[i]
            i += 1
        if i <= m + 1:
            S.add(i - 1)
    return S
