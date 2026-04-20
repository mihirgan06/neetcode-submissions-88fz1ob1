class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
            Given an array nums, return an array output where output[i] =
            product of all elements of nums except nums[i]

            We know the product is an integer

            Initial intution
            For each integer, take the product and divide it by each i in nums

            But this uses the division operator

            To use without division operator:
                Prefix-Postfix solution


            prefix product up to i
            Postfix product from right to i

            Multiply the prefix and postfix product

        '''
        res = [1] * len(nums)
        prefix = 1
        postfix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
            
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        
        return res