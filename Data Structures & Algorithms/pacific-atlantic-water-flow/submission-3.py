class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
            givne heights, heights[r][c] = eight above sea level of the cell at coordinate (r,c)


            top and left sides = Pacific ocean
            bottom and right sides = Atlantic ocean

            Water can flow in 4 directions
            - up down left right

            water can flow in four directions from a cell to a neighboring cell with height equal or lower

            Approach
            - any cell bordering the oceans can flow into the ocean


            any cell in the first row and left most col is pacific obv
            any cell in last row and right most col is all atlantic
            then we find the overlap and those are the cells we return


            since we are actually starting from the oceans we are actually flowing into cells that are greater

            for dfs:
                pass in as attributes visited and prevHeight
                visited determines if the cell can be processed
                sicne we start from the border if the prevHeight is <= then the adjacent cell then water can flow into it


        '''
        ROWS, COLS = len(heights), len(heights[0])

        pac, atl = set(), set()
        res = []

        def dfs(r, c, visited, prevHeight):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visited or heights[r][c] < prevHeight):
                return 
            visited.add((r, c))

            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS -1][c])
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])
            
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res
                        
                    


        