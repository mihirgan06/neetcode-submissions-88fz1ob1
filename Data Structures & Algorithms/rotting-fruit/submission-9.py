class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        given grid with 3 possible values
        1. 0 = empty cell
        2. 1 = fresh fruit
        3. 2 = rotten fruit

        every minute if a fresh fruit is hor/ver adjacent to a rotten fruit the fresh fruit also becomes rotten
        return the min number of minutes that must elapse until there are 0 fresh fruits remaining
        if impossible return -1

        start by adding all the rotten fruits to a queue, and all the 


        '''
        ROWS, COLS = len(grid), len(grid[0])
        time = 0
        num_fresh = 0
        DIRS = [[-1,0], [1,0], [0,1], [0, -1]]

        q = deque()
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
                    nr = row + dr
                    nc = col + dc
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 1):
                        continue
                    grid[nr][nc] = 2
                    q.append((nr, nc))
                    num_fresh -= 1
                    
                
            time += 1
        return time if num_fresh == 0 else -1
        
        



