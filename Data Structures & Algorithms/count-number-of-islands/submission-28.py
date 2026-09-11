class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
            Given a 2d graph where 1 represents land and 0 represents water
            count and return the number of islands

            if you find a 1 expan d in 4 directions uyntil you find 0

        '''
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        num_islands = 0

        def dfs(r, c):

            if (r < 0 or c < 0 or r >= ROWS or c >= COLS):
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
                        

            
                

        