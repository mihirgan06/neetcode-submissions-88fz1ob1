class Solution:
    def climbStairs(self, n: int) -> int:
        '''
            given an integer n representing number of steps to reach top of staircase
            either 1 or 2 steps at a time
            create a cache array of size -1 * n + 1 initialized


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
            