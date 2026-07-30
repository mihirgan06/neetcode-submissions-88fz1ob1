class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
            Given a matrix grid, grid[i] is either 0 = water, 1 = land


            island is defined as a group of 1s connected horizontally or vertically
            count the area
            return max area


        ''' 
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0
        visited = set()

        def dfs(r, c):
            if (r >= ROWS or c >= COLS or r < 0 or c < 0):
                return 0
            if grid[r][c] == 0 or (r,c) in visited:
                return 0

            visited.add((r,c))
            max_area = (1 + 
            dfs(r + 1, c) +
            dfs(r - 1, c) +
            dfs(r, c + 1) +
            dfs(r, c - 1)
            )
            return max_area
        for r in range(ROWS):
            for c in range(COLS):
                max_area = max(max_area, dfs(r,c))
        return max_area
            

