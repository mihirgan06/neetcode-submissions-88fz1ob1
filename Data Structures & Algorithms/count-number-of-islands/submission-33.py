class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
            Given a 2D grid, grid where 1 land
            0 = water
            count and return the number of islands

            Approach:
            - Use DFS to expand form all 1s in 4 dirs
            - once we hit a 0 the island ends

        '''
        ROWS, COLS = len(grid), len(grid[0])
        count = 0
        visited = set()

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == '0' or (r,c) in visited):
                return 
            
            visited.add((r,c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in visited:
                    dfs(r,c)
                    count += 1
        return count

        