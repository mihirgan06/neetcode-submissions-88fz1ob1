class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
            given an m x n grid where you are allowed ot move either down or to the right at any point in time

            return the number of possible unique paths that can be taken from the top left grid[0][0] to bottom right grid[m-1][n-1]

            m = 3, n = 6
            down = grid[m +1][n]
            right = grid[m][n + 1]
            dp[i][j] = the max number of unique paths to get to coordinate [i][j] from [0][0]

            to get to dp[i][j] you can come from the left or above
            tehre is 1 way to get to every square in the first row and first column
            the rest of dp[i][j] for the double loop depends on the above state and left state


        '''

        dp = [[0] * (n) for i in range(m)]

        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1
        #the first row and first col should just be entirely 1s

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j - 1]
        
        return dp[m - 1][n - 1]

        

        

        
        

        