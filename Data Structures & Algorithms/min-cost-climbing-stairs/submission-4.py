class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ''' 
            Given an integers cost where cost[i] = the cost of taking a step from th ith floor of a staricase

            After paying the cost --> i + 1 or i + 2

            return min cost to reach top
        '''
        n = len(cost)
        cache = [-1] * n
        def dfs(i):
            if i >= len(cost):
                return 0
            if cache[i] != -1:
                return cache[i]
            cache[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return cache[i]
        return min(dfs(0), dfs(1))

        