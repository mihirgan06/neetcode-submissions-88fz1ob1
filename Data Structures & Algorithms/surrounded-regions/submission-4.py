class Solution:
    def solve(self, board: List[List[str]]) -> None:
        '''
            given m x n matrix board 
            2 letters:
            1. 'X'
            2. 'O'
            capture regions that are surrounded

            any of the 'o' cells that are on the edge of the baord 
            replace 'O's with 'X's in place

            board = [
            ["X","X","X","X"],
            ["X","O","O","X"],
            ["X","X","O","X"],
            ["X","O","X","X"]
            ]

            we eneed to mark all the boundary Os as safe
            those cannot be touched



        '''

        ROWS, COLS = len(board), len(board[0])
        

        def dfs(r,c):
            #boundary checks or if grid[r][c] == X then we should skip it
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != "O"):
                return
            board[r][c] = "T"
            #expand in 4 dirs
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

            
            
        for r in range(ROWS):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][COLS - 1] == "O":
                dfs(r, COLS - 1)
        for c in range(COLS):
            if board[0][c] == "O":
                dfs(0, c)
            if board[ROWS - 1][c] == "O":
                dfs(ROWS - 1, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
                





            

            
        