class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
            1. -1 water cell
            2. 0 = treasure chest
            3. INF = 2147483647

            Fill each land cell witht he distance to nearest treasure chest

            Multi-source bfs
            we can launch bfs from every treasure chest

            first put every treasure chest of value 0 into a queue
            then expand in 4 directions from that treasure chest
            only traversing over land cells
            increment the value for [nr][nc] as [row][col] + 1
        '''
        ROWS, COLS = len(grid), len(grid[0])

        q = deque()
        dirs = [[-1,0], [1, 0], [0, 1], [0,-1]]
        INF = 2147483647
        #put all the 0s ie treasure chests into a queue initially
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))

        
        while q:
            row, col = q.popleft()

            
            for dr, dc in dirs:
                nr, nc = row + dr, col + dc

                if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != INF):
                    continue
                    #increment distance to treasure chest for land cells
                q.append((nr, nc))
                    #add it to the queue cuz we need to process nr, nc
                grid[nr][nc] = grid[row][col] + 1
        
                


            

        