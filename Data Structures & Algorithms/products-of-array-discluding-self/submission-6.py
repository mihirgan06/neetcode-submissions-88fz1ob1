class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
            given an array nums, return an array output where output[i] = product of all elements besides nums[i]
            nums = [1,2,4,6]
            naive approach for each element:
            multiply by each element and divide by each element

            Prefix/postfix approach:
            prefix can store the multiplcation of every element before nums[i]
            postfix can store the multiplcation ov every element after nums[i]
            





        '''
        n = len(nums)
        res = [1] * n
        #now we have a result array storing 1 for every element of nums
        prefix, postfix = 1, 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix

            postfix *= nums[i]
        return res

        