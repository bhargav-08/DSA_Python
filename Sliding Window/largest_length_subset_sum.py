def largestLenSubset(arr, target):
    cnt = 0
    i, j = 0, 0
    sum = 0

    while j < len(arr) and i < len(arr):
        sum += arr[j]
        if sum > k:
            while sum > target:
                sum -= arr[i]
                i += 1
        elif sum == k:
            cnt = max(cnt, j-i+1)
        j += 1

    return cnt


arr = [4, 1, 1, 1, 2, 3, 5]
k = 5
print(largestLenSubset(arr, k))
