class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        '''
            given binary matrix GRID where 0s are land 1s represent rocks

            rocks cannot be traversed

            reutrn length of shortest path from top left corner to bottom right
            only traversing land cells
            bfs should auto return shortest path so no additional logic is needed there

        '''
        ROWS, COLS = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
            return -1 #not possible because either start or end is rocks
        q = deque()
        visited = set() #ensures we dont hit the same cell twice
        dirs = [[-1,0], [1,0], [0,1], [0, -1]]
        q.append((0,0))
        visited.add((0,0))
        length = 0


        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                if row == ROWS - 1 and col == COLS - 1:
                    return length
                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc
                    #explore in 4 dirs
                    if ( nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or (nr, nc) in visited or grid[nr][nc] == 1):
                        continue
                    q.append((nr, nc))
                    visited.add((nr, nc))
            length += 1
        return -1
                



                

        