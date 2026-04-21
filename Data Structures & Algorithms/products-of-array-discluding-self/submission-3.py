class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
            prefix/postfix sum
            Result array
            Create a prefix suma nd postfix sum
            Multiply into the result array
        '''
        res = [1] * len(nums)

        prefix = 1
        postfix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            #iterate backwards though array
            res[i] *= postfix
            postfix *= nums[i]
        return res        