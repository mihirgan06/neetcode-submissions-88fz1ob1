class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
            given two strings text1 and text2
            return length of longest common subsequence between the two strings if one exists otherwise return 0

            text1 = "cat", text2 = "crabt"

            output = 3

            text1 = "cat"
            text2 = "crabt"

            common subsequence of two strings is a subsequence that exists in both strings
            dp[i][j] = longest common subsequnce between the first i characters of text1 and first j characters of text2

            


            text1 = "cat", text2 = "crabt" 
            3

            text1 = "abcd", text2 = "abcd"

            4

            text1 = abcd, text2 = efgh
            0

            if the characters match --> 1 + dp[i-1][j-1]
            if the charactrs dont match --> max(dp[i-1][j], dp[i][j-1])

             


        '''
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        if len(text1) == 0 or len(text2) == 0:
            return 0


        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i - 1][j])
        return dp[-1][-1]
                