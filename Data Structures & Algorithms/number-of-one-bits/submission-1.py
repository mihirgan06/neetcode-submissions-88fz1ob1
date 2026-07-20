class Solution:
    def hammingWeight(self, n: int) -> int:
        '''
            Given an unsigned integer n
            return the number of 1 bits in binary rep
        
            n = 00000000000000000000000000010111
            res = 4
        '''
        res = 0
        for i in range(32):
            x = 1
            if x & n == 1:
                res += 1
            n >>= 1
        return res