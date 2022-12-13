# Problem Statment => Count the total number of subset whose difference is equal to given value

from pprint import pprint


def countSubsetDifference(arr, diff):
    total = sum(arr)
    t = [0 for _ in range(total + 1)]
    t[0] = 1

    for i in range(0, len(arr)):
        for j in range(total, 0, -1):
            if j >= arr[i]:
                t[j] = t[j] + t[j - arr[i]]
    # pprint(t)
    s1 = (diff + total) / 2
    # print(s1)
    if int(s1) == s1:
        return t[int(s1)]
    else:
        return 0


num = [1, 2, 1, 3]
num = [1, 1, 2, 3]
diff = 1
print(countSubsetDifference(num, diff))
