class Solution:
    from collections import deque
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
            BFS approach
                1. Initlaize ROWS, COLS as well as a visited set and global count for islands.
                2. WIthin BFS function create a queue
                3. If we see land, and the coordinate is not visited append to both the queue and the set
                4. While our queue is still valid
                5. Pop the coordinate and expand in 4 dirs
                6. Append if valid
                7. Global nested loop to try all values
                8. return total count


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





            




        

        
        