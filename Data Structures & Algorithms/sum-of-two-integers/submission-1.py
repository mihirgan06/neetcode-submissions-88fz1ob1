class Solution:
    def getSum(self, a: int, b: int) -> int:
        '''
            Get the sum of 2 integers without using +/- operators
            a = 1, b = 1
            a = 0001, b = 0001
            0001
            0001
            = 0010, 2,
            if we see two 1s in the same position we can always carry that over to the next place

            a = 4, b = 7
            a = 0100, b = 0111
            res = 11 which is 1011
            

            So we should xor the two numbers at each place, and if we see 1 in both matching places we carry it over
        '''
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        while b != 0:
            carry = ((a & b) << 1) & mask

            a = (a ^ b) & mask
            b = carry
        if a <= max_int:
            return a
        
        return ~(a ^ masl)