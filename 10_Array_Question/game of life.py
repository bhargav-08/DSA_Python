""" 289. Game of Life

The board is made up of an m x n grid of cells, where each cell has an initial state: live(represented by a 1) or dead(represented by a 0). Each cell interacts with its eight neighbors(horizontal, vertical, diagonal) using the following four rules(taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state. 

"""


def gameOfLife(board) -> None:
    """
    Do not return anything, modify board in-place instead.
    """

    m, n = len(board), len(board[0])
    for i in range(m):
        for j in range(n):
            cnt = sum(1 for x in (i-1, i, i+1)
                      for y in (j-1, j, j+1)
                      if 0 <= x < m and 0 <= y < n and board[x][y] & 1)

            if cnt == 3 or cnt-board[i][j] == 3:
                board[i][j] = board[i][j] | 2

    for i in range(m):
        for j in range(n):
            board[i][j] >>= 1


board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
gameOfLife(board)
print(board)
