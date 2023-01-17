def rangeAddQueries(n: int, queries):

    mat = [[0 for _ in range(n)] for _ in range(n)]
    # print(mat)

    for (x1, y1, x2, y2) in queries:
        while x1 <= x2:
            temp = y1
            while temp <= y2:
                mat[x1][temp] += 1
                temp += 1
            x1 += 1

    return mat


queries = [[1, 1, 2, 2], [0, 0, 1, 1]]
print(rangeAddQueries(3, queries))
