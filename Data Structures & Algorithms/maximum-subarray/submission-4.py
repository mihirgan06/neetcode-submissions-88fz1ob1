class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
            Given array of integers nums, find the subarray with the largest sum and return the sum

            Subarray is contiguous non-empty sequence of elements within an array
            
            nums = [2,-3,4,-2,2,1,-1,4]

            we only need the prev value for dp not the full dp array
        '''

        curr_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            curr_sum += nums[i]
            curr_sum = max(nums[i], curr_sum)
            max_sum = max(max_sum, curr_sum)
        return max_sum
            
        