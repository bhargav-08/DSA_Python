from lcs import *


def minInsertDeletion(a, b):
    length = lcs2d(a, b)
    deletion = len(a) - length
    insertion = len(b) - length

    return deletion, insertion


a = "heap"
b = "pea"
print(minInsertDeletion(a, b))
