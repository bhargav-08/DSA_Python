from lcs import *


def shortestCommonSupersequence(x, y):
    length = lcs2d(x, y)
    return len(x) + len(y) - length


x = "aggtab"
y = "gxtxayb"
print(shortestCommonSupersequence(x, y))
