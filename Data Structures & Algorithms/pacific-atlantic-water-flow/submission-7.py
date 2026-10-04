class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
            given rectangular island heights, heights[r][c] == height above sea level at coordinate (r,c)
            islands borders the Pacific from top and left isdes, and borders the atlantic from bottom and right sides


            water can flow in 4 dirs

            (up, down, left, right) with height equal or lower

            find all cells where water can flow fron that cell to both the pacific and atlantic ocean


            return as a 2d list 


            store a pacific ocean set and atlantic ocean
            dfs from those cells to find the cells that can be in both pac and atl
            since water can only flow into height <= since were moving in reverse 

        '''
        ROWS, COLS = len(heights), len(heights[0])
        pac = set()
        atl = set()
        res = []
        def dfs(r,c, visited, prevHeight):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visited or heights[r][c] < prevHeight:
                return
            

            visited.add((r,c))

            dfs(r + 1,c, visited, heights[r][c])
            dfs(r,c + 1, visited, heights[r][c])
            dfs(r - 1,c, visited, heights[r][c])
            dfs(r,c - 1, visited, heights[r][c])
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])
        for c in range(COLS):
            dfs(0,c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res




        