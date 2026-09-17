class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
            Given 2d grid where '1' = land
            '0' = water 
            count and return number of islands
        '''
        ROWS, COLS = len(grid), len(grid[0])
        num_islands = 0
        visited = set()
        def dfs(r, c):

            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or grid[r][c] == '0'):
                return
            visited.add((r, c))

            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in visited:
                    dfs(r, c)
                    num_islands += 1
        return num_islands
                


        