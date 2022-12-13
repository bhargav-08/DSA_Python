from lcs import *


def printShortestSuperSequence(x, y):
    lcs2d(x, y)
    t = lcs2d.t

    i = len(x)
    j = len(y)
    answer = ""

    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            answer += x[i - 1]
            i -= 1
            j -= 1
        else:
            if t[i][j - 1] > t[i - 1][j]:
                answer += y[j - 1]
                j -= 1
            else:
                answer += x[i - 1]
                i -= 1
    while (i > 0):
        answer += x[i - 1]
        i -= 1
    while (j > 0):
        answer += y[j - 1]
        j -= 1
    return answer[::-1]


# a = "acbcf"
# b = "abcdaf"

a = "bbabacaa"
b = "cccababab"
print(printShortestSuperSequence(a, b))
