
def generateMatrix(n: int):
    cnt = 1
    res = [[0 for _ in range(n)] for _ in range(n)]
    left, right = 0, n-1
    top, bottom = 0, n-1

    while top <= bottom and left <= right:
        for i in range(left, right+1):
            res[top][i] = cnt
            cnt += 1

        top += 1

        for i in range(top, bottom+1):
            res[i] = cnt
            cnt += 1

        right -= 1

        if top <= bottom:
            for i in range(right, left-1, -1):
                res[i][bottom] = cnt
                cnt += 1

            bottom -= 1

        if left <= right:
            for i in range(bottom, top-1, -1):
                res[i][left] = cnt
                cnt += 1

            left += 1

    return res


print(generateMatrix(3))
