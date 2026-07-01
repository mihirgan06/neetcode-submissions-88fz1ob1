class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
            Given an array of integers cost
            cost[i] = cost of taking a step from the ith flore of a staircase
            After payign the cost you can step to either i +1th floor or i + 2th floor

            you may choose to start at index 0 or index 1
            return min cost to reach the top ofthe staircase

            cost = [1,2,1,2,1,1,1]

            pay cost of 1, take two steps (total cost = 1)
            pay cost of 1, take two steps (total cost = 2)
            pay cost of 1, take two steps

            pay cost of 1 
            Total cost = 4

        '''
        cache = [-1] * len(cost)
        def dfs(i):

            if i >= len(cost):
                return 0
            if cache[i] != -1:
                return cache[i]
            cache[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return cache[i]
        return min(dfs(0), dfs(1))
        
        

        

        