class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
            Given a string s, return the number of substrings within s that are palindromes
            palindrome = string that reads the same forward and backward

            s = abc
            Output = 3 
            a, b, c

            s = aaa
            a, a, a, aa, aa, aaa

            Dynamic Programming:
            Recursiveluy to be a palindrome, the endpoints muyst be equal and everything inside muyst also be a palindrom
            so for abc,
            a = palindrome bc a = a and theres nothing inside a its vacously a palindrome


            dp[l][r] = whether s[l:r] is a palindrome
            - s[l] == s[r]
            - dp[l+1][r-1] inside is a palindrome
            every substring is built and dependant on a smaller substring
        '''
        n, count = len(s), 0
        dp = [[False] * n for i in range(n)]
        

        for length in range(1, n + 1):
            #outer loop chooses substring length
            #fitst check substrings of length 1 then legnth 2...5
            for l in range(0, n - length + 1):
                #choosing starting index
                #if length is 0 --> r = 0 --> "a"
                #if length is 1 --> r = 1 "b"
                #end index is start + length - 1
                r = l + length - 1
                if length == 1:
                    dp[l][r] = True
                
                elif length == 2:
                    dp[l][r] = s[l] == s[r]
                else:
                    dp[l][r] = s[l] == s[r] and dp[l+1][r-1]
                if dp[l][r]:
                    count += 1
        return count

