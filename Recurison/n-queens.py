from pprint import pprint
import copy


def NQueens(n):
    answer = []
    board = [["."] * n for _ in range(n)]

    rowchecker = {i: 0 for i in range(n)}
    lowerdiagonal = {i: 0 for i in range((2 * n - 2) + 1)}
    upperdiagonal = {i: 0 for i in range((2 * n - 2) + 1)}

    # def isPossible(nrows, ncols):

    # Check the straight
    # r = nrows
    # c = ncols - 1
    # while r >= 0 and c >= 0:
    #     if board[r][c] == "Q":
    #         return False
    #     c -= 1

    # Check the upper diagonal
    # r = nrows - 1
    # c = ncols - 1
    # while r >= 0 and c >= 0:
    #     if board[r][c] == "Q":
    #         return False
    #     c -= 1
    #     r -= 1

    # Check the lower diagonal
    # r = nrows + 1
    # c = ncols - 1
    # while r < n and c >= 0:
    #     if board[r][c] == "Q":
    #         return False
    #     c -= 1
    #     r += 1

    # return True

    def solve(c):
        if c == n:
            answer.append(["".join(item) for item in board])
            return

        for i in range(n):
            if not rowchecker[i] and not lowerdiagonal[
                    c + i] and not upperdiagonal[n - 1 + c - i]:
                board[i][c] = "Q"
                rowchecker[i] = "Q"
                lowerdiagonal[c + i] = "Q"
                upperdiagonal[n - 1 + c - i] = "Q"
                solve(c + 1)
                upperdiagonal[n - 1 + c - i] = 0
                lowerdiagonal[c + i] = 0
                rowchecker[i] = 0
                board[i][c] = "."

    solve(0)

    return answer


pprint(NQueens(4), indent=2, width=75)
