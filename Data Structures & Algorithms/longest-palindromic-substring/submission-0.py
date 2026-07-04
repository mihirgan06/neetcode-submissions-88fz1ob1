class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
            Given a string s, return the longest substring of s that is a palindrome
            palindrome reads same forward and backward

            s = ababd
            output = bab
            obv intuition is to solve this shit with two pointers but lets think

            how can dp be applied
            Using Bottom up:
                We initialize a dp array which says True or false if the cell is a palindrome
        '''
        n = len(s)
        dp = [[False] * n for i in range(n)]
        res = ''

        for length in range(1, n + 1):
            #for every length
            for l in range(0, n - length + 1):
                #check every substring

                r = l + length - 1
                if length == 1:
                    dp[l][r] = True
                elif length == 2:
                    dp[l][r] = s[l] == s[r]
                elif length >= 3:
                    dp[l][r] = s[l] == s[r] and dp[l + 1][r - 1]

                if dp[l][r] and length > len(res):
                    res = s[l:r + 1]
        return res
        
                

            
            
        