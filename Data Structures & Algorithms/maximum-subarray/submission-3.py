class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        Given an array of integers nums, find the subarray w the largest sum and return the sum
        subarray is contiguous non-emoty sequence of elemnets

        we dont need full dp array just the last number
        '''
        curr_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            curr_sum += nums[i]
            curr_sum = max(nums[i], curr_sum)
            max_sum = max(curr_sum, max_sum)
        return max_sum