class Solution:
    def numDecodings(self, s: str) -> int:
        '''
            a string consisting of uppercase english characters can be encoded to a numebr using the folloiwing mapping


            A --> 1
            B --> 2
            ...
            Z --> 26
            to decode a message, digits must be grouped and then mapped back into letter susing the reverse of the mappign above

            1012 --> JAB
            JL with the groupign 1012
            0 cannot be mapped into anything as a leaading zero
            given a string s containing only digits return the number of ways to decode it

            s = "12"
            we can take 12 as L or take 1 then 2 as AB

            s = "01" 0


            there is one way to decode the empty string --> do nothing


        '''

        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1 if s[0] != "0" else 0

        for i in range(2, len(s) + 1):
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]
            if 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[len(s)]
            


