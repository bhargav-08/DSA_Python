def maxSubArray(nums) -> int:
    currsum = nums[0]
    maxsum = nums[0]

    for i in nums[1:]:
        if i > currsum:
            currsum = i
        else:
            currsum = currsum+i

        maxsum = max(maxsum, currsum)

    return maxsum


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(arr))
