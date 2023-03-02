def solveNQueens(self, n: int) -> List[List[str]]:
    answer = []
    board = [["." for _ in range(n)] for _ in range(n)]

    def possible(i,j): 
        # Check horizontal and vertical 
        for k in range(n):
            if board[i][k]=="Q" or board[k][j]=="Q":
                return False

        # Check Diagonal position
        for dx,dy in [(-1,-1),(-1,+1),(+1,-1),(+1,+1)]:
            x = i+dx
            y = j+dy
            while (x>=0 and y>=0 and x<n and y<n):
                if board[x][y]=="Q":
                    return False
                x+=dx;y+=dy;

            return True
        

    def solve(j):
        if j==n:
            print("Reached")
            answer.append(board.copy())
            return 
        
        for i in range(n):
            if board[i][j]=="." and possible(i,j):
                board[i][j]="Q"
                solve(j+1)
                board[i][j] = "."
            return

    solve(0)
    return answer