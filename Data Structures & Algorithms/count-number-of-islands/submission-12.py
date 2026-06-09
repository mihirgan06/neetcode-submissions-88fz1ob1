class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
            DFS approach to Num Islands

            - given 2D grid ==> '1' = land, '0' == water
            island formed by connecting adjacent lands horizontally or vertically
            4 directions possible for island
            start at first coordinate and expand in 4 directions counting number of islands
            once we find a 0 the island is over and we return for that recursive call ==> base case
            or if we already visited the coord its wraps


        '''
        ROWS, COLS = len(grid), len(grid[0])
        num_islands = 0
        visited = set()

        def dfs(r, c):
            #r,c represents coordinates
            #first boundary check
            if r < 0 or c < 0 or r == len(grid) or c == len(grid[0]):
                return
            #base case 2: if we see water or the coordinate isnt in visited set return
            if grid[r][c] == '0' or (r, c) in visited:
                return
            visited.add((r, c))

            #expand in 4 dirs dfs
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





        