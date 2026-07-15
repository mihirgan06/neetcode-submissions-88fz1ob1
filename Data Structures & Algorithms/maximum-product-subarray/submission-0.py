class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
            Given an integer array nums, find subarray with the largest product and return product
            subarray = contiguous non-empty sequence of elements within an array

            nums = [2,4,-3,5]
            8

            nums = [-3,0,-2]
            output = 0
            
           kadanes algorithm:
           - typicall for max sum we can toss away a negative, but in prpduct the negative can turn out to be uyseful
           - two negatives can create a positive
           at nums[i] we have 3 choices
           - start a new subarray
           - extend the previous max prodct subarray

           [-2,3,4]
           current_max = -2, current_min = -2, result = -2

           then 3, start over: 
           current_max = 3
           current_min = -6
           result = 3

           then -4
           start over: -4
           prev max * -4 = -12
           prev min * -4  24
        '''
        current_max = nums[0]
        current_min = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]

            prev_max = current_max
            prev_min = current_min

            current_max = max(num, num * prev_max, num * prev_min)

            current_min = min(num, num * prev_max, num * prev_min)

            result = max(result, current_max)
        return result



            
