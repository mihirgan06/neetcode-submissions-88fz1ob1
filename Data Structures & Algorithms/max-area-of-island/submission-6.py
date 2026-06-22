class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
            Given a grid, grid[i] = 0 (water), 1 = land

            island is defined as a group of 1s connected horizontally or vertically

            area of an island is number of cells wwithin the island

            DFS in 4 dirs add up area and return that p calm
        '''
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        area = 0
        def dfs(r,c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return 0
            if grid[r][c] == 0 or (r,c) in visited:
                return 0
            visited.add((r,c))
            area = (1 +
                dfs(r + 1, c) +
                dfs(r, c + 1) +
                dfs(r - 1, c) +
                dfs(r, c - 1)
            )
            return area

        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r,c))
        return area
                

        