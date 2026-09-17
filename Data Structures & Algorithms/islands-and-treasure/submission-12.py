class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
            given m x n grid w 3 possible values
            1. -1 = water cell that cannot be traversed
            2. 0 = treasure chest
            3. INF = land cell that can be traversed


            multi-source BFS
            1. bump every treasure chest into a queue
            2. within bfs expand in 4 dirs from the treasure chests
            3. if the new row, new col is a land cell we increment the value with grid[r][c] + 1 indicating the increased distance

        '''

        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        DIRS = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        INF = 2147483647
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        

        while q:
            row, col = q.popleft()

            for dr, dc in DIRS:
                nr, nc = row + dr, col + dc

                if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != INF):
                    continue
                grid[nr][nc] = grid[row][col] + 1
                q.append((nr, nc))
                
                

        