class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
            given matrix grid where grid[i] is either 0 or 1 
            0 = water
            1 = land
            island is defined as a group of 1s connected horizontally or vertically


            area = total sum of the 1s in an island
            we want to start dfs from the 1s and not go to any 0s as 0s dont provide any area
        '''

        max_area = 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visited or grid[r][c] == 0):
                return 0
            visited.add((r,c))
            return (1 + 
            dfs(r +1, c) + 
            dfs(r -1, c) + 
            dfs(r, c + 1) + 
            dfs(r, c - 1))


            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    max_area = max(max_area, dfs(r,c))
        return max_area
        