# TC => O(n**2)
def maxSubArray(arr):
    answer = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            answer = max(answer, sum(arr[i:j+1]))
    return answer


# TC => O(n)
def kandaneAlog(arr):
    currsum = 0
    maxsum = arr[0]
    for i in arr:
        currsum += i

        maxsum = max(maxsum, currsum)

        if currsum <= 0:
            currsum = 0

    return maxsum


def circularKandane(nums):
    maxsum = nums[0]
    currsum = 0
    n = len(nums)
    second = False

    for i in range(2*n):
        if i >= n:
            second = True
        currsum += nums[i % n]
        maxsum = max(maxsum, currsum)
        if currsum < 0:
            if second:
                break
            currsum = 0

    return maxsum


arr = [-5, 4, 6, -3, 4, -1, 100]
arr = [1, 2, 3, -2, 5]
arr = [-10, -2, -3, -4]
arr = [5, -3, 5]

print(circularKandane(arr))
