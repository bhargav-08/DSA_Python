"""
You are given an array nums consisting of positive integers.

You are also given an integer array queries of size m. For the ith query, you want to make all of the elements of nums equal to queries[i]. You can perform the following operation on the array any number of times:

Increase or decrease an element of the array by 1.
Return an array answer of size m where answer[i] is the minimum number of operations to make all elements of nums equal to queries[i].

Note that after each query the array is reset to its original state.

Input: nums = [3,1,6,8], queries = [1,5]
Output: [14,10]
Explanation: For the first query we can do the following operations:
- Decrease nums[0] 2 times, so that nums = [1,1,6,8].
- Decrease nums[2] 5 times, so that nums = [1,1,1,8].
- Decrease nums[3] 7 times, so that nums = [1,1,1,1].
So the total number of operations for the first query is 2 + 5 + 7 = 14.
For the second query we can do the following operations:
- Increase nums[0] 2 times, so that nums = [5,1,6,8].
- Increase nums[1] 4 times, so that nums = [5,5,6,8].
- Decrease nums[2] 1 time, so that nums = [5,5,5,8].
- Decrease nums[3] 3 times, so that nums = [5,5,5,5].
So the total number of operations for the second query is 2 + 4 + 1 + 3 = 10.
"""

from itertools import accumulate
from bisect import bisect_left


def min_Operations(nums, queries):

    nums.sort()
    ps, n = [0] + list(accumulate(nums)), len(nums)
    splits = [(q, bisect_left(nums, q)) for q in queries]
    res = []
    for q, i in splits:
        p1 = q * i - ps[i]
        p2 = (ps[-1] - ps[i]) - q * (n - i)
        res.append(p1 + p2)

    return res


nums = [3, 1, 6, 8]
queries = [1, 5]
print(min_Operations(nums, queries))
