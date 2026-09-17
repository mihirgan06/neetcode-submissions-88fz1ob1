class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
            m x n grid initialized with 3 possible vals
            1. -1 = water cell cannot be traversed
            2. 0 = treasure chest
            3. INF = land cell that CAN be traversed
            Modify the graph in place with each land cell ast eh distance to its nearest trasure chest
            if a land cell cannot reach a treasure chest then it remains INF


            we can move in 4 dirs

        '''
        ROWS, COLS = len(grid), len(grid[0])

        q = deque()
        INF = 2147483647
        dirs = [[1,0], [-1,0], [0,-1], [0,1]]


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        #our queue will initally store all the treasure chests

        while q:
            row, col = q.popleft()
            for dr, dc in dirs:

                
                nr, nc = row + dr, col + dc

                
                if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != INF):
                    continue
                q.append((nr, nc))
                grid[nr][nc] = grid[row][col] + 1
        return

                
                


            


        

        