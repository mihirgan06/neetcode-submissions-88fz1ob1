from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
            3 possible vals:
                1. -1; water cell cannot be traversed
                2. 0 = treasure chest
                3. INF = land cell taht can be traversed 2147483647
                
            replace each land cell with the distance to its nearest treasure chest
        4 possible dirs
        We need to bfs

        '''
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647

        ROWS, COLS = len(grid), len(grid[0])

        def bfs():
            q = deque()
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 0:
                        q.append((r,c))
            #expand from the treasure chests and change our INF cells to distance from the treasure chests
            while q:
                row, col = q.popleft()
                for dr, dc in dirs:
                    nr = row + dr
                    nc = col + dc
                    #boundary checks
                    if (nr < 0 or nc < 0
                        or nr >= ROWS or nc >= COLS):
                            continue
                    if grid[nr][nc] != INF:
                        continue
                    grid[nr][nc] = grid[row][col] + 1
                    q.append((nr, nc))
            return grid
        bfs()


            
            
