class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
            givne heights, heights[r][c] is the height above sea level at (r,c)
            island borders pacific from top and left
            boarders atlantic from the bottom and right

            water can flow in 4 dirs to a cell with height equal or lower


            we can start dfs from the pac and atl cells


            [4,2,7,3,4],
            [7,4,6,4,7],
            [6,3,5,3,6]
            ]

            since we start from the borders we can only flow into cells that are higher or equal since we move in reverse

            add everything to pac and atl

            2 sets
            then if the cell is in both pac AND atl then thats a cell that can reach both


            return a res array where append those points
        '''


        ROWS, COLS = len(heights), len(heights[0])


        pac, atl = set(), set()
        res = []
        

        def dfs(r, c, visited, prevHeight):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visited or heights[r][c] < prevHeight):
                return
            visited.add((r,c))
            #expand in 4 dirs


            dfs(r + 1,c, visited, heights[r][c])
            dfs(r - 1,c, visited, heights[r][c])
            dfs(r,c + 1, visited, heights[r][c])
            dfs(r,c - 1, visited, heights[r][c])



        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS -1, atl, heights[r][COLS - 1])
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res

        
        
            

        