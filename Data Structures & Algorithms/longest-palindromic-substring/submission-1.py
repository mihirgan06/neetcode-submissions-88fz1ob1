class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
            Given a string s, return the longest substring of s that is a palindrome
            Reads the same forward and backward
            s = "ababd"
            "bab"

            s = "abbc"
            "bb"

            How do we know for any substring whetehr s[l:r + 1] is a palindrome
            - outer characters match 
            - inside is also a palindrome

            length = 1:
                every single character is a palindrome
            
            length = 2:
                both characters match

            
            length = 3 + 
            - dp[l][r] = s[l] == s[r] and dp[l+1][r-1]
        '''

        n = len(s)
        dp = [[False] * n for _ in range(n)]

        best_start = 0
        best_length = 1

        for length in range(1, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                if length == 1:
                    dp[l][r] = True
                
                elif length == 2:
                    dp[l][r] = s[l] == s[r]
                
                else:
                    dp[l][r] = (
                        s[l] == s[r]
                        and dp[l+1][r-1]
                    )
                if dp[l][r] and length > best_length:
                    best_start = l
                    best_length = length
        return s[best_start:best_start + best_length]