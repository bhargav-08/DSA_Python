def numIslands(grid) -> int:
    M, N = len(grid), len(grid[0])
    # code here

    def dfs(i, j):
        if 0 <= i < M and 0 <= j < N and grid[i][j] == 1:
            grid[i][j] = -1
            for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                dfs(i + dx, j + dy)

    islands = 0
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 1:
                islands += 1
                dfs(i, j)

    return islands


grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
print(numIslands(grid))
