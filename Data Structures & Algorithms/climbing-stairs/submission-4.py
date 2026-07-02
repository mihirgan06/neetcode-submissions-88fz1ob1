class Solution:
    def climbStairs(self, n: int) -> int:
        '''
            Given an integer n =number of steps to reach the top of a staricase
            1 or 2 steps at a time
            return number of inique ways to reach the top
            Can either reach the top via 1 step or 2 steps
        '''
        #base case

        
        cache = [-1] * (n + 1)
        def dfs(i):
            if i <= 2:
                return i
            cache[i] = dfs(i - 1) + dfs(i - 2)
            if cache[i] != -1:
                return cache[i]
            return cache[i]
        return dfs(n)
        


        
        