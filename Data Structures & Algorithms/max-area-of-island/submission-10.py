class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
            BFS approach
        '''

        ROWS, COLS = len(grid), len(grid[0])

        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = deque()
        visited = set()
        area = 0


        def bfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS):
                return 0
            visited.add((r, c))
            q.append((r, c))
            area = 1
            while q:
                row, col = q.popleft()

                for dr, dc in dirs:
                    
                    nr, nc = row + dr, col + dc
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or (nr, nc) in visited or grid[nr][nc] == 0):
                        continue
                    q.append((nr, nc))
                    visited.add((nr, nc))
                    area += 1
            return area
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(area, bfs(r, c))
        return area
            
                


        