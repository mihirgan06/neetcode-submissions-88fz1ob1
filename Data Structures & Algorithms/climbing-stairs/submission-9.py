class Solution:
    def climbStairs(self, n: int) -> int:
        '''Bottom up approach:
            create a dp array of size n all 0s
            initially all 0s
            dp[0] = 0
            dp[1] = 1
        '''
        dp = [0] * (n + 1)
        #create a dp array of n elements all initialized to 0
        if n <= 2:
            return n
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        i = 3
        while i <= n:
            dp[i] = dp[i -1] + dp[i-2]
            i +=1
        return dp[n]
        