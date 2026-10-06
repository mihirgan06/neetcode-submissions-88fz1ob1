class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
            Given: integer array nums, nums[i] == amount of money the ith house has

            houses are arranged in a straigh tline
            cannot rob two adjacent houses


            return the max amount of money you can rob without alerting police

            dp[i] = max amount of money you can rob from the first i houses without alerting the police
        '''
        dp = [0] * (len(nums) + 1)
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 0:
            return 0   

        dp[0] = nums[0]


        dp[1] = max(nums[0], nums[1])

        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[len(nums) - 1]
        