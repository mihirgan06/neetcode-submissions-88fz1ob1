class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
            given an array nums, where nums[i] represents the amount of numebr the ith house has

            the houses are arranged in a straight line

            you are planning to rob money from the houses but cannot rob 2 adjacent houses

            nums = [1,1,3,3]
            rob nums[0] + nums[2]

            1 + 3 = 4

            nums = [2,9,8,3,6]

            2 + 8 + 6


            dp[i] = max amount of money 
        '''

        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        dp = [0] * n
        if len(nums) < 1:
            return dp[0]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        return dp[n - 1]
        