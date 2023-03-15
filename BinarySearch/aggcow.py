def chessTournament(positions, n, c):
    positions.sort()

    def feasible(val):
        player = 1
        i = 0
        j = 1
        while j < n:
            if positions[j]-positions[i] >= val:
                i = j
                player += 1
            if player == c:
                return True
            j += 1
        return False

    low = 1
    high = positions[-1] - positions[0]
    res = float("-inf")

    while low <= high:
        mid = low+high >> 1
        if feasible(mid):
            res = mid
            low = mid+1
        else:
            high = mid-1

    return res


# position = [1, 2, 3, 4, 6]
# c = 3

# position = [1, 2, 4, 5]
# c = 2


c = 8
pos = [9, 6, 3, 12, 13, 14, 15, 16]
n = len(pos)
print(chessTournament(pos, n, c))
