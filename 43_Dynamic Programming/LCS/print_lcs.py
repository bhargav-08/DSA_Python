from lcs import *


def printSubSequence(x, y):
    lcs2d(x, y)
    table = lcs2d.t

    lx = len(table) - 1
    ly = len(table[0]) - 1

    answer = ""
    while lx != 0 or ly != 0:
        if x[lx - 1] == y[ly - 1]:
            answer += x[lx - 1]
            lx -= 1
            ly -= 1

        if x[lx - 1] != y[ly - 1]:
            if table[lx - 1][ly] > table[lx][ly - 1]:
                lx -= 1
            else:
                ly -= 1
    return answer[::-1]


x = "acbcf"
y = "abcdaf"

print(printSubSequence(x, y))
