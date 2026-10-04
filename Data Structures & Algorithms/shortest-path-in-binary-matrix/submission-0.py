class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        '''
            mxn matrix grid, return the length of the shortest clear path in the matrix

            if no clear path, return -1 failure case

            grid = [
            [0,1,0],
            [1,0,0],
            [1,1,0]
        ]

        all the visited cells of the path are 0 --> no need for visited set
        perform BFS on the graph --> implicitly returns the shortest path


        
        '''
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [[-1, 0], [1,0], [0, -1], [0,1], 
                [1,1], [-1,-1], [1,-1], [-1,1]]

        

        if grid[0][0] != 0 or grid[ROWS - 1][COLS - 1] != 0:
            return -1

        q = deque()
        q.append((0,0))
        dist = 1

        grid[0][0] = 1


        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                if row == ROWS - 1 and col == COLS - 1:
                    return dist

                for dr, dc in DIRS:
                    nr, nc = row + dr, col + dc
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 0:
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = 1
            dist += 1
        return -1
                

        
        