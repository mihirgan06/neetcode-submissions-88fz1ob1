class Solution:
    def climbStairs(self, n: int) -> int:
        '''
            given an integer n representing the number of steps to reach the top of the starircase


            step with eitehr 1 or 2 steps at a time


            n = 2

            2 ways to reach top of stair case

            1 + 1 = 2
            2 = 2




            n = 3

            1 + 1 + 1
            2 + 1
            1 + 2

            dp array dp[i] stores the number of ways to get to stair i

        ''' 
        if n <= 2:
            return n

        dp = [0] * (n + 1)
        
        dp[0] = 0 #0 ways to get to stair 0
        dp[1] = 1 #1 way to get to stair 1
        dp[2] = 2 #2 ways to get to stair 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

        