class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
            given an array of integers cost --> cost[i] = cost of taking step from ith floor

            after paying the cost you can either take the i + 1th floor or the i + 2th floor


            you amy choose to start at index 0 or index 1


            cost = [1,2,3]
            output = 2

            start at index 1 and pay cost of 2 to take two steps to the top


            we have to build a dp state of len(cost) + 1 since we want a metaphorical top 
            dp[i] = min cost to get to index i
            dp[0] = min cost to get to 0 is 0
            dp[1] = min cost to get to 1 is 0 since we can start from 1
            so we start iterating from 2

        '''
        n = len(cost)

        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 0

        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[n]


