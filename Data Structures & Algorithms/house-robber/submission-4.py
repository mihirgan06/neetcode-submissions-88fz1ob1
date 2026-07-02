class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
            Bottom up Iterative idea:

                Create dp array of size n

                we either take the current or skip but dp[i]  is the max of the two ideas
        '''
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        i = 2
        while i < n:
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
            i += 1
        return dp[-1]
        