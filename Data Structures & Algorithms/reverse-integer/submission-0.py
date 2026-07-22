class Solution:
    def reverse(self, x: int) -> int:
        '''
            Given a signed 32-bit integer x
            return x after reversing each of its digits


            x = 1234
            Res = 4321

            1234 = 
            0001 0010 0011 0100


            4321 = 
            0100 0011 0010 0001

            1234236467
            wouldnt fit 
        '''
        if x > math.pow(2, 31) - 1 or x < -(math.pow(2, 31)):
            return 0
        min = -math.pow(2, 31)
        max = math.pow(2, 31) - 1

        res = 0
        while x != 0:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if (res > max // 10 or
            (res == max // 10 and digit > max % 10)):
                return 0
            
            if (res < int(min / 10) or
            (res == int(min / 10) and digit < int(math.fmod(min, 10)))):
                return 0
            res = (res * 10) + digit
        return res