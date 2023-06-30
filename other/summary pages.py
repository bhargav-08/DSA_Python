"""
228. Summary Ranges

You are given a sorted unique integer array nums.

A range[a, b] is the set of all integers from a to b(inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is , each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range[a, b] in the list should be output as:

"a->b" if a != b
"a" if a == b
"""


def summaryRanges(nums):
    if not nums:
        return []

    start, res = nums[0], []
    for idx in range(1, len(nums)):
        if nums[idx] == nums[idx - 1] + 1:
            continue

        if start == nums[idx - 1]:
            res.append(f'{start}')
        else:
            res.append(f'{start}->{nums[idx-1]}')
        start = nums[idx]

    if start == nums[-1]:
        res.append(f'{start}')
    else:
        res.append(f'{start}->{nums[-1]}')

    return res


def summaryRanges(nums):
    ranges = []
    for n in nums:
        if not ranges or n > ranges[-1][-1] + 1:
            ranges += [],
        ranges[-1][1:] = n,
    return ['->'.join(map(str, r)) for r in ranges]


num = [0, 1, 2, 4, 5, 7]
num = [0, 2, 3, 4, 6, 8, 9]
print(summaryRanges(num))
