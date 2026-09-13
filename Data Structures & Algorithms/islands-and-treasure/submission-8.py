class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
            given m x n grid 
            1. -1 water cell cannot be traversed
            2. 0 = treasure chest
            3. INF = a land cell that can be traversed

            fill each land with the distance from nearest treasure chest
            up down left right


            we can do BFS sicne were looking to replace distance
            no visited set

            two options
            1. we can start BFS from every treasure chest and find the shortest distance to land and replace that

            2. we can start BFS from every land cell to the nearest treasure chest


            lets go with option 1 as thats likely less BFS to run


        '''
        inf = 2147483647

        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))


        while q:
            row, col = q.popleft()
            for dr, dc in dirs:
                nr, nc = row + dr, col + dc
                if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == -1):
                    continue
                if grid[nr][nc] != inf:
                    continue
                q.append((nr, nc))

                grid[nr][nc] = grid[row][col] + 1
        return 
        