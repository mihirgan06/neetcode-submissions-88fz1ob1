class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
            you are given a rectangular island heights, heights[r][c] = height above sea level  
            at coordinate (r, c)



            the islands borders pacific ocean from top and left sides

            and borders the atlantic from the bottom and right sides

            water can flow in 4 directions
            - up, down, left, right
            from a cell to a neighboring cell with height equal or lower

            find all cells where water can flow from that cell to oth Pacific and atlantic oceans

            2D list each element is a list [r, c] of the row and column for the cell

            heights = [
            [4,2,7,3,4],
            [7,4,6,4,7],
            [6,3,5,3,6]
            ]


            [[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]

            you can flow into a cell thats shorter or equal to the height of the current cell

            Start from the pacific ocean everything in the bordering row and col can reach pacific
            Then start from all of THOSE nodes, find which other nodes can reach the pacific ocean

            Store this in a pacific set


            Do the same thing with teh atlantic ocean

            right side and bottom row
            the ones that can reach both we add to our result and return the result


            O(n * M)
            sicne we start from the borders we are actually going from cells of equal or GREATER heights

            n 


        '''
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        res = []

        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or r < 0 or c < 0 or r == ROWS or c == COLS or 
            heights[r][c] < prevHeight):
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res



        

        
            

        


        