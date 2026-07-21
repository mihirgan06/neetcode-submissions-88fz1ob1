class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
            Given an array nums w n integers [0, n]
            no duplicates, return the ingle numer in the range missing from nums
            nums = [1,2,3]
            return 0
            loop through n
        '''
        n = len(nums)
        xor = len(nums)
        for i in range(n):
            xor ^= i
            xor ^= nums[i]
        return xor

        
            

        