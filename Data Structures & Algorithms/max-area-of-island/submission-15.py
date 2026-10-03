class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
            you are given a matrix grid, grid[i] is either 0 or 1
            island is a group of 1s connected hor/ver


            expand in 4 dirs append all 1s to area return max area
        '''
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def dfs(r,c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0 or (r,c) in visited:
                return 0
            

            visited.add((r,c))
            return 1 + (
                dfs(r +1, c) +
                dfs(r - 1, c) +
                dfs(r, c + 1) +
                dfs(r, c - 1)

            )
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    max_area = max(max_area, dfs(r,c))
        return max_area


        