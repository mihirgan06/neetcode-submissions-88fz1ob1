class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
            given a rectangular island heights, where heights[r][c] = height above sea level at coord (r,c)

            islands borders the pacific ocean from top and left sides
                row = 0, col = all cols
                col = 0, row = all rows
            
            islands border the atlantic from right and bottom
                col = len(cols) - 1, all rows
                row = len(rows) - 1, all cols
            REVERSE DFS
            Spread DFS from those cells if the height is = or lower

            find all common sides for both pacific and atlantic
        '''
        pac, atl = set(), set()
        ROWS, COLS = len(heights), len(heights[0]) 
        
        def dfs(r, c, visited, prevHeight):
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visited or heights[r][c] < prevHeight:
                return
            visited.add((r,c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c]) #just the tip row
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c]) #just the bottom row
            
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0]) #left col
            dfs(r, COLS - 1, atl, heights[r][COLS - 1]) #right col
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r,c])
        return res   
            
        