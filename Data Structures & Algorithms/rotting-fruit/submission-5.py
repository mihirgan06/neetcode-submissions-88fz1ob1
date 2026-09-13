from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
            given 2D matrix grid, eachcell has 3 possible values

            0 = empty
            1 = fresh fruit
            2 = rotten fruit
            every minute if a fresh fruit is horizontally or vertically adjacent to a rotten fruit
            the fresh fruit also becomes rotten

            return num minutes to make the entire grid rotten
            multi source bfs from every rotten fruit
            increment time at every bfs
            update the fresh fruit adjacent to rotten
            modify grid in place


        '''
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        time = 0
        num_fresh = 0
        
        dirs = [[-1,0], [1, 0], [0, -1], [0, 1]]


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    num_fresh += 1
                    
        def bfs():
            nonlocal time, num_fresh
            while q and num_fresh > 0:
                for i in range(len(q)):
                    row, col = q.popleft()

                    for dr, dc in dirs:
                        nr, nc = row + dr, col + dc
                        if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 1):
                            continue
                        grid[nr][nc] = 2
                        num_fresh -= 1

                        q.append((nr, nc))
                time += 1
        bfs()
        return -1 if num_fresh > 0 else time
                        
                        
                        
                        











        