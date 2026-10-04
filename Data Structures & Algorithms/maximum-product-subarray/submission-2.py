class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
            Given:
            - integer array nums, find a subarray that has the largest product return this product

            subarray = contiguous non-empty sequence of elements within an array

            nums = [2,4,-3,5]

            max product = 2 * 4

            nums = [-3,0,-2]
            0 MUST BE CONTIGUOUS


            dp[i] = max product from the first i characters ending at i


            we need to keep track of the min product
            and the max product
            if the min product gets multiplied by another negative it can end up becoming a large positive
        '''
        max_dp = [0] * len(nums)
        min_dp = [0] * len(nums)


        max_dp[0] = nums[0]
        min_dp[0] = nums[0]

        for i in range(1, len(nums)):
            min_dp[i] = min(nums[i], max_dp[i-1] * nums[i], min_dp[i - 1] * nums[i])
            max_dp[i] = max(nums[i], max_dp[i-1] * nums[i], min_dp[i - 1] * nums[i])
        return max(max_dp)
            

        