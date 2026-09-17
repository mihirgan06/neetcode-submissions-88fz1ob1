class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
            2d matrix grid:
            3 possible values
            1. 0 = empty cell
            2 1 = fresh fruit
            3. 2 = rotten fruit

            Approach:
            1. put al the rotten fruit into a queue
            2. decrement the number of fresh fruit after each orange is turned rotten
            3. increment time once full level is completed
            expand from all rotten fruits in palce convert all fresh fruit to rotten
            return time at the end

        '''
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        time, num_fresh = 0, 0
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for r in range(ROWS):
            for c in range(COLS):
                #in one loop well just quickly add all the rotten to a queue and also increment the num_fresh
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    num_fresh += 1
        
        while q and num_fresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()

                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 1):
                        continue
                    
                    grid[nr][nc] = grid[row][col] + 1

                    q.append((nr,nc))
                    num_fresh -= 1
            time += 1
        return time if num_fresh == 0 else -1




        