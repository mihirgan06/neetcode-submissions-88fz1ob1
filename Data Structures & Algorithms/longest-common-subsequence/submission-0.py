class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
            Given two strings text1 and text2
            return the longest common subsequence btwn the two strings else retrun 0

            Subsequence = sequence that can be derived from given sequence by deleting some or no elements without changing actual order

            "cat" and "crabt"

            cat is the longest subsequence if we delete b from crabt


            so return 3

            dp[i][j] refers to the length longest common subsequence up to i and j from text1 and text2 respectively



            text1 = abcd
            text 2 = abcd

            entire string so 4


            so take the first i characters from text 1 and j characters from text2
            O(text 1 * text2)


            Setup:
            2D table:
            - text 1 x text 2

            if they match: 1 + dp[i - 1][j - 1]

            if they dont match we take the max of max(dp[i-1][j], dp[i][j - 1])

        '''
        dp = []
        for i in range(len(text1) + 1):
            row = [0] * (len(text2) + 1)
            dp.append(row)
        if len(text1) == 0:
            return 0
        elif len(text2) == 0:
            return 0
        
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                #match
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                #if they dont match
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j - 1])
        return dp[-1][-1]
