from collections import deque


def orangesRotting(grid) -> int:
    M = len(grid)
    N = len(grid[0])
    q = deque()
    t = 0

    for i in range(M):
        for j in range(N):
            if grid[i][j] == 2:
                q.append((i, j, t))
                break

    while q:
        x, y, t = q.popleft()
        # ans = t
        for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            i = x+dx
            j = y+dy
            if i >= 0 and j >= 0 and i < M and j < N and grid[i][j] == 1:
                grid[i][j] = 2
                q.append((i, j, t+1))

    for i in range(M):
        for j in range(N):
            if grid[i][j] == 1:
                print(grid[i][j])
                return -1

    return t


grid = [[2, 2, 2, 1, 1]]
# print(orangesRotting(grid))

