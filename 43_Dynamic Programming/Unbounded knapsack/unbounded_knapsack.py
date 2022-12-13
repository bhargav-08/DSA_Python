import pprint


def unbounded_knapsack(max_weight, profit, weight, n):
    table = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(max_weight + 1):

            if j >= weight[i - 1]:
                table[i][j] = max(table[i - 1][j],
                                  profit[i - 1] + table[i][j - weight[i - 1]])
            else:
                table[i][j] = table[i - 1][j]

    # pprint.pprint(table)
    return table[-1][-1]


max_weight = 8
n = 4
p = [1, 2, 5, 6]
w = [2, 3, 4, 5]
print(unbounded_knapsack(max_weight, p, w, n))
