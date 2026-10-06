class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
            Given: array nums, return an output, output[i] = product of all elements of nums except nums[i]

            nums = [1,2,4,6]
            [48,24,12,8]
            nums = [-1,0,1,2,3]
            anything multiplied by 0 is 0

            Brute Force:
            - multiply all the numbers together
            - divide by every element easy

            Optimal without using division operator:
            - prefix/postfix approach
            - start with an array initialized to 1
            prefix and postfix 1
            start from right and left for prefix and postfix
            multiply them tgt


        '''
        output = [1] * len(nums)

        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        return output
            
        