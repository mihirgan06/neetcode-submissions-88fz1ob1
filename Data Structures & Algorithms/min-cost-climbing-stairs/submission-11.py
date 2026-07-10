class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
            Bottom up approach:
                Create dp array of size len(cost)
                set dp[0] = cost[0], dp[1] = min(cost[0], cost[1])
                iterate i while less than n
                dp[i] = cost[i] + min(dp[i -1], dp[i -2])
        '''
        n = len(cost)
        dp = [0] * (n + 2)
        

        dp[0] = cost[0]
        dp[1] = min(cost[0], cost[1])
        for i in range(n-1, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
        return min(dp[0], dp[1])
        