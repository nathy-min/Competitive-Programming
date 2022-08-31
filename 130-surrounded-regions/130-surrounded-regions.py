class Solution:
    def solve(self, board: List[List[str]]) -> None:

        rows = len(board)
        cols = len(board[0])
        def dfs(r,c):
            if r < 0 or not r < rows or c < 0 or not c < cols or board[r][c] == "X" or board[r][c] == "T":
                return
            board[r][c] = "T"
            dfs(r + 1,c)
            dfs(r - 1,c )
            dfs(r,c + 1)
            dfs(r, c - 1)
        for i in [0,rows-1]:
            for j in range(cols):
                if board[i][j] == "O":
                    dfs(i,j)

        for i in range(rows):
            for j in [0,cols-1]:
                if board[i][j] == "O":
                    dfs(i,j)
                
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "T":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
