class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
            DFS approach but compute area inside rather than incrementing count
            have a check to see if we found a new max area if so return that
        '''
        
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            #base case invalid dims:
            if r < 0 or c < 0 or r == len(grid) or c == len(grid[0]):
                return 0
            
            #base case 2: water/visited
            #if we run into water return immediately
            if grid[r][c] == 0 or (r, c) in visited:
                return 0
            visited.add((r, c))
            return (
                #initial node + recurse on 4 dirs
                1 + 
                dfs(r + 1, c) +
                dfs(r, c + 1) +
                dfs(r - 1, c) +
                dfs(r, c - 1)
            )
        area = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                
                area = max(area, dfs(r, c))

        return area

        