import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Brute Force: Iterate through array with index i, compute product of the array except for that index elemnet
        #O(N^2)

        '''
        We can have an array of the size of inpiut array nums
        each element can legit be the multiplcation of the elements
        then for each element we divide it by nums[i]

        '''
        res = [1] * (len(nums))
        #prefix postfix solution
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1

        for i in range(len(nums) - 1, -1, -1):
            res[i] = postfix * res[i]

            postfix *= nums[i]
        return res


        
       
