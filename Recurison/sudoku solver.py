from pprint import pprint


def sudokuSolver(board):

    def isPossible(i, j, k):
        for r in range(9):
            if board[i][r] == k:
                return False
            if board[r][j] == k:
                return False
            if board[(i // 3) * 3 + (r // 3)][(j // 3) * 3 + (r % 3)] == k:
                return False
        return True

    def solver(board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    for k in range(1, 10):
                        if isPossible(i, j, str(k)):
                            board[i][j] = str(k)
                            if solver(board):
                                return True
                            else:
                                board[i][j] = "."

                    return False
        return True

    solver(board)
    pprint(board)


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
sudokuSolver(board)
