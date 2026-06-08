class Solution:
    from collections import deque
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
            BFS approach
                1. add the first land cell to the queue, iterate while queue not emoty
                2. RUn bfs while island is valid
                3. once we see water we need to remove from queue and restart


        '''
        ROWS, COLS = len(grid), len(grid[0])

        #initialize ROWS AND COLS FOR THE GRID
        visited = set()

        count = 0
        def bfs(r, c):
            q = deque()
            

            if grid[r][c] == '1' and (r, c) not in visited:
                q.append((r,c))
                visited.add((r,c))

                
            while q:
                row, col = q.popleft()
                directions = [
                    (row + 1, col), # down
                    (row - 1, col), # up
                    (row, col + 1), # right
                    (row, col - 1)  # left
                ]
                for nr, nc in directions:
                    #check bounds before adding for all 4 directions
                    if (
                    nr >= 0 and nc >= 0 and
                    nr < ROWS and nc < COLS and
                    grid[nr][nc] == "1" and
                    (nr, nc) not in visited
                    ):
                        q.append((nr, nc))
                        visited.add((nr, nc))
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in visited:
                    count += 1
                    bfs(r, c)
        return count





            




        

        
        