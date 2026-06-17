from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
            Given a 2D matrix grid, each cell has one of 3 possible values
            1. 0 = empty cell
            2. 1 = fresh fruit
            3. rotten fruit

            Return number of minutes before every fruit is rotten
            BFS from every rotten fruit at each minute expand in 4 dirs

        '''
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        num_fresh = 0
        time = 0
        q = deque()

        def bfs():
            nonlocal num_fresh, time
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 2:
                        q.append((r,c))
                    if grid[r][c] == 1:
                        num_fresh += 1
            
            while q and num_fresh > 0:
                for i in range(len(q)):
                    row, col = q.popleft()
                    for dr,dc in dirs:
                        nr = row + dr
                        nc = col + dc

                        if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS):
                            continue
                        if grid[nr][nc] != 1:
                            continue
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            num_fresh -= 1
                            q.append((nr, nc))
                time += 1
        bfs()
        if num_fresh == 0:
            return time
        else:
            return -1
            
            

            
        