class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        '''
            given 2 string text1 and text2, return the length of the longest common subsequence betwene the two strings if one exists otherwise return 0

            subsequence is a sequence that can be derived from hte given sequence by deleting some or no elements withot changing the order



            "cat" and "crabt"
            cat -- 3
            dp[i][j] = length of lognest common subsequence from the first i characters of text1 and first j characters of text2


            text1 = "abcd", text2 = "abcd"
            length = 4

            text1 = "abcd", text2 = "efgh"
            
            setup for a 2D table
            - the x axis is the characters from text1
            - y axis is the character from text2
            first row is 0s 
            


        '''
        
        dp = [[0] * (len(text2) + 1) for i in range(len(text1) + 1)]
        
        if len(text1) == 0 or len(text2) == 0:
            return 0
        

        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i-1][j - 1]
                else:
                    dp[i][j] = max(dp[i -1][j], dp[i][j - 1])
        return dp[-1][-1]

                
        
        