# Problem Statement => Check whether there exist two subset for given sum in equal partition
# Note: One element should be only in one set cannot be included in both the set

import pprint


def canPartition(nums):

    def subset_sum(arr, total):
        t = [[-1 for _ in range(total + 1)] for _ in range(len(arr) + 1)]
        for i in range(len(arr) + 1):
            for j in range(total + 1):
                if i == 0:
                    t[i][j] = False
                if j == 0:
                    t[i][j] = True

        for i in range(1, len(arr) + 1):
            for j in range(1, total + 1):
                if arr[i - 1] <= j:
                    t[i][j] = max(t[i - 1][j - arr[i - 1]], t[i - 1][j])
                elif arr[i - 1] > j:
                    t[i][j] = t[i - 1][j]
        return t[-1][-1]

    result = sum(nums)

    if result % 2 != 0:
        return False
    else:
        return subset_sum(nums, result // 2)


nums = [1, 3, 2, 4, 8]
# print(canPartition(nums))


def dfs(arr, sum, n):
    if sum == 0:
        return True
    if n == 0:
        return False

    return max(dfs(arr, sum - arr[n - 1], n - 1), dfs(arr, sum, n - 1))


total = 9
print(dfs(nums, total, len(nums)))
