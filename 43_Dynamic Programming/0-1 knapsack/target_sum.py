# Problem Statment => Count the total number of ways we can obtain sum by either putting + or - sign in front of every element of array

from pprint import pprint


def countSubsetDifference(arr, target):
    total = sum(arr)
    if target > total or (target + total) % 2 != 0:
        return 0
    t = [0 for _ in range(total + 1)]
    t[0] = 1

    for i in range(0, len(arr)):
        for j in range(total, 0, -1):
            if j >= arr[i] or arr[i] == 0:
                t[j] = t[j] + t[j - arr[i]]
    # pprint(t, compact=True)
    if 0 in arr:
        # print(t[target])
        return int(pow(2, arr.count(0)) * t[target])
    else:

        s1 = (target + total) / 2
        return t[int(s1)]


def targetSumR(arr, target, n):
    if target == 0 and n == 0:
        return 1
    if n == 0:
        return 0

    positive = targetSumR(arr, target - arr[n - 1], n - 1)
    negative = targetSumR(arr, target + arr[n - 1], n - 1)

    return positive + negative


# num = [1, 2, 1, 3]
# num = [1, 1, 2, 3]

# num = [1, 1, 1, 1, 1]
# target = 3 # 5

# num = [0, 0, 0, 0, 0, 0, 0, 0, 1]
# target = 1 # 256

# num = [7, 9, 3, 8, 0, 2, 4, 8, 3, 9]
# target = 0 #2

num = [1, 0]
target = 1  # 2
print(countSubsetDifference(num, target))

# print(targetSumR(num, target, len(num)))
