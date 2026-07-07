class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
            Bottom up approach
        '''
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        i = 2
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        while i < len(nums):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])

            i += 1
        return dp[-1]

        