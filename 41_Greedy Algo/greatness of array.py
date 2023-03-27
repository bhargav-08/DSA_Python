from collections import Counter
from bisect import bisect_left


def maximizeGreatness(nums) -> int:
    nums.sort()
    cnt = Counter(nums)
    arr = sorted(set(nums))
    greatness = 0

    for i in nums:
        ind = bisect_left(arr, i+1)
        if ind < len(arr) and cnt[arr[ind]] > 0:
            greatness += 1
            cnt[arr[ind]] -= 1
            if cnt[arr[ind]] == 0:
                arr.remove(arr[ind])

    return greatness


def maximizeGreatness(A):
    A.sort()
    res = 0
    for a in A:
        if a > A[res]:
            res += 1
    return res


nums = [1, 3, 5, 2, 1, 3, 1]
print(maximizeGreatness(nums))
