from bisect import bisect_right


def findKthNumber(m: int, n: int, k: int) -> int:
    low = 1
    high = m*n

    def feasible(val):
        result = 0
        # TLE
        # for row in matrix:
        #     result = result+bisect_right(row, val)

        for r in range(1, m+1):
            c = val//r
            result += min(c, n)

        if result >= k:
            return True
        else:
            return False

    while low < high:
        mid = low+high >> 1

        if feasible(mid):
            high = mid
        else:
            low = mid+1

    return low


m = 9895
n = 28405
k = 100787757
print(findKthNumber(m, n, k))
