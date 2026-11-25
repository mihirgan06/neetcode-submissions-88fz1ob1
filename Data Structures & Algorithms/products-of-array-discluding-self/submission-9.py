class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
            given: integer array nims, return an output array 
            where output[i] = the prodiuct of all the elements in nums besides nums[i]

            nums = [1,2,4,6]

            res = [48, 24, 12, 8]
            easy soltuion is to multiply everything then divide by nums[i]

            without division operator


            we can build a prefix and postfix product
            start prefix and postfix at 1
            res array is 1 * len(nums)

            start res at prefix and change prefix *= nums[i] so we buold from the left




        '''
        res = [1] * len(nums)
        prefix = 1
        postfix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
            '''
                prefix array
                prefix = [1, 2, 8, ]

            '''
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

        