class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
            given:
            - integer array nums
            Return:
            output where output[i] = product of all elements of nums except nums[i]


            Build prefix array from left side
            Build postfix array from right side

        '''

        prefix = 1
        postfix = 1
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
            
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
           
            
        