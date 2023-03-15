def minDays(bloomDay, m: int, k: int) -> int:
    if m*k > len(bloomDay):
        return -1

    def feasible(val):
        req = m
        cnt = k
        for b in bloomDay:
            if val >= b:
                cnt -= 1
            else:
                cnt = k

            if cnt == 0:
                req -= 1
                cnt = k
            if req == 0:
                return True

        return False

    low = 1
    high = max(bloomDay)

    while low < high:
        mid = low+high >> 1

        if feasible(mid):
            high = mid
        else:
            low = mid+1

    return low


bloomDay = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
m = 4
k = 2
print(minDays(bloomDay, m, k))
