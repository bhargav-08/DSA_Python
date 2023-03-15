""" MAXIMUM SUM COMBINATIONS
Given two equally sized 1-D arrays A, B containing N integers each.

A sum combination is made by adding one element from array A and another element of array B.

Return the maximum C valid sum combinations from all the possible sum combinations.
"""

import heapq


def solve(A, B, C):
    A.sort()
    B.sort()
    res = []
    hp = [(-(A[-1]+B[-1]), (len(A)-1, len(B)-1))]
    vis = set()
    vis.add((len(A)-1, len(B)-1))

    while C:
        mx, (x, y) = heapq.heappop(hp)
        res.append(-mx)
        if x > 0 and y > 0 and (x-1, y) not in vis:
            heapq.heappush(hp, (-(A[x-1]+B[y]), (x-1, y)))
            vis.add((x-1, y))

        if x > 0 and y > 0 and (x, y-1) not in vis:
            heapq.heappush(hp, (-(A[x]+B[y-1]), (x, y-1)))
            vis.add((x, y-1))

        C -= 1

    return res


A = [59, 63, 65, 6, 46, 82, 28, 62, 92, 96, 43, 28, 37, 92, 5, 3, 54, 93, 83]
B = [59, 63, 65, 6, 46, 82, 28, 62, 92, 96, 43, 28, 37, 92, 5, 3, 54, 93, 83]
# A.sort()
# B.sort()
# print(A)
# print(B)
C = 10
print(solve(A, B, C))
