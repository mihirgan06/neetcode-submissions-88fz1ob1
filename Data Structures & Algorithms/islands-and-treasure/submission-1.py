class Solution:
    from collections import deque
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
            Given 2d grid (mxn):

                3 possible values:
                    -1 = water cell cannot be traversed
                    0 = treasure chest
                    INF = land cell that can be traversed
                Using BFS, we need ot edit the grid in place so that every INF is changed to be the distance to the land cell
                if we hit a -1 we cut the path there increment path till we get to -1
        '''
    
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647
        #initialize rows and cols
        ROWS, COLS = len(grid), len(grid[0])
        def bfs():
            #no parameters bc we dont start form a specific cell
            q = deque()
            #append starting coord
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 0:
                        q.append((r, c))
            
            while q:
                row, col = q.popleft()
                for dr, dc in dirs:
                    nr = row + dr
                    nc = col + dc
                    if (
                    nr < 0 or nc < 0 or
                    nr >= ROWS or nc >= COLS 
                    ):
                        continue
                    if grid[nr][nc] != INF:
                        continue
                    
                    grid[nr][nc] = grid[row][col] + 1
                    q.append((nr, nc))
            return INF
            
        bfs()
        

            
                    







                
                
        