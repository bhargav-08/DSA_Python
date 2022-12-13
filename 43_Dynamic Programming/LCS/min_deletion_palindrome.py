from lcs import *


def minDeletion(s):
    answer = lcs2d(s, s[::-1])
    return len(s) - answer


if __name__ == "__main__":
    s = "agbcba"
    print(minDeletion(s))