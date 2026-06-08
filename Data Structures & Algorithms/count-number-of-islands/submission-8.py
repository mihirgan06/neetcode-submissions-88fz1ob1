class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
            We need to recurse in 4 dirs, up down (vertical) left right (horizontal)
            If we find a 1 is we increment num islands, once we find a 0 we stop counting islands for that


            we are given the 2d grid already
            We can attempt with dfs
        '''

        num_islands = 0
        ROWS, COLS = len(grid), len(grid[0])
        #define rows and cols
        visit = set()


        def dfs(r, c):
            #index for a point if this point on the grid is == 1 we have an island
            if r < 0 or c < 0 or r == len(grid) or c == len(grid[0]):
                return

            if grid[r][c] == '0' or grid[r][c] in visit:
                return
            
            visit.add((r, c))

            

            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)
            



            



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visit:
                    dfs(r, c)
                    num_islands += 1
        

        return num_islands
        