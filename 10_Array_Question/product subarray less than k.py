""" 713. Subarray Product Less Than K
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.


Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
"""


def numSubarrayProductLessThanK(nums, k: int) -> int:
    left = res = 0
    prod = 1

    for right, val in enumerate(nums):
        prod *= val
        while prod >= k and right >= left:
            prod //= nums[left]
            left += 1
        res += right-left+1

    return res
