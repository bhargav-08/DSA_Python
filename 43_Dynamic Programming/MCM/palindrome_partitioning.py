# Problem ==> Minimum Partition such that all partition are palindrom itself
import sys

from functools import lru_cache


def isPalindrome(x):
    return x == x[::-1]


def minPalindromePartition(s, i, j):
    if i >= j or isPalindrome(s[i:j + 1]):
        return 0

    answer = float("inf")
    for k in range(i, j):
        temp = minPalindromePartition(s, i, k) + \
        minPalindromePartition(s, k + 1, j) + 1

        answer = min(answer, temp)
    return answer


def minPalindromePartitionMemo(s, i, j):
    if t[i][j] != -1:
        return t[i][j]
    if i >= j or isPalindrome(s[i:j + 1]):
        return 0

    answer = float("inf")
    for k in range(i, j):
        left = t[i][k] if t[i][k] != -1 else minPalindromePartitionMemo(
            s, i, k)
        right = t[k +
                  1][j] if t[k + 1][j] != -1 else minPalindromePartitionMemo(
                      s, k + 1, j)

        temp = 1 + left + right
        # temp = minPalindromePartition(s, i, k) + \
        # minPalindromePartition(s, k + 1, j) + 1

        answer = min(answer, temp)

    t[i][j] = answer
    return answer


def gap(s):
    length = len(s)
    p = [[False for _ in range(length)] for _ in range(length)]
    for g in range(length):
        i, j = 0, g
        while (j < length):
            if g == 0:
                p[i][j] = True
            elif g == 1:
                p[i][j] = s[i] == s[j]
            else:
                p[i][j] = True if s[i] == [j] and p[i +
                                                    1][j +
                                                       1] == True else False

            i += 1
            j += 1

    c = [[0 for _ in range(length)] for _ in range(length)]

    for g in range(1, length):
        i, j = 0, g
        while (j < length):
            if p[i][j]:
                c[i][j] = 0
            elif g == 1:
                c[i][j] = s[i] == s[j]
            else:
                answer = float("inf")
                for k in range(i, j):
                    left = c[i][k]
                    right = c[k + 1][j]
                    answer = min(answer, left + right + 1)
                c[i][j] = answer
            i += 1
            j += 1
    return c[0][-1]


s = "nitin"
s = "ababbbabbababa"
s = "aab"
s = "abccbc"
t = [[-1 for _ in range(len(s) + 1)] for _ in range(len(s) + 1)]

print(gap(s))

# print(minPalindromePartitionMemo(s, 0, len(s) - 1))
# print(minPalindromePartition(s, 0, len(s) - 1))
