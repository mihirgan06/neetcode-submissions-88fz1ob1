class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cache = [-1] * (n + 1)

        def dfs(i):
            if i < 2:
                return 0
            
            if cache[i] != -1:
                return cache[i]
            
            cache[i] = min(dfs(i - 1) + cost[i -1], dfs(i - 2) + cost[i - 2])
            return cache[i]
        return dfs(n)


        