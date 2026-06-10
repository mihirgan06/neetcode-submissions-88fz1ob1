class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
            0 = empty
            1 = fresh
            2 = rotten
            rotten fruit does BFS and expands in 4 dirs at start of each new minute

            return number of mins till all fruits are rotten
            if no rotten fruit does not expand return -1
            we BFS from all rotten fruits so just add rotten fruits to queue
        '''
        
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        num_fresh = 0
        time = 0
        q = deque()
        for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 2:
                        #if rotten we add the coord to the queue

                        q.append((r, c))
                    elif grid[r][c] == 1:
                        num_fresh += 1

        def bfs():
            nonlocal num_fresh, time

            while q and num_fresh > 0:
                for i in range(len(q)):
                    row, col = q.popleft()
                
                    for dr, dc in dirs:
                        nr, nc = row + dr, col + dc
                        if (
                        nr < 0 or nc < 0 or
                        nr >= ROWS or nc >= COLS 
                        ):
                            continue

                        
                        if grid[nr][nc] == 0 or grid[nr][nc] == 2:
                            continue

                        if grid[nr][nc] == 1:
                            #if clean turn rotten
                            
                            grid[nr][nc] = 2
                            num_fresh -= 1
                            q.append((nr, nc))
                time += 1

        bfs()
        if num_fresh == 0:
            return time
        else:
            return -1
        
                    
                    






        