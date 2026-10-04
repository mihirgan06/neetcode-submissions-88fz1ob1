class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
            given an integer array nums, return the length of the longest strictly incresing subsequence

            subsequence is a sequence that can be derived from the given sequence by deleting some or no elements

            nums = [9,1,4,2,3,3,7]

            4
            [1,2,3,7]

            dp[i] = length of longest strictly increasing subsequence from the first i characters
            intialize with 1s NOT 0s because every individual character is its own strictly increasing subsequence








        '''
        dp = [1] * (len(nums))
        

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)
                


        