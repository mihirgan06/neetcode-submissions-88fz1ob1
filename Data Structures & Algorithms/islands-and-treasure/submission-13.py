class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
            given an m x n grid, with 3 possible values


            1. -1 = water cell that cannot be traversed
            2. 0 = treasure chest

            3. INF = land cell that can be traversed


            fill each land cell with the distance to its nearest treasure chest

            start BFS from only the treasure chests and alter the land cells to the distance from the treasure chests
        '''
        ROWS, COLS = len(grid), len(grid[0])
        
        q = deque()
        DIRS = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        #add all the treasure chests to the queue
        INF = 2147483647
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        while q:
            row, col = q.popleft()
            for dr, dc in DIRS:
                nr, nc = row + dr, col + dc
                if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != INF):
                    continue
                grid[nr][nc] = grid[row][col] + 1
                q.append((nr, nc))
            
                
                
        

            


        


        

