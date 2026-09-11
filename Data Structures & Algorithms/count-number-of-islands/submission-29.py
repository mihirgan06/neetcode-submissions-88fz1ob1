class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
            BFS approach use a queue and a visited array

        '''
        ROWS, COLS = len(grid), len(grid[0])

        q = deque()
        visited = set()
        num_islands = 0
        dirs = [[1,0], [-1,0], [0, 1], [0,-1]]


        def bfs(r,c):
            visited.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                for dr, dc in dirs:

                    nr, nc = dr + row, col + dc
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == '0' or (nr,nc) in visited):
                        continue
                    
                    q.append((nr, nc))
                    visited.add((nr, nc))
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r,c)
                    num_islands += 1
        return num_islands
                




            
        