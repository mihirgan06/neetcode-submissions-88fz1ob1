class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        '''
            given m x n matrix grid 
            0 = sea
            1 = land

            move consists of walking from one land to another land or walking off the boundary
            outside dfs we need to get rid of the boundary cells as those cannot be walked into

        '''
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        num_enclaves = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0 or (r,c) in visited):
                return
            visited.add((r,c))

            #expand in 4 dirs
            dfs(r + 1,c)
            dfs(r - 1,c)
            dfs(r,c + 1)
            dfs(r,c - 1)
        
        for r in range(ROWS):
            if grid[r][0] == 1:
                dfs(r, 0)
            if grid[r][COLS - 1] == 1:
                dfs(r, COLS - 1)
        

        for c in range(COLS):
            if grid[0][c] == 1:
                dfs(0, c)
            if grid[ROWS - 1][c] == 1:
                dfs(ROWS - 1, c)

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    num_enclaves += 1
        return num_enclaves
                



        