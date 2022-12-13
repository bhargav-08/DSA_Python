from sys import maxsize


def mcm(arr, i, j):
    if i >= j:
        return 0

    answer = maxsize
    for k in range(i, j):
        tempanswer = mcm(arr, i, k) + \
        mcm(arr, k + 1,j) + \
        (arr[i] * arr[j] * arr[k])

        answer = min(answer, tempanswer)

    return answer


def mcmMemo(arr, i, j):
    if i >= j:
        return 0

    if t[i][j] != -1:
        return t[i][j]
    answer = maxsize
    for k in range(i, j):
        tempanswer = mcm(arr, i, k) + \
        mcm(arr, k + 1,j) + \
        (arr[i] * arr[j] * arr[k])

        answer = min(answer, tempanswer)

    t[i][j] = answer
    return answer


arr = [40, 20, 30, 10, 30]
# print(mcm(arr, 1, len(arr) - 1))

t = [[-1 for _ in range(len(arr) + 1)] for _ in range(len(arr) + 1)]
print(mcmMemo(arr, 1, len(arr) - 1))
