class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
            given a 2D grid grid, '1' = land, '0' = water

            count and return the number of islands

            island is connected adjacent lands horizontally or vertically and surrounded ny wter


        '''

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        num_islands = 0

        def dfs(r,c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == '0' or (r,c) in visited):
                return
            
            visited.add((r,c))
            dfs(r + 1,c)
            dfs(r,c + 1)
            dfs(r - 1,c)
            dfs(r,c - 1)
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c] == '1':
                    dfs(r,c)
                    num_islands +=1
        return num_islands





        