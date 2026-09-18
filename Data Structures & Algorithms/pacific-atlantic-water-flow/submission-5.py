class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
            Given rectangular land heights
            heights[r][c] = height above sea level of the cell at (r,c)

            island borders the pacific from top left and borders atlantic from bottom right


            travel in 4 dirs
            form a cell to a neighbor with height equal or lower


            return a 2D list where each element is a list [r,c] representing the row and column of the cell
            heights = [
                [4,2,7,3,4],
                [7,4,6,4,7],
                [6,3,5,3,6]
                ]
            Approach:
            add everything in left col and top row to pac
            add everything in right col and bottom row to atl
            since we are working in reverse here we can only flow into rows of higher or equal height

            and then basically we return a result of all cells where cells are in both pac and atl





        '''
        ROWS, COLS = len(heights), len(heights[0])

        pac, atl = set(), set()
        res = []

        def dfs(r,c, visited, prevHeight):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visited or heights[r][c] < prevHeight):
                return
            visited.add((r,c))

            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])




        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS -1][c])
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res




        