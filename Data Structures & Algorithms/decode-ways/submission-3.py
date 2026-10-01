class Solution:
    def numDecodings(self, s: str) -> int:
        '''
            a string consists of uppercase english cahracters can be encoded to a number using following mapping

            A --> 1
            B --> 2
            ...
            Z --> 26

            to decode a message, digits must be grouped and then mapped back into the letters using the reverse of the mappign above

            givern a string containing only digits return the number of ways to decode int

            s = "12" --> 2 ways "12" --> L or "1""2" = AB


            we have to create a mapping of all possible numbers to letters
            decision tree


            dp[i] = the number of ways to decode ending at index i

            s = '121'
            1 by itself = A
            12 by itself = L
            21 by itself is its own character
            what if we had 27 --> >26 so cannot be a character

            1 by itself then 2 then 1 --> reaching the end so 1 more way
            reahing the end is 1 way to decode
            12 then 1 --> 1 more way
            3 ways to decode 121
            what if we had 12131
            you can take 3 after but not 31 > 26
            we can only take double digit values if the first digit starts with a 1 then you can take anythign from 0-9
            if it starts with a 2 you can only take 0-6
            if the first digit is anything other than 1 or 2 --> doesnt owrk
            we can either start by taking 1 character or 2 cahracters


            dp[i] = dp[i + 1] + dp[i + 2]


        '''
        dp = {len(s) : 1}
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
            if i + 1 < len(s) and (s[i] == "1" or
               s[i] == "2" and s[i + 1] in "0123456"
            ):
                dp[i] += dp[i + 2]
        return dp[0]




        
        