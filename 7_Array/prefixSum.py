def maxLen(arr):
    temp = 0
    prefixSum = {}
    answer = 0

    for i, num in enumerate(arr):
        temp += num

        if temp == 0:
            answer = max(answer, i+1)
        elif temp in prefixSum:
            length = i - prefixSum[temp]
            answer = max(answer, length)
        else:
            prefixSum[temp] = i

    return answer


arr = [15, -2, 2, -8, 1, 7, 10, 23]
print(maxLen(arr))
