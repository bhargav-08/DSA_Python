def reversePairs(nums) -> int:

    def merge(start, end):
        if start >= end:
            return 0
        mid = (start+end)//2
        answer = merge(start, mid) + merge(mid+1, end)

        j = mid+1
        for i in range(start, mid+1):
            while j <= end and nums[i] > 2*nums[j]:
                j += 1
            answer += j-(mid+1)

        nums[start:end+1] = sorted(nums[start:end+1])
        return answer

    return merge(0, len(nums)-1)


arr = [40, 25, 19, 12, 9, 6, 2]
print(reversePairs(arr))
