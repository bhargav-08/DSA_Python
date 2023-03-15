def findKthLargest(nums, k: int) -> int:

    def quickselect(start, end):
        pivot, p = nums[start], start+1
        for i in range(start+1, end+1):
            if nums[i] <= pivot:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1

        nums[p], nums[start] = nums[start], nums[p]

        if p == len(nums)-k:
            return nums[p]
        elif p < len(nums)-k:
            return quickselect(p+1, end)
        else:
            return quickselect(start, p-1)

    return quickselect(0, len(nums)-1)


nums = [3, 2, 1, 5, 6, 4]
k = 2
print(findKthLargest(nums, k))
