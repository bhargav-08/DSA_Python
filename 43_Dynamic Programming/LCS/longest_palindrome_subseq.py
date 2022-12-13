from lcs import *


def longestPalindromeSubsequence(s):
    l = lcs2d(s, s[::-1])
    pprint(lcs2d.t)
    return l


# s = "agbcba"
s = "bbbab"
print(longestPalindromeSubsequence(s))
