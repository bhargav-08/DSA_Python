def shipWithinDays(weights, days: int) -> int:
    left, right = max(weights), sum(weights)

    while left < right:
        mid = (left+right)//2
        curr = 0
        res = 1
        for w in weights:
            if curr+w <= mid:
                curr += w
            else:
                curr = w
                res += 1
        if res <= days:
            right = mid-1
        else:
            left = mid+1

    return left


weights = [3, 2, 2, 4, 1, 4]
days = 3

print(shipWithinDays(weights, days))
