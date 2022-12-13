def drop(f, e):
    if f == 0 or f == 1:
        return f
    if e == 1:
        return f

    if memo[e][f] != -1:
        return memo[e][f]

    answer = float("inf")

    for k in range(1, f + 1):

        temp = 1 + max(drop(k - 1, e - 1), drop(f - k, e))
        answer = min(temp, answer)

    memo[e][f] = answer
    return answer


f = 464
e = 2
memo = [[-1 for _ in range(f + 1)] for _ in range(e + 1)]
print(drop(f, e))
