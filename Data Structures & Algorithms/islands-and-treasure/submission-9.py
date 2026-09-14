class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
            Given m x n grid initialized with 3 possible values
            1. -1 a water cell that cannot be traversed
            2. 0: a treasure chest
            3. INF: a land cell that can be traversed


            INF = land cell



            fill each land cell with the distance to the nearest treasure chest
            if a land cell cannot reach a trasure chest then th evalue can remain INF



            Traversed up down left right



            modify in place --> no visited set
            We traverse FROM the treasure chests ONLY
        '''
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        dirs = [[-1,0], [1, 0], [0, -1], [0,1]]
        INF = 2147483647

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        while q:
            row, col = q.popleft()
            for dr, dc in dirs:
                nr = row + dr
                nc = col + dc
                if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == -1):
                    continue
                if grid[nr][nc] != INF:
                    continue
                q.append((nr, nc))
                grid[nr][nc] = grid[row][col] + 1
        return

            

            
            
                    

        


        

        
        