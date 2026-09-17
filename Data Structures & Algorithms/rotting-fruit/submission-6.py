class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
            given a 2d matrix grid each cell has one of 3 possible values
            0 = empty
            1 = fresh
            2 = rotten

            every minute if a fresh is hor/ver to a rotten fruit, the fresh fruit becomes rotten

            return the min number of minutes that must elapse until there are zero fresh fruits remaining

            Approach:
            - keep track of time and the number of fresh fruits
            - at every full expansion of bfs time gets incremented by one and num_fresh gets decremented

            - put all the rotten fruits into the queue
            - expand in 4 dirs from all the rotten fruits turning the whole grid rotten

            O(m * n) tiem complexity since we iterate over all cells in the grid


        '''


        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        time, num_fresh = 0, 0
        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        #increment the number of fresh fruits
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    num_fresh += 1
        
        while q and num_fresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc
                
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 1 ):
                        continue
                    num_fresh -= 1
                    grid[nr][nc] = 2
                    q.append((nr, nc))
                    
            time += 1
            
        return time if num_fresh == 0 else -1
                    
            


        