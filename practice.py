from collections import defaultdict


def longestEqualSubarray(nums, k: int) -> int:
    low, high = 1, len(nums)

    def check(x):
        size = x + k
        count = defaultdict(int)

        for i in range(len(nums)):
            count[nums[i]] += 1
            if i >= size:
                count[nums[i-size]] -= 1
            if count[nums[i]] >= x:
                return True
        return False

    while low < high:
        mid = (low + high) >> 1
        if check(mid):
            # res = mid
            low = mid
        else:
            high = mid - 1

    # return res
    return low


nums = [3, 2, 4, 2]
k = 1
print(longestEqualSubarray(nums, k))
