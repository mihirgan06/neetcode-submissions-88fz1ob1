from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
            -1 = cell that cannot be traversed
            0 = treasure chest
            INF = land cell that can be traversed

            From every single treasure chest add to queue and start BFS,
            change every land cell (marked as INF) to the distance
        '''

        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647
        

        def bfs():
            q = deque()
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 0:
                        q.append((r,c))
            while q:
                
                row, col = q.popleft()
                for dr, dc in dirs:
                    nr = row + dr
                    nc = col + dc
                    
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS):
                        continue
                    
                    if grid[nr][nc] != INF:
                        continue
                    #if it is inf
                    grid[nr][nc] = grid[row][col] + 1
                    q.append((nr,nc))
            return grid
        bfs()
            
