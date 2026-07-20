class Solution:
    def reverseBits(self, n: int) -> int:
        '''
            Given a 32bit int n, reverse bits
            reverse the bits of binary rep
            return n
            res all 32 bits as 0
        '''
        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res = res | ((bit) << (31 - i))
        return res
        

        