class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
            given an integer array nums, find a subarray that has the largest product and return the product

            dp[i] = max product from subarray from nums[:i]
            nums = [2,4,-3,5]
            2 * 4 = 8

            nums = [-3,0,-2]

            0

            we need to track both a min and max cuz if a massive min gets multiplied by another negative it becomes a huge positive



        '''
        n = len(nums)
        min_dp = [0] * n
        max_dp = [0] * n
        min_dp[0] = nums[0]
        max_dp[0] = nums[0]
        for i in range(1, n):
            max_dp[i] = max(nums[i], max_dp[i-1] * nums[i], min_dp[i - 1] * nums[i])
            min_dp[i] = min(nums[i], max_dp[i-1] * nums[i], min_dp[i - 1] * nums[i])
        return max(max_dp)