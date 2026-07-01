class Solution:
    def climbStairs(self, n: int) -> int:
        '''
            top down DP
            given an integer n = number of steps to reacht he top of the staircase
            climb either 1 or 2 steps at a time
            Return the number of ways to reach the top

            For top down start with recursive and add cache

            Base case if nb = 1 --> 1 way, n = 2 --> 2
            for n = 3
            theres 1, 2
            then 2, 1
            then 1, 1, 1
        '''
        cache = [-1] * (n + 1)
        def dfs(i):

            if i <= 2:
                return i
            if cache[i] != -1:
                return cache[i]
            cache[i] = dfs(i-1) + dfs(i - 2)
            return cache[i]
        return dfs(n)
        
        
        