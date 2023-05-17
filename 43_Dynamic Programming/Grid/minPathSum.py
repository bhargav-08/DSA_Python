def minPathSum(grid) -> int:
    m, n = len(grid), len(grid[0])

    for y in range(1, n):
        grid[0][y] += grid[0][y-1]

    for i in range(1, m):
        for j in range(n):
            if j > 0:
                grid[i][j] = grid[i][j] + min(grid[i-1][j], grid[i][j-1])
            else:
                grid[i][j] = grid[i][j] + grid[i-1][j]

    return grid[m-1][n-1]


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print(minPathSum(grid))
