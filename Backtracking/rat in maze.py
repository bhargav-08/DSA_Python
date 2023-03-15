import sys

sys.setrecursionlimit(100000)


def findPath(m, n):
    # code here
    answer = []
    if m[0][0] == 0:
        return answer

    def solve(path, i, j):
        if i == n-1 and j == n-1:
            answer.append(path)
            return

        # Replacing first i and j with 0
        if i == 0 and j == 0:
            m[i][j] = 0

        for dx, dy, direction in [(-1, 0, "U"), (1, 0, "D"), (0, 1, "R"), (0, -1, "L")]:
            if i+dx >= 0 and j+dy >= 0 and i+dx < n and j+dy < n and m[i+dx][j+dy] != 0:
                m[i+dx][j+dy] = 0
                path += direction
                solve(path, i+dx, j+dy)

                m[i+dx][j+dy] = 1
                path = path[:-1]

    solve("", 0, 0)
    answer.sort()
    return answer


# n = 4
# m = [[1, 0, 0, 0],
#      [1, 1, 0, 1],
#      [1, 1, 0, 0],
#      [0, 1, 1, 1]]
n = 2
m = [[1, 1], [1, 1]]

print(findPath(m, n))
