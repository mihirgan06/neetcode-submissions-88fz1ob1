class Solution:
    def climbStairs(self, n: int) -> int:
        '''
            Bottom up approach
            Iterate starting from stair 3 we can either take 2 steps or 1 step
            Start a dp array but set value at 1 and 2 to 1 and 2
        '''
        dp = [0] * (n + 2)
        dp[1] = 1
        dp[2] = 2
        i = 3
        while i <= n:
            dp[i] = dp[i -1] + dp[i - 2]
            i += 1
        return dp[n]


        