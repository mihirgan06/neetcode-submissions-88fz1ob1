class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
            Given an integer array where nums[i] is the amount of money in ith house
            planning to rob but cant rob adjacent house
            max amount without robbing adjacent houses


            either we take or skip nums[i]

            take: nums[i] + nums[i - 2]
            skip: nums[i - 1]
        
            iterate left to right
        '''
        dp = [0] * (len(nums))
        dp[0] = nums[0]
        if len(nums) == 1:
            return nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            take = nums[i] + dp[i - 2]
            skip = dp[i - 1]
            dp[i] = max(take, skip)
        return dp[-1]
