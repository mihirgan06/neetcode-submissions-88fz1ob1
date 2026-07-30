class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
            2D grid, where '1' = land, '0' = water count the number of islands

            island is formed by connecting adjacent lands horizontally or verticallyt surrounded by water
            we keep the island ocunt as far as tehre is land in 4 directions
        '''
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        num_islands = 0
        def dfs(r,c):
            if r >= ROWS or c >= COLS or r < 0 or c < 0:
                return 
            if (r,c) in visited or grid[r][c] == '0':
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
                    num_islands += 1
                

        return num_islands
        