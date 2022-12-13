# Problem Statement => Calculate the smallest  difference between two subset from the given array
# Note: One Element should be in single set only not in both

import sys


def minSubsetSumDifference(arr):
    total = sum(arr)
    diff = sys.maxsize
    t = [0 for _ in range(total + 1)]
    t[0] = 1

    for i in range(len(arr)):
        for j in range(total, 0, -1):
            if j >= arr[i]:
                t[j] = max(t[j], t[j - arr[i]])
    mapping = [0]
    for i in range(1, total // 2 + 1):
        if i * t[i] == 0:
            continue
        mapping.append(i * t[i])

    for i in map(lambda x: x * 2, mapping):
        diff = min(total - i, diff)
    return diff


arr = [1, 6, 11, 5]
print(minSubsetSumDifference(arr))