# Problem Statement -  Calculate the number of subset which can be formed for given sum and return the count

from pprint import pprint


def countSubsetSum(arr, total):
    t = [[0 for _ in range(total + 1)] for _ in range(len(arr) + 1)]

    for i in range(len(arr) + 1):
        for j in range(total + 1):
            if i == 0:
                t[i][j] = False
            if j == 0:
                t[i][j] = 1

    for i in range(1, len(arr) + 1):
        for j in range(1, total + 1):
            if j >= arr[i - 1]:
                t[i][j] = t[i - 1][j] + t[i - 1][j - arr[i - 1]]
            elif j < arr[i - 1]:
                t[i][j] = t[i - 1][j]

    return t[-1][-1]


arr = [2, 3, 5, 6, 8, 10]
# arr = [1, 2, 1, 3]
total = 10
print(countSubsetSum(arr, total))
