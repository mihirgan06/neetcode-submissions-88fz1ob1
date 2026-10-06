class Solution:
    def numDecodings(self, s: str) -> int:
        '''
            'A' --> 1
            B --> 2
            ...
            Z --> 26

            to decode a message: digits must be grouped and then mapped back into letters using the reverse
            1012 ==> JAB
            or JL
            0 cannot be converted into anything because it contains a leading 0

            if were looking at 2 numbers they must be between 10 and 26
            if were lookinga t 1 number it can be anything between 1 and 9


            dp[i] = number of ways to decode the first i characters of s
            dp[0] = 1 theres 1 way to decode an emopty string do nothing
            dp[1] = 1 

        '''
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        
        dp[1] = 1 if s[0] != '0' else 0

        for i in range(2, len(s) + 1):
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]
            if "10" <= s[i - 2:i] <= "26":
                dp[i] += dp[i - 2]
        return dp[len(s)]



        