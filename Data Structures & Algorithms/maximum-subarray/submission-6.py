class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
            given an int array nums, find the subarray with the larget sum and return the sum
            subarray is a contiguous non-empty sequnce of elements within an array

            nums = [2,-3,4,-2,2,1,-1,4]
            

            running sum:
            7 total start to end

            5 from -3

            8 starting from 4
            Brute force we start from everys lot in nums and keep computing a max sum and return the sum from that
            keep computing every single subarray until the end
            then repeat for the next number
            O(n^2)

            Linear Solution:
                the negative numbers contribute nothing
                we can IGNORE the negative prefix before the positives
                if the prefix before a negative we should shift our window we want to remove the negative prefix
                as we compute the total sum get rid of the negative prefix






        '''
        maxSub = nums[0]
        curSum = 0
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub
        
        