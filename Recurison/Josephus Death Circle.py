def JosephusDeathCircle(n, k):

    def helper(arr, k, i):
        if len(arr) == 1:
            return arr[0]

        i = (i + k) % len(arr)
        arr.pop(i)
        return helper(arr, k, i)

    arr = [i for i in range(1, n + 1)]
    return helper(arr, k - 1, 0)


# print(JosephusDeathCircle(40, 7))

import math
import sys

print(0.15 + 0.15 - 0.2 + 0.1 < 0.0001)
