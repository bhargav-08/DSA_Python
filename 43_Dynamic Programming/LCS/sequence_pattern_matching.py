from lcs import *


def seqPatternMatching(x, y):
    answer = lcs2d(x, y)
    return True if min(len(x), len(y)) else False


s1 = "axy"
s2 = "adxcpy"
print(seqPatternMatching(s1, s2))
