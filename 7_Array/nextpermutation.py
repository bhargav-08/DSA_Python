def nextPermutation(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    def reverse(start, end):
        while (start < end):
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    i = len(nums)-2

    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1

    if i >= 0:
        l = len(nums)-1
        while l >= 0 and nums[l] <= nums[i]:
            l -= 1

        nums[i], nums[l] = nums[l], nums[i]
    print(nums)
    reverse(i+1, len(nums)-1, nums)


nums = [5, 1, 1]
nextPermutation(nums)
print(nums)
