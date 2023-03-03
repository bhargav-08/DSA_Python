def solveSudoku(board) -> None:

    R = len(board)
    C = len(board[0])

    def possible(i, j, k):
        # check horizontal and vertical for that number
        for x in range(R):
            if board[i][x] == k or board[x][j] == k:
                return False

            if board[3*(i//3)+x//3][3*(j//3)+x % 3] == k:
                return False

        return True

    def solve(board):
        for i in range(R):
            for j in range(C):
                if board[i][j] == ".":

                    for k in range(1, 10):
                        if possible(i, j, str(k)):
                            board[i][j] = str(k)
                            if solve(board):
                                return True
                            else:
                                board[i][j] = "."
                    return False
        return True

    solve(board)


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                      ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
solveSudoku(board)
print(board)
