class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
            Given an array of integers nums, find the subarray with the largest sum and return the sum

            Contiguous non-emoty sequence of elements within an array

            nums = [2,-3,4,-2,2,1,-1,4]

            start by taking 2, then we track our sums by either adding or not adding

            dont take = 2
            take = -1

            dont take = 2

            take = 3

            dont take = 2

            this problem can be done with DP or kadanes 

            for dp we could consider taking or leaving at each slot
            INSTEAD with kadanes we can consider a starting and future subsequence
            if our starting subsequence becomes negative we drop and start over as it will always be less than just F
            The clear observation is that we dont need to keep storing a dp array, bc all we care about is one value


        '''
        current_sum = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            current_sum += nums[i]
            current_sum = max(nums[i], current_sum)
            max_sum = max(current_sum, max_sum)
        return max_sum

