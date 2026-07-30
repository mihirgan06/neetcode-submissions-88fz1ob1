from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]
        max_area = 0

        def bfs(r,c):
            q = deque()
            grid[r][c] = 0
            q.append((r,c))
            area = 1
            while q:
                r,c = q.popleft()
                for dr, dc in (dirs):
                    nr = r + dr
                    nc = c + dc
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 0):
                        continue
                    grid[nr][nc] = 0
                    q.append((nr, nc))
                    area += 1
            return area
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, bfs(r,c))
        return max_area