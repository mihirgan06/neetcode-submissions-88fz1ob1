class Solution:
    from collections import deque
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
            BFS approach to this problem
            we need queue and visited set
            set up dirs for traversal 
            calculate area in 4 dirs within snapshot of queue
        '''
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        area = 0


        def bfs(r, c):
            q = deque()
            visited = set()

            visited.add((r,c))
            q.append(r,c)
            res = 1
            while q:
                (row, col) = q.popleft()
                #once we pop from the queue explore all different dirs
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 0):
                        #if not valid
                        continue
                    q.append((nr, nc))
                    visited.add((nr, nc))
                    res += 1
            return res
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(area, bfs(r, c))
        return area


