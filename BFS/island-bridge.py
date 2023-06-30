""" 934. Shortest Bridge

You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.
"""


def shortestBridge(grid) -> int:
    vis = set()
    n = len(grid)

    def scan(i, j):
        # if min(i,j)<0 or max(i,j)==n:
        if i < 0 or i == n or j < 0 or j == n or grid[i][j] == 0 or (i, j) in vis:
            return 0
        vis.add((i, j))
        return 1 + scan(i+1, j) + scan(i-1, j) + scan(i, j+1) + scan(i, j-1)

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                found = scan(i, j)
                break
        if found:
            break

    q = dequre

    while 



grid = [[0, 1, 0], [0, 0, 0], [0, 0, 1]]
print(shortestBridge(grid))
