from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
            given a 2d Matrix grid
            3 possible values
            1. 0 = emoty cell
            2. 1 = fresh fruit
            3. 2 = rotten fruit

            every minute if a fresh fruit is horizontically or vertically

            Multi Source BFS
            - we want to start form the rotten fruits in a queue
            - increment time once we finish expanding from all the rotten fruit currently in the queue
            - return the time assuming no fresh fruits avialable
        '''
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        num_fresh = 0
        time = 0
        DIRS = [[-1,0], [1,0], [0, -1], [0,1]]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    num_fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
        
        while q and num_fresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in DIRS:
                    nr, nc = row + dr, col + dc

                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 1:
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = grid[row][col] + 1
                    num_fresh -= 1
                    
            time += 1
        return time if num_fresh == 0 else -1

        