from pprint import pprint


def minCoinChange(coins, total, n):
    if total == 0:
        return 0
    if n == 0:
        return float("inf")
    elif coins[n - 1] <= total:
        return min(
            minCoinChange(coins, total, n - 1),  # type: ignore
            1 + minCoinChange(coins, total - coins[n - 1], n))
    elif coins[n - 1] > total:
        return minCoinChange(coins, total, n - 1)


def minCoinChange2d(coins, total):
    n = len(coins)
    t = [[0 for _ in range(total + 1)] for _ in range(n + 1)]

    for i in range(total + 1):
        t[0][i] = float("inf")  # type: ignore

    for i in range(1, len(coins) + 1):
        for j in range(1, total + 1):
            if j >= coins[i - 1]:
                t[i][j] = min(t[i - 1][j], 1 + t[i][j - coins[i - 1]])
            elif j < coins[i - 1]:
                t[i][j] = t[i - 1][j]

    # pprint(t)
    return t[-1][-1]


def minCoinChange1d(coins, total):
    n = len(coins)
    t = [float("inf") for _ in range(total + 1)]
    t[0] = 0

    for i in range(1, n + 1):
        for j in range(1, total + 1):
            if j >= i:
                t[j] = min(t[j], 1 + t[j - coins[i - 1]])
    # pprint(t)
    return t[-1]


coins = [1, 2, 3]
total = 5

coins = [2, 3, 6]
total = 10
# print(minCoinChange(coins, total, len(coins)))
print(minCoinChange2d(coins, total))
print(minCoinChange1d(coins, total))
