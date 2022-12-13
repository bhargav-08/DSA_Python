import collections
import math


def kpermutation(k, n):
    num = list(range(1, n+1))
    k = k-1
    answer = ""

    def solve(n):
        nonlocal k, answer

        while True:
            if not num:
                break
            total_ways = math.factorial(n-1)
            block = k//total_ways
            answer += str(num[block])
            num.pop(block)
            k = k % total_ways
            n -= 1

    def solve2(n, k, answer):

        if not num:
            return answer

        total_ways = math.factorial(n-1)
        block = k//total_ways
        val = num.pop(block)

        return solve2(n-1, k % total_ways, answer+str(val))

    return solve2(n, k, "")
    # print(answer)


k = 24
n = 4
# print(kpermutation(k, n))


print(help(collections.deque()))
