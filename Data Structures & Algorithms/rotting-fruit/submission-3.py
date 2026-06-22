from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
            2D grid:
                0 = empty cell
                1 = fresh fruit
                2 = rotten fruit

            BFS from the rotten fruit incrementing time and decreasing number of fresh fruit if there is a fresh fruit after each bfs
        '''
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        time = 0
        num_fresh = 0
        q = deque()
        def bfs():
            nonlocal num_fresh,time
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 2:
                        q.append((r,c))
                    if grid[r][c] == 1:
                        num_fresh += 1
            
            while q and num_fresh > 0:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    for dr, dc in dirs:
                        nr, nc = row + dr, col + dc

                        if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS):
                            continue
                        if grid[nr][nc] != 1:
                            continue
                        
                        grid[nr][nc] = 2
                        num_fresh -= 1
                        q.append((nr,nc))
                time += 1
        bfs()
        if num_fresh == 0:
            return time
        else:
            return -1