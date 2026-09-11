class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
            mxn grid where you can move either down or to the right at any point

            Given two integers m and n, return the number of possible unique paths that can take you from
            top left corner of the grid


            grid[0][0]

            to bottom right
            grid[m - 1][n - 1]

            possible directions:
            - down 
                Increment row
            - right
                increment column


            dp[i][j] the number opf possible paths using i squaresa from i squares horizontally and j squares vertically


            so we can create a 2d dp array of size m x n, for each size have the unique paths




            target = grid[m -1][n - 1]
            m = 3, n = 6

            _ _ _
            _ _ _
            _ _ _
            _ _ _
            _ _ _
            _ _ _


            start at 0, 0
            move from either the right or down


            '''
        dp = [[0] * n for i in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1
            
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j - 1] # you can come from the left or above
            

        return dp[m - 1][n - 1]

        