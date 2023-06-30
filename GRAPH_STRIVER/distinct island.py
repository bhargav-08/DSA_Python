# Geek for Geeks

def countDistinctIslands(grid) -> int:
    res = set()
    M, N = len(grid), len(grid[0])
    vis = [[0 for _ in range(N)] for _ in range(M)]
    temp = ()

    def dfs(ii, ij, i, j):
        nonlocal temp
        if i < 0 or j < 0 or i == M or j == N or vis[i][j] or grid[i][j] == 0:
            return
        temp = temp + ((i - ii, j - ij),)
        vis[i][j] = 1
        dfs(ii, ij, i, j + 1)
        dfs(ii, ij, i, j - 1)
        dfs(ii, ij, i + 1, j)
        dfs(ii, ij, i - 1, j)

        return temp

    for i in range(M):
        for j in range(N):
            if grid[i][j] and vis[i][j] == 0:
                temp = ()
                dfs(i, j, i, j)
                res.add(temp)

    return len(res)


grid = [[1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1]]
print(countDistinctIslands(grid))
