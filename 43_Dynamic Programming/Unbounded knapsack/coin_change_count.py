from pprint import pprint


def coinChangeRecursive(coins, total, n):
    if total == 0:
        return 1
    if n == 0:
        return 0
    elif total >= coins[n - 1]:
        return (coinChangeRecursive(coins, total, n - 1) +
                coinChangeRecursive(coins, total - coins[n - 1], n))
    elif total < coins[n - 1]:
        return coinChangeRecursive(coins, total, n - 1)


def coinChange2D(coins, total):
    t = [[1 for _ in range(total + 1)] for _ in range(len(coins) + 1)]
    for _ in range(1, total + 1):
        t[0][_] = 0

    for i in range(1, len(coins) + 1):
        for j in range(1, total + 1):
            if j >= coins[i - 1]:
                t[i][j] = t[i - 1][j] + t[i][j - coins[i - 1]]
            elif coins[i - 1] > j:
                t[i][j] = t[i - 1][j]
    # pprint(t)
    return t[-1][-1]


# coins = [1, 2, 3]
# total = 4  # 4

coins = [2, 3, 5, 6]
total = 10  # 5
n = len(coins)
print(coinChangeRecursive(coins, total, len(coins)))
print(coinChange2D(coins, total))
