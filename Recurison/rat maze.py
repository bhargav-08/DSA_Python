def ratmaze(matrix):
    answer = []
    vis = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]
    direction = "LRDU"

    def solve(x, y, d):
        if x == len(matrix)-1 and y == len(matrix)-1:
            answer.append(d[:])
            return

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and ny >= 0 and nx < len(matrix) and ny < len(matrix) and not vis[nx][ny] and matrix[nx][ny]:
                vis[nx][ny] = 1
                solve(nx, ny, d+direction[i])
                vis[nx][ny] = 0

    if matrix[0][0] == 1:
        solve(0, 0, "")
    return answer


m = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 1]
]

print(ratmaze(m))
