from collections import deque


def islandPerimeter(grid) -> int:
    # find the start of island
    M, N = len(grid), len(grid[0])
    perimeter = 0

    def bfs(i, j):
        nonlocal perimeter
        q, vis = deque(), set()
        q.append((i, j))
        vis.add((i, j))

        while q:
            x, y = q.popleft()
            land = 0
            for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                if 0 <= x + dx < M and 0 <= y + dy < N and grid[x + dx][y + dy] == 1:
                    land += 1
                    if (x + dx, y + dy) not in vis:
                        q.append((x + dx, y + dy))
                        vis.add((x + dx, y + dy))
            perimeter += 4 - land

    for i in range(M):
        for j in range(N):
            if grid[i][j] == 1:
                bfs(i, j)
                break

    return perimeter


grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
print(islandPerimeter(grid))
