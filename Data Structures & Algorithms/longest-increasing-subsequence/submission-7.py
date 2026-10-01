class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
            given an integer array nums, return the length of the longest strictly increasing subsequence


            a subsequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the relative order


            nums = [9,1,4,2,3,3,7]

            1, 2, 3, 7
            have a loop with i have j follow behind if nums[i] > nums[j] we can increase our subsequence
            dp[i] = max strictly increasing subsequence ending at index i



        '''
        n = len(nums)
        dp = [1] * (n + 1)


        #intialize with 1s becasuse any individual character is a longest increasing subsequence of 1

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
                    

        