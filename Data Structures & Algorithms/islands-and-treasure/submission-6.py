from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
            Given an mxn grid with three possible values
            1. -1 = water cell that can not be traversed
            2. 0 = treasure chest
            3. INF = a land cell that can be traversed

        '''
        INF = 2147483647
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(1,0), (0,1), (-1,0), (0, -1)]

        def bfs():
            #BFS from every treasure chest
            q = deque()
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 0:
                        q.append((r,c))
                        

            while q:
                row, col = q.popleft()
                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc

                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS):
                        continue
                    
                    if grid[nr][nc] != INF:
                        continue
                    grid[nr][nc] = grid[row][col] + 1
                    q.append((nr,nc))
            return grid
        bfs()

                    
                

                    
        