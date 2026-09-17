class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        '''
            Given a matrix GRID where 0s represent land adn 1s represent rocks

            return number of unique paths from top left corner to bottom right corner making sure
            all traversed cells are land cells

        '''

        ROWS, COLS = len(grid), len(grid[0])

        visited = set() #to ensure we dont revisit cells within same dfs

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or grid[r][c] == 1):
                return 0 

            if (r == ROWS - 1 and c == COLS - 1):
                return 1
            visited.add((r,c))
            
            num_paths = 0
            if grid[r][c] == 0:
                #can traverse in 4 dirs
                num_paths = (
                    dfs(r + 1, c) +
                    dfs(r, c + 1) + 
                    dfs(r - 1, c) +
                    dfs(r, c - 1)
                )
            visited.remove((r,c)) 
            return num_paths 
        return dfs(0,0)