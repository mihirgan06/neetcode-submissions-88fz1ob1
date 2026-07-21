class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
            Bottom up approach
        '''
        #at the beginning each spot in dp has a subsequence of 1
        n = len(nums) 
        dp = [1] * (n + 1)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)

                    

        