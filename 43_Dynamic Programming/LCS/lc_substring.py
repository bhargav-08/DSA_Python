from pprint import pprint


def longestSubstring2d(x, y):
    t = [[0 for _ in range(len(y) + 1)] for _ in range(len(x) + 1)]
    answer = 0
    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            if x[i - 1] == y[j - 1]:
                t[i][j] = 1 + t[i - 1][j - 1]
                answer = max(answer, t[i][j])
            else:
                t[i][j] = 0
    return answer


def longestSubstringRecursive(i, j, count):
    if i == 0 or j == 0:
        return count
    if x[i - 1] == y[j - 1]:
        count = longestSubstringRecursive(i - 1, j - 1, count + 1)

    count = max(count, longestSubstringRecursive(i - 1, j, 0),
                longestSubstringRecursive(i, j - 1, 0))
    return count


x = "abcde"
y = "abce"
print(longestSubstring2d(x, y))
print(longestSubstringRecursive(len(x), len(y), 0))
