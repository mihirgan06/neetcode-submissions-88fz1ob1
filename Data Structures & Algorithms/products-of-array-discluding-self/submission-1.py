class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        We want to return the product of all elems in the array
        BESIDES a certain nums[i]

        [1,2,4,6]
        [(2*4*6), (1*4*6), (1*2*6), (1*2*4)]

        We are returning an array where EACH element is the product of the other elements apart from itself

        Initial Intuition:
        We multiply each element in the array and then divide by each element

        EFFICIENT:
        prefix and postfix sum
        
        '''
        #prefix = []
        #suffix = []
        #we dont even need a prefix postfix array, we can compute it within output
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1

        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res



        