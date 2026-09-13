class Solution:
    def solve(self, board: List[List[str]]) -> None:
        '''
            Given an m x n board with letters 'X' and 'O' capture regions that are surrounded

            cell is connected to adjacent cells horizontally or verticallty
            region to form a region connect every 'O' cell
            surround: a region is surrounded if none of the 'O'  cells in that region are on the edge of the board
            modify in place everytime we can expand purely from the Os
            if the O is in the bordering cell thenb it cant be modified

            expand in 4 directions from all the Os that arent a corner O
            so maybe move 1 is to isolate all the corner Os as those are not surroundable,




        '''
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != "O"):
                #out of bounds check
                return
            board[r][c] = "T"

            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)

        for c in range(COLS):
            if board[0][c] == "O":
                dfs(0, c)
            

            if board[ROWS - 1][c] == "O":
                dfs(ROWS - 1, c)
        

        for r in range(ROWS):
            if board[r][0] == "O":
                dfs(r, 0)
            

            if board[r][COLS - 1] == "O":
                dfs(r, COLS - 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
            






        