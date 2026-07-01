class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
            Bottom up approach, start with the base cases and start i after that onyl
            Then move forward


        '''
        n = len(cost)
        dp = [0] * (n + 2)
        #fill backwards
        for i in range(n - 1, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
        
        return min(dp[0], dp[1])

