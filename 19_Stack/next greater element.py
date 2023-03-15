def nextGreaterElement(nums1, nums2):
    s = []
    mp = {k: -1 for k in nums1}
    res = [-1]*len(nums1)

    for i in range(len(nums2)):
        cur = nums2[i]
        while s and cur > s[-1]:
            val = s.pop()
            mp[val] = cur
        if cur in mp:
            s.append(cur)

    for ind, num in enumerate(nums1):
        res[ind] = mp[num]

    return res


"""
503. Next Greater Element II

Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.
"""


def nextGreaterElementsCircular(nums):
    res = [-1]*len(nums)
    N = len(nums)
    s = []

    for i in range(len(nums)*2):
        curr = nums[i % N]
        while s and curr > nums[s[-1]]:
            res[s.pop()] = curr
        s.append(i % N)

    return res


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(nextGreaterElement(nums1, nums2))
