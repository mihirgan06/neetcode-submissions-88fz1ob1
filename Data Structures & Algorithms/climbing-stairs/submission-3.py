class Solution:
    def climbStairs(self, n: int) -> int:
        '''
            Bottom Up DP approach:
                Start at the base case and move from i = 2
                Iterate from i = 2 to n
        '''

        if n <= 2:
            return n
        dp = [0] * (n + 1)
        def dfs(n):
            nonlocal dp

            i = 3
            dp[1] = 1
            dp[2] = 2
            while i <= n:
                dp[i] = dp[i-1] + dp[i - 2]
                i += 1
            return dp[n]
        return dfs(n)



        