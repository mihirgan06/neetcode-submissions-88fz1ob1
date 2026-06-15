class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
            Computing max area of island with dfs

        '''
        ROWS, COLS = len(grid), len(grid[0])

        area = 0
        visited = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS:
                return 0
            if grid[r][c] == 0 or (r,c) in visited:
                return 0
            visited.add((r,c))

            return (1 +
                dfs(r + 1, c) +
                dfs(r, c + 1) +
                dfs(r - 1, c) +
                dfs(r, c - 1))
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r,c))
        return area

        