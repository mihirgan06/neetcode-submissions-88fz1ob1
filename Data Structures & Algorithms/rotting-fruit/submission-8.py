class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
            given 2d matrix grid
            3 possible values
            0 = empty cell
            1 = fresh fruit
            2 = rotten fruit
            every minute if a fresh fruit is hor/ver adj to a rotten the fresh also becomes rotten
            return min number of mins that must elapse until there are 0 frehs fruits remaining

            Approach:
            - initialize time and num_fresh

            - put all the rotten fruits into a queue
            - expand in 4 dirs from all the rotten fruits
            - at each orange level the num_fresh is decremented
            - at the end of each level the time is incremented
            this is auto the medium because we do bfs which guarantees shortest path

        '''
        ROWS, COLS = len(grid), len(grid[0])
        time, num_fresh = 0, 0
        dirs = [[-1,0], [1,0], [0, -1], [0,1]]
        q = deque()


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    #increment num_fresh
                    num_fresh += 1



        while q and num_fresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 1):
                        continue
                    grid[nr][nc] = 2 #turn the orange rotten
                    #add the next orange
                    q.append((nr, nc))
                    num_fresh -= 1
            time += 1
        

        return time if num_fresh == 0 else -1

            

        
        
        