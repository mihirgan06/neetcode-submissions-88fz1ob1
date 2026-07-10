class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
            Given array of integers cost, cost[i] cost from taking a step from the ith floor
            After paying cost you can eitehr step to the i + 1 or i + 2 floor

        '''
        cache = [-1] * len(cost)

        def dfs(i):
            if i >= len(cost):
                return 0
            cache[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))

            
            if cache[i] != -1:
                return cache[i]
            
            return cache[i]
        return min(dfs(0), dfs(1))
        