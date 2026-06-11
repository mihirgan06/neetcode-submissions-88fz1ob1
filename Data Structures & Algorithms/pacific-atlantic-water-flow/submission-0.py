class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
            Water can flow into the ocean if there exists SOME valid path
            water can only flow downhill or same level but not uphill
            any corner would automatically be valid

            Reverse DFS APproach:
                Rather than starting DFS from each cell, we start it only from the pacific/atlantic cells
                We check with 2 searches whether water could have flown into either of these two
        '''
        ROWS, COLS = len(heights), len(heights[0])
        #store rows and cols
        pacific = set()
        atlantic = set()


        def dfs(r, c, visited, prevHeight):
            
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visited or heights[r][c] < prevHeight:
                #out of bounds
                return
            visited.add((r,c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c]) #just the tip row
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c]) #just the bottom row
            
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0]) #left col
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1]) #right col
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r,c])
        return res

            


        