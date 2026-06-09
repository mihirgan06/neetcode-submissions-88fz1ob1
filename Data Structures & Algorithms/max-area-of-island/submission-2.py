class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
            Reattempting DFS approach to max area of island
            VALUES NOT STRING
            0 - water
            1 - land
            Same approach as num of islands except instead we add up the ones for the island rather than counting
            When we hit 0 end of island
            same boundaries

        '''
        ROWS, COLS = len(grid), len(grid[0])
        area = 0
        visited = set()

        def dfs(r, c) -> int:
            #first boundary checks and base case
            if r < 0 or c < 0 or r == len(grid) or c == len(grid[0]):
                return 0
            if grid[r][c] == 0 or (r, c) in visited:
                return 0
            visited.add((r,c))
            

            new_area = (
                1 + dfs(r + 1, c)
                + dfs(r, c + 1)
                + dfs(r -1, c)
                + dfs(r, c - 1)
            )
            return new_area
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))
        return area


            


        