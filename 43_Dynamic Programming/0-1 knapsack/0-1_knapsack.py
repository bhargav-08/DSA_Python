import pprint


def knapsack_tabulation(weight, profit, max_weight, n):
    table = [[0 for j in range(max_weight + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for j in range(max_weight + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            else:
                if j >= weight[i - 1]:
                    table[i][j] = max(
                        table[i - 1][j],
                        profit[i - 1] + table[i - 1][j - weight[i - 1]])
                else:
                    table[i][j] = table[i - 1][j]
    # pprint.pprint(table)
    return table[-1][-1]


def knapsack_recursive(weight, profit, max_weight, n):
    global count
    count = count + 1
    if n == 0 or max_weight == 0:
        return 0
    elif weight[n - 1] <= max_weight:
        return max(
            profit[n - 1] + knapsack_recursive(
                weight, profit, max_weight - weight[n - 1], n - 1),
            knapsack_recursive(weight, profit, max_weight, n - 1))
    elif weight[n - 1] > max_weight:
        return knapsack_recursive(weight, profit, max_weight, n - 1)


def knapsack_recursive_memoization(weight, profit, max_weight, n):
    global count
    count = count + 1

    if n == 0 or max_weight == 0:
        return 0

    if t[n][max_weight] != -1:
        return t[n][max_weight]

    if weight[n - 1] <= max_weight:
        t[n][max_weight] = max(profit[n - 1] + knapsack_recursive_memoization(
            weight, profit, max_weight - weight[n - 1], n - 1),
                               knapsack_recursive_memoization(
                                   weight, profit, max_weight,
                                   n - 1))  # type: ignore
        return t[n][max_weight]

    if weight[n - 1] > max_weight:
        t[n][max_weight] = knapsack_recursive_memoization(  # type: ignore
            weight, profit, max_weight, n - 1)
        return t[n][max_weight]


max_weight = 8
n = 4
p = [1, 2, 5, 6]
w = [2, 3, 4, 5]
count = 0

# print(knapsack_tabulation(w, p, max_weight, n))
# print(knapsack_recursive(w, p, max_weight, n))  # total 21 count

t = [[-1 for _ in range(100)] for _ in range(100)]
import timeit

SETUP_CODE1 = """
from __main__ import knapsack_recursive_memoization
count = 0
t = [[-1 for _ in range(100)] for _ in range(100)]
"""
SETUP_CODE2 = """
from __main__ import knapsack_recursive
count = 0
t = [[-1 for _ in range(100)] for _ in range(100)]
"""

TEST_CODE1 = """
max_weight = 80
n = 4
p = [1, 2, 5, 6]
w = [2, 3, 4, 5]
knapsack_recursive_memoization(w,p,max_weight,n)
"""
TEST_CODE2 = """
max_weight = 80
n = 4
p = [1, 2, 5, 6]
w = [2, 3, 4, 5]
knapsack_recursive(w,p,max_weight,n)
"""

time1 = timeit.repeat(setup=SETUP_CODE1,
                      stmt=TEST_CODE1,
                      number=1_00_000,
                      repeat=3)

time1_with_global = timeit.repeat(
    "knapsack_recursive_memoization(w,p,max_weight,n)",
    number=1_00_000,
    globals=globals(),
    repeat=3)

time2 = timeit.repeat(setup=SETUP_CODE2,
                      stmt=TEST_CODE2,
                      number=1_00_000,
                      repeat=3)

print(f"Time required for memoization code => {min(time1)}")
print(f"Time required without memoization code => {min(time2)}")

# print(knapsack_recursive_memoization(w, p, max_weight, n))  # total 8 count
# print(count)
# pprint.pprint(t, compact=True)
