class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
            Givne a nonempty array of nums
            every integer appears twice except for one
            Loop through nums
        '''
        res = 0
        for num in nums:
            res = num ^ res
        return res
        