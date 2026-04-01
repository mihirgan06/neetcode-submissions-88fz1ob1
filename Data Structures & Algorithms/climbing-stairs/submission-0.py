class Solution:
    def climbStairs(self, n: int) -> int:
        #base cases 1 way to climb 1 stair, 2 to climb
        #2

        if n <= 2:
            return n
        first, second = 1, 2
        for i in range(3, n + 1):
            first, second = second, first + second
        return second
        