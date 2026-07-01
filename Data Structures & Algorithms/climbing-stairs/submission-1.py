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
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n - 2)
        
        
        