class Solution:
    def hammingWeight(self, n: int) -> int:
        '''
            Given integer n unsigned
            return the number of 1 bits in its binary representation
            we dont loop since we want O(1) time

        '''

        res = 0
        for i in range(32):
            res += n & 1
            n >>=1
        return res

        
        