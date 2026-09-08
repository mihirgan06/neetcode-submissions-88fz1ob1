class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
            Naive approach, muktiply all elems tgt and then divide by the element for each  element
            Optimal Approach

            nums = [1,2,4,6]
            [48,24,12,8]

            nums = [-1,0,1,2,3]
            [0,-6,0,0,0]
            prefix sum
            if any eklement is 0 then it becomes 0 for everything esle
            '''
        n = len(nums)
        prefix = 1 #solve from the leftside to i for output[i]

        postfix = 1 #solve from rightside to left for output i
        res = [1] * n
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        for i in range(n -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

            
                
                
            



            



        