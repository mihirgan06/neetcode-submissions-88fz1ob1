class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
            m x n grid where you are allowed to move either down or right at any point in time

            given 2 integers m and n return the number of possible unique paths that can be taken from top left to bottom right corner grid[m - 1][n - 1]


            dp[i][j] = number of ways to get from [0][0] to [i][j]
            

        
        '''
        dp = [[0] * n for i in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m -1][n -1]
                
        