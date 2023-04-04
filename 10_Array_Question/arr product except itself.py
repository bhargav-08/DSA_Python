""" 
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""


def productExceptSelf(nums):
    n = len(nums)
    res = [0]*n

    # calculate prefix
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]

    # caclculate sufix and update values
    suffix = 1
    for i in range(n-1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]

    return res


nums = [1, 2, 3, 4]
print(productExceptSelf(nums))
