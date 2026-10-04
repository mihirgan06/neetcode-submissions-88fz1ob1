class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        '''
            you are given three strings s1, s2, and s3

            return true if s3 is formed by interleaving s1 and s2 together or false otherwise

            interleaving two strings s and t into n and m substrings respectively
            where the following conditions are met
            1. |n - m| <= 1 the difference between number of substrings of s and t are 1 at most
            s = s1 + s2 + .... sn
            t = t1 + t2 +....tm
            Interleaving s and t is s1 + t1 + s2 + t2 +....
            or t1 + s1 + ....


            dp[i][j] = did we form an interleaving string (first i + j) cahrs of s3 using the first i chars of s and first j characters of t
        '''
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        dp[0][0] = True
        #two empty strings shoul db etrue

        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i > 0:
                    #if thee previous state was valid and the next character from s1 matches the character we need in s3
                    if dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]:
                        dp[i][j] = True
                if j > 0:
                    if dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]:
                        dp[i][j] = True
        return dp[len(s1)][len(s2)]
        

        