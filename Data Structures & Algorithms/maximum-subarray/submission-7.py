class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
            given an array of integers nums, find the subarray with the largest sum adn return the sum

            subarray = contiguous non-empty sequence of elements
            nums = [2,-3,4,-2,2,1,-1,4]

            since its sum, a negative value only hurts us

        '''
        curr_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            if curr_sum < 0:
                curr_sum = 0

            curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)
        return max_sum
                
                
