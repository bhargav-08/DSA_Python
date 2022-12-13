import functools
from pprint import pprint
from timeit import timeit


# @functools.lru_cache()
def rodCutting(max_weight, profit, n):
    if max_weight == 0 or n == 0:
        return 0

    elif max_weight >= n:
        return max(
            rodCutting(max_weight, profit, n - 1),  # type: ignore
            profit[n - 1] + rodCutting(max_weight - n, profit, n))

    elif max_weight < n:
        return rodCutting(max_weight, profit, n - 1)


cache = {}


def rodCuttingMemo(max_weight, profit, n):
    if (max_weight, n) in cache:
        return cache[(max_weight, n)]

    if max_weight == 0 or n == 0:
        return 0

    elif max_weight >= n:
        cache[(max_weight, n)] = max(
            rodCutting(max_weight, profit, n - 1),  # type: ignore
            profit[n - 1] + rodCutting(max_weight - n, profit, n))
        return cache[(max_weight, n)]

    elif max_weight < n:
        cache[(max_weight, n)] = rodCutting(max_weight, profit, n - 1)
        return cache[(max_weight, n)]


def rodCutting2DTab(max_weight, profit):
    n = len(profit)
    t = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, max_weight + 1):
            if j >= i:
                t[i][j] = max(t[i - 1][j], profit[i - 1] + t[i][j - i])
            else:
                t[i][j] = t[i - 1][j]
    return t[-1][-1]


def rodCutting1DTab(max_weight, profit):
    n = len(profit)
    t = [0 for _ in range(max_weight + 1)]

    for i in range(1, len(profit) + 1):
        for j in range(1, max_weight + 1):
            if j >= i:
                t[j] = max(t[j], profit[i - 1] + t[j - i])

    return t[-1]

max_weight = 8
n = 8
p = (1, 5, 8, 9, 10, 17, 17, 20)
# w = list(range(1, 9))
# print(timeit("rodCutting(max_weight,p,n)", globals=globals(), number=1_00_000))
# print(
#     timeit("rodCuttingMemo(max_weight,p,n)",
#            globals=globals(),
#            number=1_00_000))

# print(rodCutting.cache_info())
# print(rodCutting(max_weight, p, n))

print(rodCutting2DTab(max_weight, p))
print(rodCutting1DTab(max_weight, p))
