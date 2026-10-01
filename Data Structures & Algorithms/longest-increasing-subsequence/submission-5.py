class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
            given an integer array nums return the length of the longest strictly increasing subsequence

            subsequence is a sequnce that can be derived from the given subsequence by deleting some or no elements without changing the order
            nums = [9,1,4,2,3,3,7]

            we cant sort because we cant change the order

            longest increasing subsequence: 1,2,3,7 == 4

            nums = [0,3,1,3,2,3]

            LIS = 0,1,2,3 ==> 4
            dp[i] = longest increasing subsequence ending at index i

            ie dp[3] would be the longest increasing subsequence ending at index i

            we dont have to actually create the subsequence


            initialize dp array with 1, at any index i there is at least a length of 1 if we just take the 1 value


        '''
        n = len(nums)
        dp = [1] * (n + 1)
        #initialize with 1 because any subsequence ending at index i always has at least a length of 1

        for i in range(len(nums)):
            for j in range(i):
                #j follows behind i
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
