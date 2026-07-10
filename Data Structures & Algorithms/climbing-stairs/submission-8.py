class Solution:
    def climbStairs(self, n: int) -> int:
        '''
            Given an integer n rep number of steps to reach top of staircase
            Climb w 1/2 steps at a time
            Return number of distinct ways to climb to the top of the staircase
            if n <= 2 --> return n

            Cache array of size n elements

        '''
        cache = [-1] * (n + 1)
        def dfs(i):
            if i <= 2:
                return i
            
            if cache[i] != -1:
                return cache[i]

            cache[i] = dfs(i - 1) + dfs(i - 2)
            
            return cache[i]
        return dfs(n)

        