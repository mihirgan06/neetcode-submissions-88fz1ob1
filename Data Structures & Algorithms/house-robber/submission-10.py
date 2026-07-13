class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
            Bottom up approach
            dp array of size n

        '''
        n = len(nums)
        dp = [0] * (n)
        dp[0] = nums[0]
        if len(nums) >= 1:
            dp[1] = max(nums[0], nums[1]) 
        if len(nums) == 1:
            return nums[0]
        i = 2
        
        while i < n:
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
            i += 1
        return dp[-1]

        