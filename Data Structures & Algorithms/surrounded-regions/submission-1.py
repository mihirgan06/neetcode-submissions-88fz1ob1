from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        '''
            Given an m x n matrix board with letters 'X' and 'O' capture regions that are surrounded:
                - Connect: A cell is connected to adjacent cells horizontally/vertically
                - Region: to form a region connect every '0' cell
                - Surround: a region is surrounded if none of the '0' cells in the region are on the edge of the board

            To capture a surrounded region, replace all 0s with Xs in place

            board = [
                ["X","X","X","X"],
                ["X","O","O","X"],
                ["X","X","O","X"],
                ["X","O","X","X"]
            ]
            Output: [
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","O","X","X"]
            ]

            We can BFS from every 0 if its not a border cell convert all the 0s to Xs

        '''
        ROWS, COLS = len(board), len(board[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs():
            q = deque()
            for r in range(ROWS):
                for c in range(COLS):
                    if board[r][c] == 'O' and (r == 0 or c == 0 or r == ROWS - 1 or c == COLS - 1):
                        #mark all border 0s as safe
                        
                        q.append((r,c))
                        board[r][c] = "S"
            while q:
                row, col = q.popleft()
                for dr, dc in dirs:
                    nr = row + dr
                    nc = col + dc
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS):
                        continue
                    if board[nr][nc] != 'O':
                        #if our cell is an x we wanna just like skip the loop
                        continue
                    board[nr][nc] = 'S'
                    q.append((nr,nc))
        bfs()
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == "S":
                    board[r][c] = "O"
        




        